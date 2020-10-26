import random
import json


# Used to randomize order of questions AND order of choices
def shuffle_in_place(original_list):
    for i in range(len(original_list)-1, 0, -1):
        pos = random.randint(0, i)
        original_list[i], original_list[pos] = original_list[pos], original_list[i]


# Prints the question and it's choices and takes in user input to check against answer
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


# Takes in filename of file with JSON data, parses it, and returns data
def parse_json(filename):
    with open(filename) as f:
        data = json.load(f)
    return data


# Plays one round of trivia and keeps track of round score
def play_trivia():
    print("Let's Play A Round of Trivia!\n")
    score = 0
    data = parse_json('Apprentice_TandemFor400_Data.json')
    shuffle_in_place(data)
    for i in range(10):
        points = ask_question(data[i]['question'], data[i]['incorrect'], data[i]['correct'])
        score += points
    print("Your final score was:", score)


# Begins one round of trivia and gives user ability to keep playing rounds
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
