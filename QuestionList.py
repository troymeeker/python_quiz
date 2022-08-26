from calendar import c
from Question import Question
questions_list = [
    "What is the least populated State in the USA?\n (a) Alaska\n (b) Connecticut\n (c) Wyoming\n (d) Iowa \n\n ", 
    "What is the largest animal of all time?\n(a) Blue Whale \n(b) Chinese Giant Salamander \n(c) Giant squid \n(d) Argentinosaurus \n\n", 
    "What was the first state in the United States\n(a) Virginia \n(b) California\n(c) Maryland \n(d) Delaware\n\n "
  
]

questions = [
    Question(questions_list[0], "c"),
    Question(questions_list[1], "a"),
    Question(questions_list[2], "d")

]

def run_test(questions):
    score = 0
    for q in questions:
        answer = input(q.question)
        if answer == q.answer:
            score +=1 

        print("you got " + str(score) + "/" + str(len(questions)) + " questions correct!")            


run_test(questions)