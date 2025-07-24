import random
playing = True
while playing:
    choice = input('roll the dies(y/n):').lower()
    if choice == 'y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'{die1},{die2}')
    elif choice == 'n':
        print("Thank you for playing!")
        break
else:
    print("Invalid choice!")


output :
roll the dies(y/n): y
4, 2
roll the dies(y/n): y
6, 1
roll the dies(y/n): x
Invalid choice!
roll the dies(y/n): n
Thank you for playing!
