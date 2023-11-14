print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What Speices is Thrawn? ")
if answer.lower() == "chiss":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the name of the Mandalorian's ship? ")

if answer.lower() == "razor crest":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("where is the Jedi Temple located? ")

if answer.lower() == "coruscant":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Where was the first Jedi Temple located? ")

if answer.lower() == "tython":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
