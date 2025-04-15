quiz_questions = []  # List to store questions and answers
possible_answers1 = []
possible_answers2 = []
possible_answers3 = []
possible_answers4 = []
correct_answer = []

while True:  # While loop for entering multiple questions
    question = input("Enter your question:")
    quiz_questions.append(question)

    # Checking for answers if not duplicate
    while True:
        answer1 = input("Enter your 1st possible answer:")
        answer2 = input("Enter your 2nd possible answer:")
        answer3 = input("Enter your 3rd possible answer:")
        answer4 = input("Enter your 4th possible answer:")
        
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
        correct = input("Enter the correct answer:")
        if correct in [answer1, answer2, answer3, answer4]:  # Check if correct answer matches provided input possible answers by the user
            correct_answer.append(correct)
            break  
        else:
            print("Correct answer must match one of the provided options. Please try again.")

    decision = input("Do you want to enter another question? (yes/no):")
    if decision.lower() != "yes":
        print("Thank You!!")
        break

# Print the quiz questions and answers
for i in range(len(quiz_questions)):
    print(f"{i + 1}. {quiz_questions[i]}")
    print(f"a. {possible_answers1[i]}")
    print(f"b. {possible_answers2[i]}")
    print(f"c. {possible_answers3[i]}")
    print(f"d. {possible_answers4[i]}")
    print(f"Correct answer: {correct_answer[i]}")