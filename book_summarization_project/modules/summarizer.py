# modules/summarizer.py

from modules.gemini_api import GeminiClient

def generate_summary(text):
    gemini = GeminiClient()
    prompt = f"Summarize the following text:\n\n{text}"
    return gemini.generate_text(prompt)
