#mock watsonx API call

def generate_quiz_mock(topic):
    return {
        "topic": topic,
        "questions": [
            {"q": f"What is {topic}?", "options": ["A", "B", "C", "D"], "answer": "A"}
        ]
    }




#mock pinecone similarity function

def semantic_similarity_mock(query, documents):
    return sorted(documents, key=lambda x: len(set(query.split()) & set(x.split())), reverse=True)