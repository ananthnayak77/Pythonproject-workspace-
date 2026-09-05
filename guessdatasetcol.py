import random
columns=["age", "height", "weight", "gender", "income"]
word = random.choice(columns)
guessed=set()
attempts=8
while attempts>0:
    guess=input("Guess a column name: ")
    if guess in guessed:
        print("You already guessed that column.")
    elif guess==word:
        print("Congratulations! You guessed the correct column:", word)
        break
    else:
        print("Incorrect guess. Try again.")
        guessed.add(guess)
        attempts -= 1
        print(f"You have {attempts} attempts left.")