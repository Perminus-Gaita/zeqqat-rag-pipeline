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