import gk
import random

print("Welcome to the Quiz Game")

playing = input("Do you want to play ?\n-->Type Yes or No: ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play...")

score = 0
x = 1

while True:
    random_question = random.choice(gk.gk_questions)
    print(f"Question {x}: " + random_question["question"])

    user_answer = input("Write your answer: ")

    if user_answer.lower() == random_question["answer"].lower():
        score += 1
        print("Well Done! Correct Answer!")
    else:
        print("Ohh! Wrong Answer!")
        print("Correct Answer is " + random_question["answer"])

    print("Your Score: " + str(score))

    if user_answer == "":
        print("Game Ended!")
        break

    x += 1

