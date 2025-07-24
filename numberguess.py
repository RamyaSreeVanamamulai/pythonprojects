import random
number_guess = random.randint(1,100)
while True:
    try:
        guess = int(input('Guess the number 1 to 100:'))
        if guess > number_guess:
            print("Too high")
        elif guess < number_guess:
            print("Too low")
        else:
            print("congratulations")
            break
    except ValueError:
        print("enter a valid number")
    

output:
Guess the number 1 to 100: 50
Too low
Guess the number 1 to 100: 80
Too high
Guess the number 1 to 100: abc
enter a valid number
Guess the number 1 to 100: 70
congratulations
