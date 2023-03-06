import random
import time

name = input("Game timer is 30 seconds.\nWhen you enter your name/nickname, the game will start: ").title()
time_limit = 30
start_time = time.time()


def main():
    start_quiz()
    while True:
        user_input = input("Enter 'restart' to restart the game, 'exit' to end:")
        if user_input == "restart":
            restart_game()
        elif user_input == "exit":
            break

def start_quiz():
    print("*************************")
    print("Welcome to the quiz game!")
    print("*************************")
    health = 3
    score = 0
    # Quiz questions and answers
    questions = [
        {"question": "What is the capital of France?",
         "options": ["Paris", "Rome", "Madrid", "London"],
         "answer": "Paris"},
        {"question": "What is the largest ocean in the world?",
         "options": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"],
         "answer": "Pacific Ocean"},
        {"question": "What is the smallest country in the world?",
         "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"],
         "answer": "Vatican City"},
        {"question": "What is the highest mountain in the world?",
         "options": ["K2", "Mount Everest", "Kangchenjunga", "Lhotse"],
         "answer": "Mount Everest"}
    ]

    random.shuffle(questions)

    for i,question in enumerate(questions):
        print(question['question'])
        for j, option in enumerate(question['options']):
            print(f"{j + 1}. {option}")
        try:
            answer = input("Enter the option number:").strip()
            if question['options'][int(answer)-1] == question['answer']:
                print("---------------------------------------------------")
                print("Correct!")
                score += 1
                print("Health:", health)
                display_time_remaining(time_limit, start_time)
                print("---------------------------------------------------")

            else:
                print("---------------------------------------------------")
                print("Incorrect.")
                health -= 1
                print("Health:", health)
                display_time_remaining(time_limit, start_time)
                print("---------------------------------------------------")

            if health == 0:
                print("Game over.")
                break

            if time.time() - start_time >= time_limit:
                print("Time's up!")
                break

        except Exception:
            health -= 1
            if health == 0:
                print("Game over.")
                break

            print("---------------------------------------------------")
            print("Health: ", health)
            print("Incorrect.")
            display_time_remaining(time_limit, start_time)
            print("---------------------------------------------------")
            continue


    global score_points
    if score > 1:
        score_points = f"{score} points,"
    else:
        score_points = f"{score} point,"


    print("***************************************************")
    print("Final Score:", score_points, "Health:", health, )
    display_time_remaining(time_limit, start_time)
    print("***************************************************")
    show_leaderboard()
    print("***************************************************")



def display_time_remaining(time_limit, start_time):
    global time_left_sec
    global g

    elapsed_time = time.time() - start_time
    time_left = time_limit - elapsed_time
    g = time_limit - time_left
    if time_left >= 2:
        time_left_sec = f"{time_left:.0f} seconds."
    else:
        time_left_sec = f"{time_left:.0f} second."

    print(f"Time remaining: {time_left_sec}")



def show_leaderboard():
    num = 0

    with open("leaderboard.txt","a") as f:
        f.write(f"{name},")
        f.write(f" {score_points}")
        f.write(f" {g:.0f} seconds. \n")
    print("Leaderboard:")

    with open("leaderboard.txt","r") as f:
        data = [tuple(line.strip().split()) for line in f]


    sorted_data = sorted(data, key=lambda x: int(x[1],), reverse = True)
    for item in sorted_data:
        num = num + 1
        a = (f"{item[0]} {item[1]} {item[2]} {item[3]} {item[4]}")

        print(f"{num}. {a}")


def restart_game():
    start_quiz()

if __name__ == "__main__":
    main()
