import pandas as pd
import random

# Read the CSV file
df = pd.read_csv('Data for repository.csv')

def choose_random_name():
    names = df['Movie Name'].tolist()
    random_name = random.choice(names)
    random_name = random_name.replace(" ", "/")  
    return random_name

def display_partial_name(name, guessed_consonants):
    partial_name = ""
    for char in name:
        if char.lower() in guessed_consonants or char.lower() in "aeiou/":
            partial_name += char
        else:
            partial_name += "_"
    return partial_name

def consonant_guess_game():
    name_to_guess = choose_random_name()
    guessed_consonants = set()
    chances = 8

    print("Welcome to the Consonant Guessing Game!")
    print("Try to guess the name with only consonants revealed.")
    print(display_partial_name(name_to_guess, guessed_consonants))

    while chances > 0:
        user_guess = input("\nEnter a consonant: ").lower()

        if len(user_guess) != 1 or not user_guess.isalpha() or user_guess in "aeiou":
            print("Invalid guess. Please enter a single consonant that you haven't guessed before.")
            continue

        if user_guess in guessed_consonants:
            print("You've already guessed that consonant. Try a different one.")
            continue

        guessed_consonants.add(user_guess)
        partial_name_display = display_partial_name(name_to_guess, guessed_consonants)
        print(partial_name_display)

        if "_" not in partial_name_display:
            print("\nCongratulations! You've guessed the name:", name_to_guess)
            break

        if user_guess not in name_to_guess.lower():
            chances -= 1
            print(f"Chances left: {chances}")

    if chances == 0:
        print("\nSorry, you've run out of chances. The correct name was:", name_to_guess)

if __name__ == "__main__":
    consonant_guess_game()


# import pandas as pd
# import random

# # Read the CSV file
# df = pd.read_csv('Data for repository.csv')

# def choose_random_name():
#     names = df['Movie Name'].tolist()
#     random_name = random.choice(names)
#     random_name = random_name.replace(" ", "/")  # Replace space with '/'
#     return random_name

# def display_partial_name(name, guessed_consonants):
#     partial_name = ""
#     for char in name:
#         if char.lower() in guessed_consonants or char.lower() in "aeiou/":
#             partial_name += char
#         else:
#             partial_name += "_"
#     return partial_name


# def consonant_guess_game():
#     name_to_guess = choose_random_name()
#     guessed_consonants = set()
#     chances = 8

#     print("Welcome to the Consonant Guessing Game!")
#     print("Try to guess the name with only consonants revealed.")
#     print(display_partial_name(name_to_guess, guessed_consonants))

#     while chances > 0:
#         user_guess = input("\nEnter a consonant: ").lower()

#         if len(user_guess) == 1 and user_guess.isalpha() and user_guess not in "aeiou" and user_guess not in guessed_consonants:
#             guessed_consonants.add(user_guess)
#             partial_name_display = display_partial_name(name_to_guess, guessed_consonants)
#             print(partial_name_display)
#         elif len(user_guess) == 1 and user_guess.isalpha() and user_guess not in "aeiou" and user_guess in guessed_consonants:
#             guessed_consonants.add(user_guess)
#             partial_name_display = display_partial_name(name_to_guess, guessed_consonants)
#             print(partial_name_display)

#             if "_" not in partial_name_display:
#                 print("\nCongratulations! You've guessed the name:", name_to_guess)
                
#                 break
#         else:
#             print("Invalid guess. Please enter a single consonant that you haven't guessed before.")
#             continue

#         chances -= 1
#         print(f"Chances left: {chances}")

#     if chances == 0:
#         print("\nSorry, you've run out of chances. The correct name was:", name_to_guess)

# if __name__ == "__main__":
#     consonant_guess_game()
