print("Welcome to the Quiz!")

play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()

print("Lets's start!")
score = 0

answer = input("CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("GPU stands for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("GUI stands for? ")
if answer.lower() == "graphic user interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("LCD stands for? ")
if answer.lower() == "liquid crystal display":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("LED stands for? ")
if answer.lower() == "light emiting diode":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("LAN stands for? ")
if answer.lower() == "local area network":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your " + str(score) + " answers correct!")
print("You scored " + str((score/8)*100) + "%.")