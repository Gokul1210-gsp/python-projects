def treasure():
    lives = 3
    print("Welcome to the Treasure Island!")
    print("You have 3 lives.Make the right choices!\n")

    # Game steps (data-driven)
    steps = [
        {
            "question": "Left or Right? ",
            "correct": "left",
            "fail_msg": "💀 You fell into a pit!"
        },
        {
            "question": "Swim or Wait? ",
            "correct": "wait",
            "fail_msg": "🐟 Attacked by trout!"
        },
        {
            "question": "Choose a door (Red / Blue / Yellow): ",
            "correct": "yellow",
            "fail_msg": "🚪 Wrong door!"
        }
    ]

    for step in steps:
        while lives > 0:
            choice = input(step["question"]).strip().lower()

            if choice == step["correct"]:
                break
            else:
                lives -= 1
                print(f"{step['fail_msg']} Lives left: {lives}")

        if lives == 0:
            print("Game Over!")
            return

    print("🎉 You found the treasure! You Win!")

treasure()
