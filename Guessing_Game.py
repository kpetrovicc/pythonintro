secret_word = "giraffe"
guess = ""
max_guess_count = 3
guess_count = 0
flag = False

while (guess != secret_word) and guess_count < max_guess_count and flag == False:
    guess = input("Enter guess: ")
    if guess == secret_word:
        print("You win!")
        flag = True
    else:
        guess_count += 1
        print("You have " + str(max_guess_count - guess_count) + " guesses left.")

if guess_count >= max_guess_count:
    print("You lose!")
