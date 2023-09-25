import random

number_range = input("pick a number foo: ")

if number_range.isdigit():
    number_range = int(number_range)

    if number_range <= 0:
        print("Ha ha get wasted. You should pick a number larger than 0 next time.")
        quit()
else:
    print("Bro... you dumb or stupid? I said pick a number.")
    quit()

random_number = random.randint(0, number_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess what the number might be: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Like I said before, pick a number.")
        continue

    if user_guess == random_number:
        print("I swear bro you're cheating. You got it right.")
        break
    elif user_guess > random_number:
        print("You're a little too high.")
    else:
        print("Here's a little flashback, only up!")

print("It took you", guesses, "guesses. SMH could've been better.")