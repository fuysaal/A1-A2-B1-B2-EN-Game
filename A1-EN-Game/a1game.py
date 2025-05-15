import random
import os
from time import sleep


def colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

sleep(2)
print("\nWelcome to the path of learning English")
sleep(2)
print("This program aims to memorize simple words at A1 level with daily repetition.")
sleep(3)
print("If there is a word you don't know, you can search for it, and if you don't want to see the words you know anymore, you can remove them from the list. You can continue to review the words you just learned in the future.")
sleep(4)
print("Each word you remove from the list is worth a new word, once the list is complete you can move on to the others. A2")
sleep(2)
print("If you are ready, let's start")
input(colored("\nPress Enter to start the program...",32))
sleep(0.5)


def load_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.readlines()

        return [word.strip() for word in words if word.strip()]
    except FileNotFoundError:
        print(f"Error: '{filename}' file is not exists")
        return []


def save_words(filename, words):
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + "\n")


def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')


def show_random_word():
    words = load_words('A1.txt')
    if not words:
        print("file not upload.")
        return

    while True:
        clear_screen()
        random_word = random.choice(words)
        print(f"\n{colored('Random Word:', 33)} {colored(random_word, 35)}")
        print(colored("If you don't know, research it. Don't be lazy.",31))
        print(colored("\n1. Continue",32))
        print(colored("2. Remove",32))
        print(colored("3. Exit",32))


        choice = input("Please enter your choice (e.g 1,2,3)==> ")

        if choice == "1":
            continue
        elif choice == "2":
            words.remove(random_word)
            save_words('A1.txt', words)  # Dosyayı güncelle
            print(f"{random_word} has been removed from the list.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please choose 1, 2, or 3.")

if __name__ == "__main__":
    show_random_word()
