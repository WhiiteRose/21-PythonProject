questions = {
    "What does CPU stand for? ": "Central Processing Unit",
    "What does GPU stand for? ": "Graphics Processing Unit",
    "What does RAM stand for? ": "Random Access Memory",
    "What does ROM stand for? ": "Read Only Memory",
    "What does SSD stand for? ": "Solid State Drive",
    "What does HDD stand for? ": "Hard Disk Drive",
    "What does OS stand for? ": "Operating System",
    "What does USB stand for? ": "Universal Serial Bus",
    "What does HTTP stand for? ": "HyperText Transfer Protocol",
    "What does IP stand for? ": "Internet Protocol",
}


print("Welcome to my computer quiz!")

playing = input("Do you want to play ? (yes or no) ")

if playing.lower() != "yes":
    quit()

print("Okay ! Let's play :)")
score = 0

for question, answer in questions.items():
    response = input(question)
    if response.lower() == answer.lower():
        print ("Correct !")
        score += 1
    else:
        print('Incorrect !')

print("You got " + str((score / len(questions)) * 100) + "%.")
