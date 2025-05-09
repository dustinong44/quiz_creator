import os
import random

# dito po makikita yung folder ng quiz 
quiz_directory = r"C:\Users\dustin\Music\quiz_creator\answer_the_quiz\answer_the_quiz"
filename_prefix = "Your Quiz"

# find the latest quiz file
def get_latest_quiz_file():
    existing_files = [f for f in os.listdir(quiz_directory) if f.startswith(filename_prefix) and f.endswith(".txt")]
    if not existing_files:
        return None  # No quiz files found
    latest_file = sorted(existing_files, key=lambda x: int(x.replace(filename_prefix, "").replace(".txt", "")), reverse=True)[0]
    return os.path.join(quiz_directory, latest_file) 

# load quiz data from file
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

def ask_question(question_data):
    print(f"\nQuestion: {question_data['question']}")
    for answer in question_data["answers"]:
        print(answer)

    while True:
        user_answer = input("Your answer (enter a, b, c, or d): ").strip().lower()
        if user_answer in ["a", "b", "c", "d"]:
            return user_answer
        else:
            print("Invalid input. Please enter a, b, c, or d.")

def check_answer(user_answer, question_data):
    correct_text = question_data["correct"]
    correct_letter = None

    # finds the correct letter from (a, b, c, d) by matching the full answer text
    for answer in question_data["answers"]:
        if correct_text == answer[3:].strip(): 
            correct_letter = answer[0]  
            break

    if user_answer == correct_letter:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer was {correct_letter}: {correct_text}")
        return False

def run_quiz(quiz_data):
    if not quiz_data:
        print("Error: No quiz data available.")
        return
    
    score = 0
    total_questions = len(quiz_data)

    random.shuffle(quiz_data)  # Shuffle questions before starting

    for question_data in quiz_data:  
        user_answer = ask_question(question_data)
        if check_answer(user_answer, question_data):
            score += 1

    print(f"\nQuiz Complete! Your final score: {score}/{total_questions}")

# Find the latest quiz file 
latest_quiz_file = get_latest_quiz_file()

if latest_quiz_file:
    print(f"Loading quiz from: {latest_quiz_file}")
    quiz_questions = load_quiz(latest_quiz_file)
    run_quiz(quiz_questions)
else:
    print("Error: No valid quiz files found.")