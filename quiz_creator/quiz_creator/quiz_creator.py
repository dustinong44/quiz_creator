import os

quiz_questions = []  
possible_answers1 = []
possible_answers2 = []
possible_answers3 = []
possible_answers4 = []
correct_answer = []
question_scores = []

filename_prefix = "Your Quiz"
save_directory = r"C:\Users\dustin\Music\quiz_creator\answer_the_quiz\answer_the_quiz"
os.makedirs(save_directory, exist_ok=True)  


def get_filename(version):
    return os.path.join(save_directory, f"{filename_prefix}{version}.txt")


existing_files = [f for f in os.listdir(save_directory) if f.startswith(filename_prefix)]
version_number = len(existing_files) + 1  
filename = get_filename(version_number)  

while True:  
    print(f"Current quiz version: {version_number}")

    question = input("Enter your question: ")
    quiz_questions.append(question)

    while True:
        try:
            score = float(input("Enter the point value for this question: "))
            question_scores.append(score)
            break
        except ValueError:
            print("Invalid input. Please enter an integer value for the score.")

    
    while True:
        answer1 = input("Enter your 1st possible answer (a): ")
        answer2 = input("Enter your 2nd possible answer (b): ")
        answer3 = input("Enter your 3rd possible answer (c): ")
        answer4 = input("Enter your 4th possible answer (d): ")

        if len({answer1, answer2, answer3, answer4}) == 4:  
            possible_answers1.append(answer1)
            possible_answers2.append(answer2)
            possible_answers3.append(answer3)
            possible_answers4.append(answer4)
            break  
        else:
            print("Answers must be unique. Please try again.")

    while True:
        correct = input("Enter the correct answer (must be one of the options): ")
        if correct in [answer1, answer2, answer3, answer4]:  
            correct_answer.append(correct)  
            break
        else:
            print("Correct answer must match one of the provided options. Please try again.")

    
    with open(filename, "a") as file:  
        file.write(f"Question: {question}\n")
        file.write(f"Possible Score: {score}\n")
        file.write(f"a. {answer1}\n")
        file.write(f"b. {answer2}\n")
        file.write(f"c. {answer3}\n")
        file.write(f"d. {answer4}\n")
        file.write(f"Correct answer: {correct}\n")
        file.write("\n")  

    decision = input("Do you want to enter another question? Strictly yes/no: ")
    if decision.lower() != "yes":
        print(f"Quiz version {version_number} has been saved.")

        
        create_new_version = input("Do you want to start a new quiz version? Strictly yes/no: ")
        if create_new_version.lower() == "yes":
            version_number += 1  
            filename = get_filename(version_number)  

            
            quiz_questions.clear()
            possible_answers1.clear()
            possible_answers2.clear()
            possible_answers3.clear()
            possible_answers4.clear()
            correct_answer.clear()
            question_scores.clear()
        else:
            print("Thank you! All quiz data has been saved.")
            break


min_length = min(len(quiz_questions), len(question_scores), len(possible_answers1), 
                 len(possible_answers2), len(possible_answers3), len(possible_answers4), len(correct_answer))

print("\nFinal Quiz:")
for i in range(min_length):  
    print(f"{i + 1}. {quiz_questions[i]}")
    print(f"Possible Score: {question_scores[i]}")
    print(f"a. {possible_answers1[i]}")
    print(f"b. {possible_answers2[i]}")
    print(f"c. {possible_answers3[i]}")
    print(f"d. {possible_answers4[i]}")
    print(f"Correct answer: {correct_answer[i]}")