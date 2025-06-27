import pinecone
import pandas as pd

pinecone.init(api_key="your_pinecone_key", environment="us-east1-gcp")
index = pinecone.Index("quiz-performance")

# Fetch student quiz data
student_id = "student_123"
results = index.query(vector=[0.25, 0.67, 0.89], top_k=5, include_metadata=True)

# Display insights
for match in results["matches"]:
    print(f"Topic: {match['metadata']['topic']}, Score: {match['metadata']['score']}")