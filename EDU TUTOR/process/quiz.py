from ai_services.granite_client import GraniteClient
from db.pinecone_client import PineconeClient

class QuizGenerator:
    def __init__(self):
        self.granite = GraniteClient()
        self.vector_db = PineconeClient()
    
    def generate_quiz(self, topic, difficulty, student_level=None):
        # Get relevant context from vector DB
        context = self.vector_db.query(topic, top_k=3)
        
        # Generate quiz using Granite
        prompt = f"""
        Generate a {difficulty} level quiz on {topic} for a {student_level} student.
        Context: {context}
        Format: 5 multiple choice questions with 4 options each.
        """
        
        return self.granite.generate(prompt)