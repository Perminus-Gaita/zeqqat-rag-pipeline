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
