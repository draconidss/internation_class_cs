import random




def get_word_bank() -> list:
    user_input = input("please input your word bank, and use space to separate each word: ")
    word_bank = user_input.split()
    return word_bank

def play_game(word_bank):
    word_sequence = random.sample(word_bank, len(word_bank))
    print("Hi! Welcome to Vocab Challenging! Let's see how well you can memorize your words!")
    print("\nPlease remember the following word(s):")
    print(" ".join(word_sequence))
    input("\nPress Enter when you are ready to recall...")
    print("\n" * 50)

    user_input = input("✍️ Please input the words you remembered, and use space to separate each word): ").split()
    user_attempts = []
    for word in user_input:
        user_attempts.append(word.lower())


    i= 0
    while( i % 1 ==i):
        if user_attempts[i] != word_sequence[i]:
            print(f"❌ Nice Try! The correct answer is: {' '.join(word_sequence)}")

    print("✅ Correct! You did a great job!")

word_bank = get_word_bank()
play_game(word_bank)