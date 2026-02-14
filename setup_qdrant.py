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