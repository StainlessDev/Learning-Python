import random

# Generate a random number between 1 and 10

# Ask the user to guess the number and store it in a variable

# Compare the guess to the secret number

# Print the result

random_number = random.randint(1, 10)

print("Welcome to the number guessing game!")
guess = input("Guess a number between 1 and 10: ")

tries = 1

while tries <= 3:
    
    if guess.isdigit() == False:
        print("That's not a number!")
        guess = input("Guess a number between 1 and 10: ")
        continue
    else:

        if guess == random_number:
            print("You win!")
            quit()
        else:
            print("You lose!")
            print("The number was " + str(random_number) + ".")
            tries += 1
            break
            

if tries == 3:
    print("You lose!")
    print("The number was " + str(random_number) + ".")
    quit()