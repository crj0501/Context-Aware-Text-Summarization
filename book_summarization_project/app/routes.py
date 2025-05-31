# routes.py
import os
from flask import request, render_template, redirect, url_for, session
from werkzeug.utils import secure_filename
from modules.textextractor import TextExtractor
from modules.preprocessor import clean_text
from modules.summarizer import generate_summary
from modules.keyword_extractor import extract_keywords
from modules.retrieval_qa import RetrievalQA
from modules.gemini_api import GeminiClient
from modules.quiz_generator import QuizGenerator  

qa_engine = None           # RAG engine instance
global_context = {}        # Avoid storing huge text in session

def initialize_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        global qa_engine

        if request.method == 'POST':
            uploaded_file = request.files.get('pdf_file')
            if uploaded_file and uploaded_file.filename.endswith('.pdf'):
                filename = secure_filename(uploaded_file.filename)
                pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                uploaded_file.save(pdf_path)

                # Step 1: Extract and clean text
                raw_text = TextExtractor().extract_text(pdf_path)
                cleaned_text = clean_text(raw_text)
                global_context['context'] = cleaned_text  # Store in RAM not session

                # Step 2: Generate summary and keywords
                summary = generate_summary(cleaned_text)
                keywords = extract_keywords(cleaned_text)

                # Step 3: Save small results to session (safe)
                session['summary'] = summary
                session['keywords'] = keywords

                # Step 4: Initialize RAG engine
                qa_engine = RetrievalQA(cleaned_text)

                return redirect(url_for('chatbot'))

        return render_template('index.html')

    @app.route('/chatbot', methods=['GET', 'POST'])
    def chatbot():
        global qa_engine

        summary = session.get('summary')
        keywords = session.get('keywords')
        context = global_context.get('context')
        response = ""

        if request.method == 'POST':
            user_question = request.form.get('user_question')
            if user_question and context:
                retrieved_context = qa_engine.get_relevant_chunks(user_question)
                gemini = GeminiClient()
                response = gemini.answer_question(user_question, retrieved_context)

        return render_template(
            'index.html',
            summary=summary,
            keywords=keywords,
            response=response
        )
    @app.route('/generate_quiz', methods=['POST'])
    def generate_quiz():
        # Get the summary from session or global context
        summary = session.get('summary') or global_context.get('context')
        
        # Make sure summary is available
        if not summary:
            return "Summary is missing!", 400  # Handle the case where summary is missing
        
        # Create QuizGenerator instance, passing the summary and number of questions
        quiz_generator = QuizGenerator(summary=summary, num_questions=5)  # Pass the required summary
        quiz = quiz_generator.generate_quiz()

        # Get other session data like keywords
        keywords = session.get('keywords')

        # Return the generated quiz and other details to the template
        return render_template(
            'index.html',
            summary=summary,
            keywords=keywords,
            quiz=quiz
        )

