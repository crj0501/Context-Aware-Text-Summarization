# quiz_generator.py
from modules.gemini_api import GeminiClient
import re

class QuizGenerator:
    def __init__(self, summary, num_questions=5):
        self.summary = summary
        self.num_questions = num_questions
        self.gemini = GeminiClient()

    def parse_quiz_response(self, raw_text):
        # Extract questions and answers using regex
        pattern = r'\*\*Question\s*(\d+):\*\*\s*(.*?)\s*(a\).*?)\s*\*\*Answer\s*\1:\*\*\s*(.*?)\s*(?=(\*\*Question\s*\d+:)|$)'
        matches = re.findall(pattern, raw_text, re.DOTALL)

        quiz = []
        for match in matches:
            question_num, question, options, answer, _ = match
            option_lines = [opt.strip() for opt in options.strip().split('\n') if opt.strip()]
            quiz.append({
                "question": question.strip(),
                "options": option_lines,
                "answer": answer.strip()
            })
        return quiz

    def generate_quiz(self):
        prompt = (
            f"Generate a {self.num_questions}-question multiple choice quiz based on the following text.\n\n"
            f"Text:\n{self.summary}\n\n"
            "Format each question like this:\n"
            "**Question 1:** What is ...?\n"
            "a) Option A\nb) Option B\nc) Option C\nd) Option D\n"
            "**Answer 1:** b) Option B\n\n"
            "Continue this format for each question."
        )

        raw_output = self.gemini.generate_text(prompt)
        return self.parse_quiz_response(raw_output)
