from string import ascii_lowercase

questions = {
    "What is the 2nd tallest Mountain in the world":
        ["K2", "Kilimanjaro", "Denali", "Mt Hood"],
    "What is the least populated state in the US":
        ["Wyoming", "Alaska", "Montana", "Hawaii"],
    "Who is the oldest active player in the NFL":
        ["Tom Brady", "John Elway", "Joe Burrow", "Adam Vinatieri", "Aaron Rodgers"],
    "Who was the youngest President of the United States":
        ["Theodore Roosevelt", "Barack Obama", "Abraham Lincoln", "George W Bush"],

}

score = 0
for num, (question, answers) in enumerate(questions.items(), start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    correct = answers[0]
    
    labeled_answers = dict(zip(ascii_lowercase, sorted(answers)))
    # sorted_answers = sorted(answers)
    for label, answer in labeled_answers.items():
        print(f" {label}) {answer}")

    answer_label = input("\nChoice? ")
    answer = labeled_answers.get(answer_label)
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
