quiz_questions = []
possible_answers1 = []
possible_answers2 = []
possible_answers3 = []
possible_answers4 = []
correct_answer = []

while True:
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

    