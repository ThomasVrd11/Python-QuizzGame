# Quizz

questions = (
    "In which video game do players explore the fictional post-apocalyptic United States in the character of Joel and Ellie?",
    "What is the name of the main protagonist in the video game series 'The Legend of Zelda'?",
    "Which game is known for the iconic phrase 'War... War never changes'?",
    "Which of these games is famous for introducing the concept of 'battle royale?",
    "'Overwatch' is a team-based multiplayer first-person shooter developed and published by which company?")

options = (("A. Fallout 4", "B. Metro Exodus", "C. The Last of Us", "D. Borderlands"),
        ("A. Mario", "B. Link", "C. Ganon", "D. Zelda"),
        ("A. Halo", "B. Fallout", "C. Battlefield", "D. Medal of Honor"),
        ("A. Fortnite", "B. PUBG", "C. Apex Legends", "D. Minecraft Hunger Games"),
        ("A. Valve", "B. Epic Games", "C. Blizzard", "D. Ubisoft"))

answers = ("C", "B", "B", "B", "C")
guesses = []
score = 0
questionNumber = 0

for question in questions:
    print("------------Kouiz-------------")
    print(question)
    for option in options[questionNumber]:
        print(option)

    guess = input("Enter your answer: (A, B, C, D) ").upper()
    guesses.append(guess)
    if guess == answers[questionNumber]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is {answers[questionNumber]}")
    print(f"Your current score is {score}/{questionNumber + 1}")
    questionNumber += 1
print()
print("-------------------------")
print("Thank you for playing!")
print(f"Your final score is {score}/{questionNumber}")
score = (score / questionNumber) * 100
print(f"Your final score is {score}%")
print("-------------------------")

