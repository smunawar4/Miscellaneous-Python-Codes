import random, sys

print('Heads or Tails Program.')
choice = input('Please enter Heads or Tails: ')
user_choice = 0
flag = True
if choice == 'Heads':
    user_choice = 1
elif choice == 'Tails':
    user_choice = 2

while flag:
    computer_choice = random.randint(1,2)
    if computer_choice == 1:
        print("Heads!")
        if user_choice == computer_choice:
            print('Congrats you won the coin flip!')
        else:
            print('Better Luck next time!')
        flag = False

    if computer_choice == 2:
        print("Tails!")
        if user_choice == computer_choice:
            print('Congrats you won the coin flip!')
        else:
            print('Better Luck next time!')
        flag = False
