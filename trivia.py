import random
import json


def shuffle_in_place(original_list):
    for i in range(len(original_list)-1, 0, -1):
        pos = random.randint(0, i)
        original_list[i], original_list[pos] = original_list[pos], original_list[i]


def ask_question(question, choices, ans):
    options = choices
    options.append(ans)
    shuffle_in_place(options)
    print(question)
    for i in range(len(options)):
        print(options[i])
    choice = input("\nPlease input your answer: ")
    if choice == ans:
        print("Correct!\n")
        return 10
    else:
        print("Wrong! The right answer is", ans, "\n")
        return -5


def play_trivia():
    print("Let's Play A Round of Trivia!\n")
    score = 0
    with open('Apprentice_TandemFor400_Data.json') as f:
        data = json.load(f)
    shuffle_in_place(data)
    for i in range(10):
        points = ask_question(data[i]['question'], data[i]['incorrect'], data[i]['correct'])
        score += points
    print("Your final score was:", score)


def main():
    play = True
    play_trivia()
    while play:
        cont = input("Play again (Y/N)? ")
        print("")
        if cont == 'Y':
            play_trivia()
        elif cont == 'N':
            print("Take care. Goodbye!")
            play = False


main()
