import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5  

QUESTIONS = {
    "What is the 2nd tallest Mountain in the world":
        ["K2", "Kilimanjaro", "Denali", "Mt Hood"],
    "What is the least populated state in the US":
        ["Wyoming", "Alaska", "Montana", "Hawaii"],
    "Who is the oldest active player in the NFL":
        ["Tom Brady", "John Elway", "Adam Vinatieri", "Aaron Rodgers"],
    "Who was the youngest President of the United States":
        ["Theodore Roosevelt", "Barack Obama", "Abraham Lincoln", "George W Bush"],

}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

score = 0
for num, (question, answers) in enumerate(questions, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct = answers[0]
    
    labeled_answers = dict(
        zip(ascii_lowercase, random.sample(answers, k=len(answers)))
    )
   
    for label, answer in labeled_answers.items():
        print(f" {label}) {answer}")

    while (answer_label := input("\nChoice? ")) not in labeled_answers:
        print(f"Please answer one of {', '.join(labeled_answers)}")    
    
    answer = labeled_answers[answer_label]
    if answer == correct:
        score += 1
        print(" Correct! ")
        
    else:
        print(f"The correct answer is {correct!r}, not {answer!r} ")

if int(score) == 0:
    print("You got " + str(score) + "/" + str(len(questions)) + " questions correct! Try again")
elif int(score) < 3:
    print("You got " + str(score) + "/" + str(len(questions)) + " questions correct! You did Okay, Study up!")
else:
    print("You got " + str(score) + "/" + str(len(questions)) + " questions correct! Great Job!")            
