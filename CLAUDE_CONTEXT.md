# CLAUDE_CONTEXT.md — zeqqat-rag-pipeline

> Auto-generated on 2026-02-14 18:31:24
> Do not edit manually. Run `python generate_context.py` to regenerate.

## Project Overview

Python scripts for the RAG (Retrieval-Augmented Generation) pipeline.
These scripts are run ONCE from a local machine to index articles into Qdrant.
They are NOT part of the Next.js app.

## File Structure

```
zeqqat-rag-pipeline/
├── articles/
│   ├── bankroll-management-weekly-jackpots.mdx (2.4 KB)
│   ├── best-apps-jackpot-results-kenya.mdx (7.4 KB)
│   ├── betika-vs-sportpesa-jackpot.mdx (2.7 KB)
│   ├── biggest-jackpot-wins-kenya.mdx (11.7 KB)
│   ├── buy-lottery-tickets-jackpot-kenya.mdx (10.5 KB)
│   ├── common-sportpesa-jackpot-mistakes.mdx (6.5 KB)
│   ├── double-chance-strategy-guide.mdx (2.7 KB)
│   ├── fake-sportpesa-jackpot-winner.mdx (4.5 KB)
│   ├── final-article.mdx (424 bytes)
│   ├── free-sportpesa-draw-counter.mdx (15.3 KB)
│   ├── how-to-analyze-head-to-head-records.mdx (6.6 KB)
│   ├── how-to-analyze-jackpot-fixtures.mdx (2.5 KB)
│   ├── how-to-analyze-team-form-jackpot.mdx (6.6 KB)
│   ├── how-to-deposit-mpesa-sportpesa.mdx (2.7 KB)
│   ├── how-to-predict-away-win.mdx (13.7 KB)
│   ├── how-to-predict-draws.mdx (10.6 KB)
│   ├── how-to-predict-home-win.mdx (13.3 KB)
│   ├── how-to-use-ai-jackpot-predictions.mdx (3.1 KB)
│   ├── increase-chances-winning-sportpesa-jackpot.mdx (16.6 KB)
│   ├── jackpot-betting-psychology.mdx (2.6 KB)
│   ├── jackpot-betting-sites-kenya-reviews.mdx (9.4 KB)
│   ├── jackpot-syndicate-contracts-legal.mdx (2.4 KB)
│   ├── jackpot-syndicate-guide.mdx (2.6 KB)
│   ├── jackpot-winners-kenya.mdx (10.8 KB)
│   ├── midweek-jackpot-strategy-guide.mdx (2.8 KB)
│   ├── midweek-mega-jackpot-predictions.mdx (9.1 KB)
│   ├── odds-winning-sportpesa-jackpot.mdx (11.5 KB)
│   ├── reputable-online-jackpot-games-kenya.mdx (7.6 KB)
│   ├── sms-betting-codes-cheat-sheet.mdx (2.0 KB)
│   ├── sportpesa-app-vs-desktop-comparison.mdx (3.0 KB)
│   ├── sportpesa-jackpot-prediction-websites.mdx (10.4 KB)
│   ├── sportpesa-jackpot-statistics-trends.mdx (3.0 KB)
│   ├── sportpesa-jackpot-tax-guide-2026.mdx (2.4 KB)
│   ├── sportpesa-jackpot-winners-picks.mdx (12.7 KB)
│   ├── sportpesa-registration-guide-2026.mdx (2.1 KB)
│   ├── successful-jackpot-syndicate-examples.mdx (2.3 KB)
│   ├── ultimate-guide-sportpesa-jackpot.mdx (15.7 KB)
│   ├── understanding-jackpot-odds-explained.mdx (2.7 KB)
│   ├── understanding-postponed-match-rules-jackpot.mdx (5.7 KB)
│   ├── value-betting-in-jackpots.mdx (2.6 KB)
│   ├── what-happens-multiple-jackpot-winners.mdx (2.0 KB)
│   ├── what-is-sportpesa-jackpot-beginners.mdx (3.4 KB)
│   ├── what-is-value-betting.mdx (5.4 KB)
│   ├── what-to-do-jackpot-money.mdx (12.6 KB)
│   └── who-can-play-sportpesa-jackpot.mdx (4.1 KB)
├── chunk_articles.py (12.1 KB)
├── CLAUDE_CONTEXT.md (30.3 KB)
├── generate_context.py (4.2 KB)
├── index_articles.py (5.6 KB)
├── requirements.txt (88 bytes)
├── setup_qdrant.py (1.5 KB)
└── test_query.py (3.2 KB)
```

## File Contents

### CLAUDE_CONTEXT.md

```md
# CLAUDE_CONTEXT.md — zeqqat-rag-pipeline

> Auto-generated on 2026-02-14 18:30:42
> Do not edit manually. Run `python generate_context.py` to regenerate.

## Project Overview

Python scripts for the RAG (Retrieval-Augmented Generation) pipeline.
These scripts are run ONCE from a local machine to index articles into Qdrant.
They are NOT part of the Next.js app.

## File Structure

```
zeqqat-rag-pipeline/
├── articles/
│   ├── bankroll-management-weekly-jackpots.mdx (2.4 KB)
│   ├── best-apps-jackpot-results-kenya.mdx (7.4 KB)
│   ├── betika-vs-sportpesa-jackpot.mdx (2.7 KB)
│   ├── biggest-jackpot-wins-kenya.mdx (11.7 KB)
│   ├── buy-lottery-tickets-jackpot-kenya.mdx (10.5 KB)
│   ├── common-sportpesa-jackpot-mistakes.mdx (6.5 KB)
│   ├── double-chance-strategy-guide.mdx (2.7 KB)
│   ├── fake-sportpesa-jackpot-winner.mdx (4.5 KB)
│   ├── final-article.mdx (424 bytes)
│   ├── free-sportpesa-draw-counter.mdx (15.3 KB)
│   ├── how-to-analyze-head-to-head-records.mdx (6.6 KB)
│   ├── how-to-analyze-jackpot-fixtures.mdx (2.5 KB)
│   ├── how-to-analyze-team-form-jackpot.mdx (6.6 KB)
│   ├── how-to-deposit-mpesa-sportpesa.mdx (2.7 KB)
│   ├── how-to-predict-away-win.mdx (13.7 KB)
│   ├── how-to-predict-draws.mdx (10.6 KB)
│   ├── how-to-predict-home-win.mdx (13.3 KB)
│   ├── how-to-use-ai-jackpot-predictions.mdx (3.1 KB)
│   ├── increase-chances-winning-sportpesa-jackpot.mdx (16.6 KB)
│   ├── jackpot-betting-psychology.mdx (2.6 KB)
│   ├── jackpot-betting-sites-kenya-reviews.mdx (9.4 KB)
│   ├── jackpot-syndicate-contracts-legal.mdx (2.4 KB)
│   ├── jackpot-syndicate-guide.mdx (2.6 KB)
│   ├── jackpot-winners-kenya.mdx (10.8 KB)
│   ├── midweek-jackpot-strategy-guide.mdx (2.8 KB)
│   ├── midweek-mega-jackpot-predictions.mdx (9.1 KB)
│   ├── odds-winning-sportpesa-jackpot.mdx (11.5 KB)
│   ├── reputable-online-jackpot-games-kenya.mdx (7.6 KB)
│   ├── sms-betting-codes-cheat-sheet.mdx (2.0 KB)
│   ├── sportpesa-app-vs-desktop-comparison.mdx (3.0 KB)
│   ├── sportpesa-jackpot-prediction-websites.mdx (10.4 KB)
│   ├── sportpesa-jackpot-statistics-trends.mdx (3.0 KB)
│   ├── sportpesa-jackpot-tax-guide-2026.mdx (2.4 KB)
│   ├── sportpesa-jackpot-winners-picks.mdx (12.7 KB)
│   ├── sportpesa-registration-guide-2026.mdx (2.1 KB)
│   ├── successful-jackpot-syndicate-examples.mdx (2.3 KB)
│   ├── ultimate-guide-sportpesa-jackpot.mdx (15.7 KB)
│   ├── understanding-jackpot-odds-explained.mdx (2.7 KB)
│   ├── understanding-postponed-match-rules-jackpot.mdx (5.7 KB)
│   ├── value-betting-in-jackpots.mdx (2.6 KB)
│   ├── what-happens-multiple-jackpot-winners.mdx (2.0 KB)
│   ├── what-is-sportpesa-jackpot-beginners.mdx (3.4 KB)
│   ├── what-is-value-betting.mdx (5.4 KB)
│   ├── what-to-do-jackpot-money.mdx (12.6 KB)
│   └── who-can-play-sportpesa-jackpot.mdx (4.1 KB)
├── chunk_articles.py (12.1 KB)
├── generate_context.py (4.2 KB)
├── index_articles.py (5.6 KB)
├── requirements.txt (88 bytes)
├── setup_qdrant.py (1.5 KB)
└── test_query.py (3.2 KB)
```

## File Contents

### chunk_articles.py

```py
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
```

### generate_context.py

```py
"""
Generate CLAUDE_CONTEXT.md for the zeqqat-rag-pipeline repo.
Run manually or automatically via pre-commit hook.

Usage: python generate_context.py
"""

import os
from pathlib import Path
from datetime import datetime

# Directories and files to ignore
IGNORE_DIRS = {
    "venv", "__pycache__", ".git", ".vscode", "node_modules",
    ".idea", "dist", "build", ".egg-info"
}
IGNORE_FILES = {".DS_Store", ".env"}
IGNORE_EXTENSIONS = {".pyc", ".pyo"}

# Files to include full content for
INCLUDE_CONTENT = {".py", ".txt", ".md", ".yml", ".yaml", ".toml", ".cfg", ".json"}

# Max file size to include content (50KB)
MAX_FILE_SIZE = 50_000


def should_ignore(path: Path) -> bool:
    """Check if a path should be ignored."""
    for part in path.parts:
        if part in IGNORE_DIRS:
            return True
        if part.startswith(".") and part not in {".", ".."}:
            return True
    if path.name in IGNORE_FILES:
        return True
    if path.suffix in IGNORE_EXTENSIONS:
        return True
    return False


def get_file_tree(root: Path, prefix: str = "", is_last: bool = True) -> list[str]:
    """Generate a visual file tree."""
    lines = []
    
    items = sorted(root.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    items = [item for item in items if not should_ignore(item)]
    
    for i, item in enumerate(items):
        is_last_item = (i == len(items) - 1)
        connector = "└── " if is_last_item else "├── "
        
        if item.is_dir():
            lines.append(f"{prefix}{connector}{item.name}/")
            extension = "    " if is_last_item else "│   "
            lines.extend(get_file_tree(item, prefix + extension, is_last_item))
        else:
            size = item.stat().st_size
            size_str = f"{size:,} bytes" if size < 1024 else f"{size/1024:.1f} KB"
            lines.append(f"{prefix}{connector}{item.name} ({size_str})")
    
    return lines


def get_file_contents(root: Path) -> list[dict]:
    """Get contents of all relevant files."""
    files = []
    
    for path in sorted(root.rglob("*")):
        if path.is_file() and not should_ignore(path):
            if path.suffix in INCLUDE_CONTENT and path.stat().st_size <= MAX_FILE_SIZE:
                try:
                    content = path.read_text(encoding="utf-8")
                    files.append({
                        "path": str(path.relative_to(root)),
                        "content": content
                    })
                except (UnicodeDecodeError, PermissionError):
                    pass
    
    return files


def generate_context():
    """Generate the CLAUDE_CONTEXT.md file."""
    root = Path(".")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    lines = []
    lines.append("# CLAUDE_CONTEXT.md — zeqqat-rag-pipeline")
    lines.append(f"\n> Auto-generated on {now}")
    lines.append("> Do not edit manually. Run `python generate_context.py` to regenerate.")
    lines.append("")
    
    # Project description
    lines.append("## Project Overview")
    lines.append("")
    lines.append("Python scripts for the RAG (Retrieval-Augmented Generation) pipeline.")
    lines.append("These scripts are run ONCE from a local machine to index articles into Qdrant.")
    lines.append("They are NOT part of the Next.js app.")
    lines.append("")
    
    # File tree
    lines.append("## File Structure")
    lines.append("")
    lines.append("```")
    lines.append("zeqqat-rag-pipeline/")
    tree = get_file_tree(root)
    lines.extend(tree)
    lines.append("```")
    lines.append("")
    
    # File contents
    lines.append("## File Contents")
    lines.append("")
    
    files = get_file_contents(root)
    for f in files:
        ext = Path(f["path"]).suffix.lstrip(".")
        lines.append(f"### {f['path']}")
        lines.append("")
        lines.append(f"```{ext}")
        lines.append(f["content"].rstrip())
        lines.append("```")
        lines.append("")
    
    # Write the file
    output = "\n".join(lines)
    Path("CLAUDE_CONTEXT.md").write_text(output, encoding="utf-8")
    
    print(f"✅ Generated CLAUDE_CONTEXT.md ({len(files)} files documented)")
    print(f"   File tree + full contents of: {', '.join(f['path'] for f in files)}")


if __name__ == "__main__":
    generate_context()
```

### index_articles.py

```py
"""
Step 2: Embed all chunks and store them in Qdrant.
Run this after setup_qdrant.py and after chunking your articles.

Usage: python index_articles.py ./path-to-your-articles/

This will:
1. Chunk all MDX files in the directory
2. Generate dense embeddings (Voyage AI)
3. Generate sparse embeddings (SPLADE via FastEmbed)
4. Store everything in Qdrant

For 45 articles (~500 chunks), this takes roughly 2-5 minutes.
"""

import sys
import os
import time
import voyageai
from fastembed import SparseTextEmbedding
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, SparseVector
from chunk_articles import chunk_all_articles

# ============================================================
# YOUR CREDENTIALS — fill these in
# ============================================================
QDRANT_URL = os.environ["QDRANT_CLUSTER_ENDPOINT"]
QDRANT_API_KEY = os.environ["QDRANT_API_KEY"] 
VOYAGE_API_KEY = "YOUR_VOYAGE_API_KEY"

COLLECTION_NAME = "articles"
# ============================================================

# How many texts to embed per API call (Voyage supports up to 128)
BATCH_SIZE = 64


def main():
    if len(sys.argv) < 2:
        print("Usage: python index_articles.py ./path-to-your-articles/")
        sys.exit(1)

    articles_dir = sys.argv[1]

    # --- Initialize clients ---
    print("Initializing clients...")
    voyage = voyageai.Client(api_key=VOYAGE_API_KEY)
    sparse_model = SparseTextEmbedding(model_name="Qdrant/bm42-all-minilm-l6-v2-attentions")
    qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

    # --- Chunk all articles ---
    print(f"\nChunking articles from: {articles_dir}")
    all_chunks = chunk_all_articles(articles_dir)

    # Only index CHILD chunks (those are what we search against)
    # Parent texts are stored in the payload for retrieval
    parents = {c["id"]: c for c in all_chunks if c["type"] == "parent"}
    children = [c for c in all_chunks if c["type"] == "child"]

    print(f"\nReady to index {len(children)} child chunks")
    print(f"({len(parents)} parent chunks will be stored as payload)\n")

    if not children:
        print("No chunks to index!")
        return

    # --- Generate embeddings in batches ---
    all_texts = [c["text"] for c in children]

    # Dense embeddings (Voyage AI)
    print("Generating dense embeddings (Voyage AI)...")
    dense_embeddings = []
    for i in range(0, len(all_texts), BATCH_SIZE):
        batch = all_texts[i : i + BATCH_SIZE]
        result = voyage.embed(
            batch,
            model="voyage-3",
            input_type="document"
        )
        dense_embeddings.extend(result.embeddings)
        print(f"  Dense: {len(dense_embeddings)}/{len(all_texts)} done")
        time.sleep(0.1)  # small delay to avoid rate limits

    # Sparse embeddings (SPLADE via FastEmbed — runs locally, no API call)
    print("Generating sparse embeddings (SPLADE)...")
    sparse_embeddings = list(sparse_model.embed(all_texts))
    print(f"  Sparse: {len(sparse_embeddings)}/{len(all_texts)} done")

    # --- Build Qdrant points ---
    print("\nBuilding Qdrant points...")
    points = []
    for i, child in enumerate(children):
        # Look up the parent text for this child
        parent_id = child.get("parent_id", "")
        parent_text = parents[parent_id]["text"] if parent_id in parents else child["text"]

        sparse = sparse_embeddings[i]

        point = PointStruct(
            id=i,
            vector={
                "dense": dense_embeddings[i],
                "sparse": SparseVector(
                    indices=sparse.indices.tolist(),
                    values=sparse.values.tolist()
                )
            },
            payload={
                # What Claude will see (the rich parent chunk)
                "parent_text": parent_text,

                # The child text (what was actually embedded)
                "child_text": child["text"],

                # IDs for linking
                "chunk_id": child["id"],
                "parent_id": parent_id,

                # Metadata for filtering and citation
                "article_id": child["metadata"]["article_id"],
                "article_title": child["metadata"]["article_title"],
                "article_description": child["metadata"]["article_description"],
                "article_type": child["metadata"]["article_type"],
                "article_url": child["metadata"]["article_url"],
                "category": child["metadata"]["category"],
                "tags": child["metadata"]["tags"],
                "section_id": child["metadata"]["section_id"],
                "section_title": child["metadata"]["section_title"],
                "section_summary": child["metadata"]["section_summary"],
                "has_component": child["metadata"]["has_component"],
                "component_description": child["metadata"]["component_description"],
            }
        )
        points.append(point)

    # --- Upload to Qdrant in batches ---
    print(f"\nUploading {len(points)} points to Qdrant...")
    UPLOAD_BATCH = 100
    for i in range(0, len(points), UPLOAD_BATCH):
        batch = points[i : i + UPLOAD_BATCH]
        qdrant.upsert(
            collection_name=COLLECTION_NAME,
            points=batch
        )
        print(f"  Uploaded: {min(i + UPLOAD_BATCH, len(points))}/{len(points)}")

    # --- Verify ---
    collection_info = qdrant.get_collection(COLLECTION_NAME)
    print(f"\n✅ Done! Collection '{COLLECTION_NAME}' now has {collection_info.points_count} points")
    print(f"   Dense vectors: {collection_info.config.params.vectors['dense'].size} dimensions")
    print(f"\nYou can now query this from your Next.js app!")


if __name__ == "__main__":
    main()
```

### requirements.txt

```txt
pyyaml>=6.0
voyageai>=0.3.0
fastembed>=0.4.0
qdrant-client>=1.12.0
python-dotenv>=1.0.0
```

### setup_qdrant.py

```py
"""
Step 1: Create the Qdrant collection.
Run this ONCE before indexing.

Usage: python setup_qdrant.py
"""

import os
from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams, SparseVectorParams, Distance, SparseIndexParams
)

# ============================================================
# YOUR CREDENTIALS — fill these in
# ============================================================
QDRANT_URL = os.environ["QDRANT_CLUSTER_ENDPOINT"]      # e.g. "https://abc123.us-east4-0.gcp.cloud.qdrant.io:6333"
QDRANT_API_KEY = os.environ["QDRANT_API_KEY"]     # from Qdrant Cloud dashboard

COLLECTION_NAME = "articles"
# ============================================================

client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

# Delete if it already exists (safe to re-run)
if client.collection_exists(COLLECTION_NAME):
    client.delete_collection(COLLECTION_NAME)
    print(f"Deleted existing '{COLLECTION_NAME}' collection")

# Create collection with both vector types
client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config={
        "dense": VectorParams(
            size=1024,                  # Voyage voyage-3 outputs 1024 dimensions
            distance=Distance.COSINE
        )
    },
    sparse_vectors_config={
        "sparse": SparseVectorParams(
            index=SparseIndexParams()
        )
    }
)

print(f"✅ Collection '{COLLECTION_NAME}' created!")
print(f"   Dense vectors: 1024 dimensions, cosine distance")
print(f"   Sparse vectors: enabled (for SPLADE)")
```

### test_query.py

```py
"""
Step 3: Test that your indexed articles are searchable.
Run this after index_articles.py to verify everything works.

Usage: python test_query.py "how do I play the jackpot?"
"""

import sys
import os
import voyageai
from fastembed import SparseTextEmbedding
from qdrant_client import QdrantClient
from qdrant_client.models import SparseVector, Prefetch, FusionQuery

# ============================================================
# YOUR CREDENTIALS — fill these in (same as other files)
# ============================================================
QDRANT_URL = os.environ["QDRANT_CLUSTER_ENDPOINT"]
QDRANT_API_KEY = os.environ["QDRANT_API_KEY"] 
VOYAGE_API_KEY = "YOUR_VOYAGE_API_KEY"

COLLECTION_NAME = "articles"
# ============================================================


def search(question: str, top_k: int = 5):
    """Search articles and return results with reranking."""

    voyage = voyageai.Client(api_key=VOYAGE_API_KEY)
    sparse_model = SparseTextEmbedding(model_name="Qdrant/bm42-all-minilm-l6-v2-attentions")
    qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

    # 1. Embed the question
    print(f"\n🔍 Searching: \"{question}\"\n")

    dense_vector = voyage.embed(
        [question],
        model="voyage-3",
        input_type="query"
    ).embeddings[0]

    sparse_result = list(sparse_model.query_embed(question))[0]
    sparse_vector = SparseVector(
        indices=sparse_result.indices.tolist(),
        values=sparse_result.values.tolist()
    )

    # 2. Hybrid search in Qdrant
    results = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        prefetch=[
            Prefetch(query=dense_vector, using="dense", limit=100),
            Prefetch(query=sparse_vector, using="sparse", limit=100),
        ],
        query=FusionQuery(fusion="dbsf"),
        limit=50,
    )

    if not results.points:
        print("No results found.")
        return

    # 3. Rerank with Voyage
    candidate_texts = [p.payload["parent_text"] for p in results.points]

    reranked = voyage.rerank(
        query=question,
        documents=candidate_texts,
        model="rerank-2",
        top_k=top_k
    )

    # 4. Display results
    print(f"Top {top_k} results after reranking:\n")
    print("=" * 70)

    for rank, item in enumerate(reranked.results, 1):
        point = results.points[item.index]
        payload = point.payload

        print(f"\n#{rank} (score: {item.relevance_score:.4f})")
        print(f"   Article: {payload['article_title']}")
        print(f"   Section: {payload['section_title']}")
        print(f"   URL:     {payload['article_url']}")
        if payload.get("has_component"):
            print(f"   Component: {payload['component_description'][:80]}...")
        print(f"   Preview: {payload['parent_text'][:200]}...")
        print("-" * 70)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_query.py \"your question here\"")
        print("\nExamples:")
        print('  python test_query.py "how do I play the jackpot?"')
        print('  python test_query.py "what are the odds of winning?"')
        print('  python test_query.py "betting strategy for draws"')
        sys.exit(1)

    question = " ".join(sys.argv[1:])
    search(question)
```
```

### chunk_articles.py

```py
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
```

### generate_context.py

```py
"""
Generate CLAUDE_CONTEXT.md for the zeqqat-rag-pipeline repo.
Run manually or automatically via pre-commit hook.

Usage: python generate_context.py
"""

import os
from pathlib import Path
from datetime import datetime

# Directories and files to ignore
IGNORE_DIRS = {
    "venv", "__pycache__", ".git", ".vscode", "node_modules",
    ".idea", "dist", "build", ".egg-info"
}
IGNORE_FILES = {".DS_Store", ".env"}
IGNORE_EXTENSIONS = {".pyc", ".pyo"}

# Files to include full content for
INCLUDE_CONTENT = {".py", ".txt", ".md", ".yml", ".yaml", ".toml", ".cfg", ".json"}

# Max file size to include content (50KB)
MAX_FILE_SIZE = 50_000


def should_ignore(path: Path) -> bool:
    """Check if a path should be ignored."""
    for part in path.parts:
        if part in IGNORE_DIRS:
            return True
        if part.startswith(".") and part not in {".", ".."}:
            return True
    if path.name in IGNORE_FILES:
        return True
    if path.suffix in IGNORE_EXTENSIONS:
        return True
    return False


def get_file_tree(root: Path, prefix: str = "", is_last: bool = True) -> list[str]:
    """Generate a visual file tree."""
    lines = []
    
    items = sorted(root.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    items = [item for item in items if not should_ignore(item)]
    
    for i, item in enumerate(items):
        is_last_item = (i == len(items) - 1)
        connector = "└── " if is_last_item else "├── "
        
        if item.is_dir():
            lines.append(f"{prefix}{connector}{item.name}/")
            extension = "    " if is_last_item else "│   "
            lines.extend(get_file_tree(item, prefix + extension, is_last_item))
        else:
            size = item.stat().st_size
            size_str = f"{size:,} bytes" if size < 1024 else f"{size/1024:.1f} KB"
            lines.append(f"{prefix}{connector}{item.name} ({size_str})")
    
    return lines


def get_file_contents(root: Path) -> list[dict]:
    """Get contents of all relevant files."""
    files = []
    
    for path in sorted(root.rglob("*")):
        if path.is_file() and not should_ignore(path):
            if path.suffix in INCLUDE_CONTENT and path.stat().st_size <= MAX_FILE_SIZE:
                try:
                    content = path.read_text(encoding="utf-8")
                    files.append({
                        "path": str(path.relative_to(root)),
                        "content": content
                    })
                except (UnicodeDecodeError, PermissionError):
                    pass
    
    return files


def generate_context():
    """Generate the CLAUDE_CONTEXT.md file."""
    root = Path(".")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    lines = []
    lines.append("# CLAUDE_CONTEXT.md — zeqqat-rag-pipeline")
    lines.append(f"\n> Auto-generated on {now}")
    lines.append("> Do not edit manually. Run `python generate_context.py` to regenerate.")
    lines.append("")
    
    # Project description
    lines.append("## Project Overview")
    lines.append("")
    lines.append("Python scripts for the RAG (Retrieval-Augmented Generation) pipeline.")
    lines.append("These scripts are run ONCE from a local machine to index articles into Qdrant.")
    lines.append("They are NOT part of the Next.js app.")
    lines.append("")
    
    # File tree
    lines.append("## File Structure")
    lines.append("")
    lines.append("```")
    lines.append("zeqqat-rag-pipeline/")
    tree = get_file_tree(root)
    lines.extend(tree)
    lines.append("```")
    lines.append("")
    
    # File contents
    lines.append("## File Contents")
    lines.append("")
    
    files = get_file_contents(root)
    for f in files:
        ext = Path(f["path"]).suffix.lstrip(".")
        lines.append(f"### {f['path']}")
        lines.append("")
        lines.append(f"```{ext}")
        lines.append(f["content"].rstrip())
        lines.append("```")
        lines.append("")
    
    # Write the file
    output = "\n".join(lines)
    Path("CLAUDE_CONTEXT.md").write_text(output, encoding="utf-8")
    
    print(f"✅ Generated CLAUDE_CONTEXT.md ({len(files)} files documented)")
    print(f"   File tree + full contents of: {', '.join(f['path'] for f in files)}")


if __name__ == "__main__":
    generate_context()
```

### index_articles.py

```py
"""
Step 2: Embed all chunks and store them in Qdrant.
Run this after setup_qdrant.py and after chunking your articles.

Usage: python index_articles.py ./path-to-your-articles/

This will:
1. Chunk all MDX files in the directory
2. Generate dense embeddings (Voyage AI)
3. Generate sparse embeddings (SPLADE via FastEmbed)
4. Store everything in Qdrant

For 45 articles (~500 chunks), this takes roughly 2-5 minutes.
"""

import sys
import os
import time
import voyageai
from fastembed import SparseTextEmbedding
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, SparseVector
from chunk_articles import chunk_all_articles

# ============================================================
# YOUR CREDENTIALS — fill these in
# ============================================================
QDRANT_URL = os.environ["QDRANT_CLUSTER_ENDPOINT"]
QDRANT_API_KEY = os.environ["QDRANT_API_KEY"] 
VOYAGE_API_KEY = "YOUR_VOYAGE_API_KEY"

COLLECTION_NAME = "articles"
# ============================================================

# How many texts to embed per API call (Voyage supports up to 128)
BATCH_SIZE = 64


def main():
    if len(sys.argv) < 2:
        print("Usage: python index_articles.py ./path-to-your-articles/")
        sys.exit(1)

    articles_dir = sys.argv[1]

    # --- Initialize clients ---
    print("Initializing clients...")
    voyage = voyageai.Client(api_key=VOYAGE_API_KEY)
    sparse_model = SparseTextEmbedding(model_name="Qdrant/bm42-all-minilm-l6-v2-attentions")
    qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

    # --- Chunk all articles ---
    print(f"\nChunking articles from: {articles_dir}")
    all_chunks = chunk_all_articles(articles_dir)

    # Only index CHILD chunks (those are what we search against)
    # Parent texts are stored in the payload for retrieval
    parents = {c["id"]: c for c in all_chunks if c["type"] == "parent"}
    children = [c for c in all_chunks if c["type"] == "child"]

    print(f"\nReady to index {len(children)} child chunks")
    print(f"({len(parents)} parent chunks will be stored as payload)\n")

    if not children:
        print("No chunks to index!")
        return

    # --- Generate embeddings in batches ---
    all_texts = [c["text"] for c in children]

    # Dense embeddings (Voyage AI)
    print("Generating dense embeddings (Voyage AI)...")
    dense_embeddings = []
    for i in range(0, len(all_texts), BATCH_SIZE):
        batch = all_texts[i : i + BATCH_SIZE]
        result = voyage.embed(
            batch,
            model="voyage-3",
            input_type="document"
        )
        dense_embeddings.extend(result.embeddings)
        print(f"  Dense: {len(dense_embeddings)}/{len(all_texts)} done")
        time.sleep(0.1)  # small delay to avoid rate limits

    # Sparse embeddings (SPLADE via FastEmbed — runs locally, no API call)
    print("Generating sparse embeddings (SPLADE)...")
    sparse_embeddings = list(sparse_model.embed(all_texts))
    print(f"  Sparse: {len(sparse_embeddings)}/{len(all_texts)} done")

    # --- Build Qdrant points ---
    print("\nBuilding Qdrant points...")
    points = []
    for i, child in enumerate(children):
        # Look up the parent text for this child
        parent_id = child.get("parent_id", "")
        parent_text = parents[parent_id]["text"] if parent_id in parents else child["text"]

        sparse = sparse_embeddings[i]

        point = PointStruct(
            id=i,
            vector={
                "dense": dense_embeddings[i],
                "sparse": SparseVector(
                    indices=sparse.indices.tolist(),
                    values=sparse.values.tolist()
                )
            },
            payload={
                # What Claude will see (the rich parent chunk)
                "parent_text": parent_text,

                # The child text (what was actually embedded)
                "child_text": child["text"],

                # IDs for linking
                "chunk_id": child["id"],
                "parent_id": parent_id,

                # Metadata for filtering and citation
                "article_id": child["metadata"]["article_id"],
                "article_title": child["metadata"]["article_title"],
                "article_description": child["metadata"]["article_description"],
                "article_type": child["metadata"]["article_type"],
                "article_url": child["metadata"]["article_url"],
                "category": child["metadata"]["category"],
                "tags": child["metadata"]["tags"],
                "section_id": child["metadata"]["section_id"],
                "section_title": child["metadata"]["section_title"],
                "section_summary": child["metadata"]["section_summary"],
                "has_component": child["metadata"]["has_component"],
                "component_description": child["metadata"]["component_description"],
            }
        )
        points.append(point)

    # --- Upload to Qdrant in batches ---
    print(f"\nUploading {len(points)} points to Qdrant...")
    UPLOAD_BATCH = 100
    for i in range(0, len(points), UPLOAD_BATCH):
        batch = points[i : i + UPLOAD_BATCH]
        qdrant.upsert(
            collection_name=COLLECTION_NAME,
            points=batch
        )
        print(f"  Uploaded: {min(i + UPLOAD_BATCH, len(points))}/{len(points)}")

    # --- Verify ---
    collection_info = qdrant.get_collection(COLLECTION_NAME)
    print(f"\n✅ Done! Collection '{COLLECTION_NAME}' now has {collection_info.points_count} points")
    print(f"   Dense vectors: {collection_info.config.params.vectors['dense'].size} dimensions")
    print(f"\nYou can now query this from your Next.js app!")


if __name__ == "__main__":
    main()
```

### requirements.txt

```txt
pyyaml>=6.0
voyageai>=0.3.0
fastembed>=0.4.0
qdrant-client>=1.12.0
python-dotenv>=1.0.0
```

### setup_qdrant.py

```py
"""
Step 1: Create the Qdrant collection.
Run this ONCE before indexing.

Usage: python setup_qdrant.py
"""

import os
from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams, SparseVectorParams, Distance, SparseIndexParams
)

# ============================================================
# YOUR CREDENTIALS — fill these in
# ============================================================
QDRANT_URL = os.environ["QDRANT_CLUSTER_ENDPOINT"]      # e.g. "https://abc123.us-east4-0.gcp.cloud.qdrant.io:6333"
QDRANT_API_KEY = os.environ["QDRANT_API_KEY"]     # from Qdrant Cloud dashboard

COLLECTION_NAME = "articles"
# ============================================================

client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

# Delete if it already exists (safe to re-run)
if client.collection_exists(COLLECTION_NAME):
    client.delete_collection(COLLECTION_NAME)
    print(f"Deleted existing '{COLLECTION_NAME}' collection")

# Create collection with both vector types
client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config={
        "dense": VectorParams(
            size=1024,                  # Voyage voyage-3 outputs 1024 dimensions
            distance=Distance.COSINE
        )
    },
    sparse_vectors_config={
        "sparse": SparseVectorParams(
            index=SparseIndexParams()
        )
    }
)

print(f"✅ Collection '{COLLECTION_NAME}' created!")
print(f"   Dense vectors: 1024 dimensions, cosine distance")
print(f"   Sparse vectors: enabled (for SPLADE)")
```

### test_query.py

```py
"""
Step 3: Test that your indexed articles are searchable.
Run this after index_articles.py to verify everything works.

Usage: python test_query.py "how do I play the jackpot?"
"""

import sys
import os
import voyageai
from fastembed import SparseTextEmbedding
from qdrant_client import QdrantClient
from qdrant_client.models import SparseVector, Prefetch, FusionQuery

# ============================================================
# YOUR CREDENTIALS — fill these in (same as other files)
# ============================================================
QDRANT_URL = os.environ["QDRANT_CLUSTER_ENDPOINT"]
QDRANT_API_KEY = os.environ["QDRANT_API_KEY"] 
VOYAGE_API_KEY = "YOUR_VOYAGE_API_KEY"

COLLECTION_NAME = "articles"
# ============================================================


def search(question: str, top_k: int = 5):
    """Search articles and return results with reranking."""

    voyage = voyageai.Client(api_key=VOYAGE_API_KEY)
    sparse_model = SparseTextEmbedding(model_name="Qdrant/bm42-all-minilm-l6-v2-attentions")
    qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

    # 1. Embed the question
    print(f"\n🔍 Searching: \"{question}\"\n")

    dense_vector = voyage.embed(
        [question],
        model="voyage-3",
        input_type="query"
    ).embeddings[0]

    sparse_result = list(sparse_model.query_embed(question))[0]
    sparse_vector = SparseVector(
        indices=sparse_result.indices.tolist(),
        values=sparse_result.values.tolist()
    )

    # 2. Hybrid search in Qdrant
    results = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        prefetch=[
            Prefetch(query=dense_vector, using="dense", limit=100),
            Prefetch(query=sparse_vector, using="sparse", limit=100),
        ],
        query=FusionQuery(fusion="dbsf"),
        limit=50,
    )

    if not results.points:
        print("No results found.")
        return

    # 3. Rerank with Voyage
    candidate_texts = [p.payload["parent_text"] for p in results.points]

    reranked = voyage.rerank(
        query=question,
        documents=candidate_texts,
        model="rerank-2",
        top_k=top_k
    )

    # 4. Display results
    print(f"Top {top_k} results after reranking:\n")
    print("=" * 70)

    for rank, item in enumerate(reranked.results, 1):
        point = results.points[item.index]
        payload = point.payload

        print(f"\n#{rank} (score: {item.relevance_score:.4f})")
        print(f"   Article: {payload['article_title']}")
        print(f"   Section: {payload['section_title']}")
        print(f"   URL:     {payload['article_url']}")
        if payload.get("has_component"):
            print(f"   Component: {payload['component_description'][:80]}...")
        print(f"   Preview: {payload['parent_text'][:200]}...")
        print("-" * 70)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_query.py \"your question here\"")
        print("\nExamples:")
        print('  python test_query.py "how do I play the jackpot?"')
        print('  python test_query.py "what are the odds of winning?"')
        print('  python test_query.py "betting strategy for draws"')
        sys.exit(1)

    question = " ".join(sys.argv[1:])
    search(question)
```
