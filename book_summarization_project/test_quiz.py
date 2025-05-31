from modules.quiz_generator import QuizGenerator

sample_context = """
Photosynthesis is a process used by plants and other organisms to convert light energy
into chemical energy that can later be released to fuel the organisms' activities.
This process takes place in the chloroplasts and produces oxygen as a byproduct.
"""

def test_generate_quiz():
    print("⏳ Generating quiz from context...")
    generator = QuizGenerator()
    result = generator.generate_quiz(sample_context, num_questions=5)

    quiz = result.get("quiz", [])
    if not quiz:
        print("❌ No quiz generated.")
        return

    print("✅ Quiz generated:\n")
    for i, item in enumerate(quiz, 1):
        print(f"Q{i}: {item['question']}")
        for option in item['options']:
            print(f"  {option}")
        print(f"✔ Answer: {item['answer']}\n")

if __name__ == "__main__":
    test_generate_quiz()
