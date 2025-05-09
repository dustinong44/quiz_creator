import random

def load_quiz(filename):
    quiz_data = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            question_data = {}
            for line in lines:
                if line.startswith("Question:"):
                    question_data = {"question": line.strip("Question: ").strip(), "answers": [], "correct": None}
                elif line.startswith(("a.", "b.", "c.", "d.")):
                    question_data["answers"].append(line.strip())
                elif line.startswith("Correct answer:"):
                    question_data["correct"] = line.strip("Correct answer: ").strip()
                    quiz_data.append(question_data)  
        return quiz_data
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

quiz_file = "Your Quiz1.txt"  
quiz_questions = load_quiz(quiz_file)
print(quiz_questions)  

def get_random_question(quiz_data):
    if not quiz_data:
        print("No questions available.")
        return None
    return random.choice(quiz_data)


selected_question = get_random_question(quiz_questions)
if selected_question:
    print(f"Question: {selected_question['question']}")
    for answer in selected_question["answers"]:
        print(answer)  