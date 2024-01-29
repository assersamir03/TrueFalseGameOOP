import question_model
import quiz_brain

questNumber = 0
isRight = True
while questNumber < question_model.lenght and isRight:
    theQuestion = question_model.Question(question_model.theData[questNumber]["text"],
                                          question_model.theData[questNumber]["answer"])
    print(f"{question_model.theData[questNumber]["text"]}")
    userAnswer = input("is it true or false: ").capitalize()
    isRight = quiz_brain.QuestBrain.Checker(question_model.theData[questNumber]["answer"], userAnswer)
    if isRight:
        questNumber += 1
        print("horray you got it right!")

    else:
        print("too bad you did not get it right ")
if questNumber + 1 == question_model.lenght:
    print('you are an expert you got them all !')
else:
    print(f"you got {questNumber} good luck next time !")
