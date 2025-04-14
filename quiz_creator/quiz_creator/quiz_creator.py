quiz_questions = []   #I created a list to store the questions and answers
possible_answers1 = []
possible_answers2 = []
possible_answers3 = []
possible_answers4 = []
correct_answer = []

while True: #While loop, so that the user can enter multiple questions and they can exit after entering the last question they want to enter
    question = input ("Enter your question:")
    quiz_questions.append(question)

    answer1 = input ("Enter your 1st possible answer:")
    possible_answers1.append(answer1)

    answer2 = input ("Enter your 2nd possible answer:")
    possible_answers2.append(answer2)

    answer3 = input ("Enter your 3rd possible answer:")
    possible_answers3.append(answer3)

    answer4 = input ("Enter your 4th possible answer:")
    possible_answers4.append(answer4)

    correct = input ("Enter the correct answer:")
    correct_answer.append(correct);

    decision = input ("Do you want enter another question? (yes/no):")
    if decision != "yes":
        print ("Thank You!!")
        break

 # This for loop, works to print the quiz questions and answers
for i in range(len(quiz_questions)):
    print(f"{i + 1}. {quiz_questions[i]}")
    print(f"a. {possible_answers1[i]}")
    print(f"b. {possible_answers2[i]}")
    print(f"c. {possible_answers3[i]}")
    print(f"d. {possible_answers4[i]}")
    print(f"Correct answer: {correct_answer[i]}")
    