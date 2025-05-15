import random

def checkUserSequence(userInput, wordList):
    if len(userInput) != len(wordList):
        return False
    for i in range(len(wordList)):
        if userInput[i] != wordList[i]:
            return False
    return True

def playGame(wordBank):
    sequenceList = []
    round_number = 1
    max_rounds = len(wordBank)

    wordSequence = random.sample(wordBank, max_rounds)

    print("Hi! Welcome to Vocab Challenging! Let's see how well you can memorize your words!")

    while round_number <= max_rounds:
        new_word = wordSequence[round_number - 1]
        sequenceList.append(new_word)

        print(f"\nRound {round_number}: Please remember the following word(s):")
        print(" ".join(sequenceList))

        input("\nPress Enter when you are ready to recall...")
        print("\n" * 50)  

        userAttempts = [word.lower() for word in input("✍️ Please input the words you remembered, and use space to seperate each word): ").split()]

        if checkUserSequence(userAttempts, sequenceList):
            print("✅ Correct! Moving on to the next round...")
            round_number += 1
        else:
            print(f"❌ Nice Try! The correct answer is: {' '.join(sequenceList)}")
            print(f"You completed {round_number - 1} round(s). Better luck next time!")
            break

    if round_number > max_rounds:
        print(f"\n🎉 Congratulations! You completed all {max_rounds} rounds!")

wordBank = ["cerebellum", "cerebral", "talent", "cortex", "personality", "characteristic", "more"]

playGame(wordBank)