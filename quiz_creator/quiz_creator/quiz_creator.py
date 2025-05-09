import os

quiz_questions = []  # List to store questions and answers
possible_answers1 = []
possible_answers2 = []
possible_answers3 = []
possible_answers4 = []
correct_answer = []
question_scores = []


version_number = 1
filename_prefix = "Your Quiz"


def get_filename(version):
    return f"{filename_prefix}{version}.txt"

while True:  # While loop for entering multiple questions
   
   
    save_directory = r"C:\Users\dustin\Music\quiz_creator\answer_the_quiz\answer_the_quiz" 
    os.makedirs(save_directory, exist_ok=True)  # Create folder if it doesn't exist

    filename = os.path.join(save_directory, get_filename(version_number))

    print(f"Current quiz version: {version_number}")

    question = input("Enter your question:")
    quiz_questions.append(question)

    while True:
        try:
            score = float(input("Enter the point value for this question:"))
            question_scores.append(score)
            break
        except ValueError:
            print("Invalid input. Please enter an integer value for the score.")


    # Validate that answers are not the same/duplicate
    while True:
        answer1 = input("Enter your 1st possible answer (a):")
        answer2 = input("Enter your 2nd possible answer (b):")
        answer3 = input("Enter your 3rd possible answer (c):")
        answer4 = input("Enter your 4th possible answer (d):")

        if len({answer1, answer2, answer3, answer4}) == 4:  # Check for unique answers
            possible_answers1.append(answer1)
            possible_answers2.append(answer2)
            possible_answers3.append(answer3)
            possible_answers4.append(answer4)
            break  
        else:
            print("Answers must be unique. Please try again.")

    # Validate the correct answer input
    while True:
        correct = input("Enter the correct answer (must be one of the options):")
        if correct in [answer1, answer2, answer3, answer4]:  # Check if correct answer matches provided answers
            correct_answer.append(correct)
            break
        else:
            print("Correct answer must match one of the provided options. Please try again.")

    # Write the question and answers to a file for this version
    with open(filename, "a") as file:  
        file.write(f"Question: {question}\n")
        file.write(f"Possible Score: {score}\n")
        file.write(f"a. {answer1}\n")
        file.write(f"b. {answer2}\n")
        file.write(f"c. {answer3}\n")
        file.write(f"d. {answer4}\n")
        file.write(f"Correct answer: {correct}\n")
        file.write("\n")  

    decision = input("Do you want to enter another question? Strictly yes/no:")
    if decision.lower() != "yes":
        print(f"Quiz version {version_number} has been saved.")
        
        
        # ask if the user wants to create another version
        create_new_version = input("Do you want to start a new quiz version? (do not enter no if still unsure) strictly yes/no:")
        if create_new_version.lower() == "yes":
            version_number += 1  
            quiz_questions.clear()  # clears the list for the new input of question and answers
            possible_answers1.clear()
            possible_answers2.clear()
            possible_answers3.clear()
            possible_answers4.clear()
            correct_answer.clear()
        else:
            print("Thank you! All quiz data has been saved.")
            break

# Print the quiz questions and answers from the final version
print("\nFinal Quiz:")
for i in range(len(quiz_questions)):
    print(f"{i + 1}. {quiz_questions[i]}")
    print(f"Possible Score:{question_scores[i]}")
    print(f"a. {possible_answers1[i]}")
    print(f"b. {possible_answers2[i]}")
    print(f"c. {possible_answers3[i]}")
    print(f"d. {possible_answers4[i]}")
    print(f"Correct answer: {correct_answer[i]}")
