"""
MDX Article Chunker for RAG
============================
Parses MDX files with YAML frontmatter and splits them into
parent chunks (full sections) and child chunks (paragraphs).

Your format:
- Frontmatter: YAML with sections[], components[], metadata
- Body: ## Heading {/*section:id*/} with {/* Context: ... */} comments
- Components: <InteractiveWrapper>...<ComponentName />...</InteractiveWrapper>
"""

import os
import re
import yaml
import hashlib
from pathlib import Path


def parse_mdx(file_path: str) -> dict:
    """
    Parse an MDX file into frontmatter (dict) + body (string).
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split frontmatter from body
    # Matches --- at start, YAML content, --- then body
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", content, re.DOTALL)
    if not match:
        raise ValueError(f"Could not parse frontmatter in {file_path}")

    frontmatter = yaml.safe_load(match.group(1))
    body = match.group(2).strip()

    return {"frontmatter": frontmatter, "body": body}


def split_into_sections(body: str) -> list[dict]:
    """
    Split the MDX body into sections based on ## Heading {/*section:id*/} markers.

    Returns a list of:
    {
        "id": "section-id",
        "heading": "Section Heading",
        "context": "Context comment if present",
        "content": "Full section text (without heading line)",
        "paragraphs": ["paragraph1", "paragraph2", ...]
    }
    """
    # Pattern: ## Heading Text {/*section:section-id*/}
    section_pattern = re.compile(
        r"^## (.+?)\s*\{/\*section:([\w-]+)\*/\}\s*$",
        re.MULTILINE
    )

    # Find all section markers
    markers = list(section_pattern.finditer(body))

    if not markers:
        # No sections found — treat entire body as one section
        return [{
            "id": "main",
            "heading": "Main",
            "context": "",
            "content": body.strip(),
            "paragraphs": _extract_paragraphs(body.strip())
        }]

    sections = []

    # Capture any content BEFORE the first section (e.g., top-level components)
    pre_content = body[:markers[0].start()].strip()

    for i, marker in enumerate(markers):
        heading = marker.group(1).strip()
        section_id = marker.group(2).strip()

        # Get content between this heading and the next (or end of body)
        start = marker.end()
        end = markers[i + 1].start() if i + 1 < len(markers) else len(body)
        raw_content = body[start:end].strip()

        # Extract context comment: {/* Context: ... */}
        context = ""
        context_match = re.match(
            r"\{/\*\s*Context:\s*(.*?)\s*\*/\}\s*",
            raw_content,
            re.DOTALL
        )
        if context_match:
            context = context_match.group(1).strip()
            raw_content = raw_content[context_match.end():].strip()

        sections.append({
            "id": section_id,
            "heading": heading,
            "context": context,
            "content": raw_content,
            "paragraphs": _extract_paragraphs(raw_content)
        })

    # If there was content before the first section (top-level components),
    # attach it to the first section or create a special "intro" section
    if pre_content:
        sections.insert(0, {
            "id": "intro",
            "heading": "Introduction",
            "context": "",
            "content": pre_content,
            "paragraphs": _extract_paragraphs(pre_content)
        })

    return sections


def _extract_paragraphs(content: str) -> list[str]:
    """
    Split section content into meaningful paragraphs.
    Filters out empty lines and standalone component tags.
    """
    # Split on double newlines (standard paragraph separator)
    raw_paragraphs = re.split(r"\n\s*\n", content)

    paragraphs = []
    for p in raw_paragraphs:
        p = p.strip()
        if not p:
            continue

        # Skip standalone context comments
        if re.match(r"^\{/\*.*\*/\}$", p, re.DOTALL):
            continue

        paragraphs.append(p)

    return paragraphs


def _is_component_block(text: str) -> bool:
    """Check if a paragraph is a component block."""
    return bool(re.match(r"^\s*<InteractiveWrapper", text))


def _get_component_description(frontmatter: dict, section_id: str) -> str:
    """
    Look up the plain-English component description from frontmatter
    for a given section.
    """
    components = frontmatter.get("components", []) or []
    for comp in components:
        if comp.get("section") == section_id:
            return comp.get("description", "")
    return ""


def chunk_article(file_path: str) -> list[dict]:
    """
    Main function: takes an MDX file path, returns parent + child chunks.

    Each chunk has:
    - id: unique identifier
    - text: the text to embed / give to Claude
    - type: "parent" or "child"
    - parent_id: (child only) links to parent
    - metadata: article_title, section_title, section_summary, url, etc.
    """
    parsed = parse_mdx(file_path)
    fm = parsed["frontmatter"]
    body = parsed["body"]

    # Build lookup for section summaries from frontmatter
    section_summaries = {}
    for s in (fm.get("sections") or []):
        section_summaries[s["id"]] = s.get("summary", "")

    # Article-level metadata
    article_id = fm.get("canonicalUrl", "").strip("/").replace("/", "-") or Path(file_path).stem
    article_title = fm.get("title", "")
    article_url = fm.get("canonicalUrl", "")
    article_description = fm.get("description", "")
    article_category = fm.get("category", "")
    article_tags = fm.get("tags", []) or []
    article_type = fm.get("articleType", "")

    # Split body into sections
    sections = split_into_sections(body)

    chunks = []

    for section in sections:
        section_id = section["id"]
        section_heading = section["heading"]
        section_context = section["context"]
        section_summary = section_summaries.get(section_id, "")

        # Check if this section has a component
        component_desc = _get_component_description(fm, section_id)

        # =====================
        # PARENT CHUNK
        # =====================
        # The full section text that Claude will see when a child matches.
        # Includes: article title, section heading, context, component description, full text.

        parent_text_parts = [
            f"Article: {article_title}",
            f"Section: {section_heading}",
        ]
        if section_context:
            parent_text_parts.append(f"Context: {section_context}")
        if section_summary:
            parent_text_parts.append(f"Summary: {section_summary}")
        if component_desc:
            parent_text_parts.append(f"Interactive component: {component_desc}")

        parent_text_parts.append("")  # blank line separator

        # For the parent, include all text paragraphs.
        # Replace component blocks with their description.
        for para in section["paragraphs"]:
            if _is_component_block(para):
                if component_desc:
                    parent_text_parts.append(f"[Interactive: {component_desc}]")
            else:
                parent_text_parts.append(para)

        parent_text = "\n\n".join(parent_text_parts)

        parent_id = f"{article_id}__{section_id}"
        parent_chunk = {
            "id": parent_id,
            "text": parent_text,
            "type": "parent",
            "metadata": {
                "article_id": article_id,
                "article_title": article_title,
                "article_description": article_description,
                "article_type": article_type,
                "article_url": article_url,
                "category": article_category,
                "tags": article_tags,
                "section_id": section_id,
                "section_title": section_heading,
                "section_summary": section_summary,
                "has_component": bool(component_desc),
                "component_description": component_desc,
            }
        }
        chunks.append(parent_chunk)

        # =====================
        # CHILD CHUNKS
        # =====================
        # Each paragraph becomes a child chunk (used for search).
        # Prepend article title + section heading so embedding has context.

        text_paragraphs = []
        for para in section["paragraphs"]:
            if _is_component_block(para):
                # Replace component with its description as a paragraph
                if component_desc:
                    text_paragraphs.append(f"[Interactive: {component_desc}]")
            else:
                text_paragraphs.append(para)

        # If the section only has 1-2 short paragraphs, don't split further —
        # just make one child chunk for the whole section
        if len(text_paragraphs) <= 2:
            child_text = (
                f"{article_title} > {section_heading}\n\n"
                + "\n\n".join(text_paragraphs)
            )
            child_chunk = {
                "id": f"{parent_id}__p0",
                "text": child_text,
                "type": "child",
                "parent_id": parent_id,
                "metadata": parent_chunk["metadata"].copy()
            }
            chunks.append(child_chunk)
        else:
            # Multiple paragraphs — each becomes a child
            for i, para in enumerate(text_paragraphs):
                child_text = (
                    f"{article_title} > {section_heading}\n\n"
                    f"{para}"
                )
                child_chunk = {
                    "id": f"{parent_id}__p{i}",
                    "text": child_text,
                    "type": "child",
                    "parent_id": parent_id,
                    "metadata": parent_chunk["metadata"].copy()
                }
                chunks.append(child_chunk)

    return chunks


def chunk_all_articles(articles_dir: str) -> list[dict]:
    """
    Process all .mdx files in a directory.
    Returns all chunks from all articles.
    """
    all_chunks = []
    mdx_files = sorted(Path(articles_dir).glob("**/*.mdx"))

    print(f"Found {len(mdx_files)} MDX files")

    for file_path in mdx_files:
        try:
            chunks = chunk_article(str(file_path))
            parents = [c for c in chunks if c["type"] == "parent"]
            children = [c for c in chunks if c["type"] == "child"]
            print(f"  ✓ {file_path.name}: {len(parents)} sections → {len(children)} child chunks")
            all_chunks.extend(chunks)
        except Exception as e:
            print(f"  ✗ {file_path.name}: ERROR — {e}")

    parents_total = sum(1 for c in all_chunks if c["type"] == "parent")
    children_total = sum(1 for c in all_chunks if c["type"] == "child")
    print(f"\nTotal: {len(all_chunks)} chunks ({parents_total} parents, {children_total} children)")

    return all_chunks


# =============================================================================
# Quick test: run this file directly to test with a single MDX file
# =============================================================================
if __name__ == "__main__":
    import sys
    import json

    if len(sys.argv) < 2:
        print("Usage: python chunk_articles.py <path-to-mdx-file-or-directory>")
        print("  Single file:  python chunk_articles.py article.mdx")
        print("  Directory:    python chunk_articles.py ./articles/")
        sys.exit(1)

    path = sys.argv[1]

    if os.path.isdir(path):
        chunks = chunk_all_articles(path)
    else:
        chunks = chunk_article(path)
        parents = [c for c in chunks if c["type"] == "parent"]
        children = [c for c in chunks if c["type"] == "child"]
        print(f"Created {len(chunks)} chunks ({len(parents)} parents, {len(children)} children)")

    # Print first few chunks as preview
    print("\n" + "=" * 60)
    print("PREVIEW: First 3 chunks")
    print("=" * 60)
    for chunk in chunks[:3]:
        print(f"\n--- {chunk['type'].upper()}: {chunk['id']} ---")
        print(f"Text preview: {chunk['text'][:200]}...")
        print(f"Metadata: {json.dumps({k: v for k, v in chunk['metadata'].items() if k != 'tags'}, indent=2)}")