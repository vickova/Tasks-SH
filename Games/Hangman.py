import random

name = input("What is your name: ")
print("Best of luck playing hangman ", name)

with open('hangmantxt.md', 'r') as reader:
    t = (reader.read()).split()
# Open a file containing 30 words.
computer = random.choice(t)
print(computer)
# Randomly choose a word from the words and assign it for computer
print("Guess this word: ")
for i in range(len(computer)):
    print("_", end=" ")

trycount = 0
while trycount < 10:
    # A while loop true when trycount is less than attempt time
    player = input("\n\nEnter a letter to guess or a word if you are sure: ")
    player = player.lower()  # to convert to lower case
    for char in computer:
        if char in player:
            print(char)
        else:
            print("\n_")

    if len(player) == 1:
        if player in computer:
            print("Congrats!", player, "is in the word. Try more")
            trycount = trycount + 1
            print("You have", (10 - trycount), "more attempt")
        else:
            print(player, "not in the word. Try more")
            trycount = trycount + 1
            print("You have", (10 - trycount), "more attempt")
    elif len(player) > 1:
        if player == computer:
            print("Correct!", player, "matches computers", computer, "You win")
            break
        else:
            print(player, "did not match the word chosen. Try again!")
            trycount = trycount + 1
            print("You have", (10 - trycount), "more attempt")
    if trycount == 10:
        print("You lose!!")
        break
print("The word is: ", computer)
