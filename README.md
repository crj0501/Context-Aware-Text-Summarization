# 📚 Context-Aware Book Summarization Project

This project provides an intelligent, modular system for context-aware summarization of books and long texts. It integrates keyword extraction, quiz generation, retrieval-based Q&A, and a web interface to make large document understanding more interactive and efficient.

---

## 🚀 Features

- 🧠 **AI-based Summarization** of long texts.
- 🔍 **Keyword Extraction** for content overview.
- 📄 **Text Extraction** from documents like PDFs.
- ❓ **Quiz Generator** for comprehension checks.
- 🌐 **Web Interface** built with Flask.
- 🔧 Modular codebase for flexibility and scalability.

---

## 🗂️ Project Structure

book_summarization_project/
│
├── app/ # Flask web app
│ ├── init.py
│ ├── routes.py
│ ├── templates/
│ │ └── index.html
│ └── static/
│ └── style.css
│
├── modules/ # Core NLP modules
│ ├── gemini_api.py
│ ├── keyword_extractor.py
│ ├── preprocessor.py
│ ├── quiz_generator.py
│ ├── retrieval_qa.py
│ ├── summarizer.py
│ └── textextractor.py
│
├── main.py # App entry point
├── requirements.txt # Python dependencies
├── test.py # Summarization test script
├── test_quiz.py # Quiz generator test script
├── .gitignore # Files to exclude from Git





## ⚙️ Installation

### 1. Clone the Repository
git clone https://github.com/your-username/book_summarization_project.git
cd book_summarization_project

### 2. Set Up a Virtual Environment
python -m venv venv
# Activate it:
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

### 3. Install Required Packages
pip install -r requirements.txt

### Run the main file 
python main.py
