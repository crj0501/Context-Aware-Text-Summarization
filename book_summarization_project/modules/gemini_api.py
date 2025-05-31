import os
from google import generativeai as genai

class GeminiClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_text(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"[Gemini Error] {e}"

    def answer_question(self, question, context):
        prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        return self.generate_text(prompt)
    
    
    
    
