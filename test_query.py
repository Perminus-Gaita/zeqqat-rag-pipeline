"""
Step 3: Test that your indexed articles are searchable.
Run this after index_articles.py to verify everything works.

Usage: python test_query.py "how do I play the jackpot?"
"""

import sys
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