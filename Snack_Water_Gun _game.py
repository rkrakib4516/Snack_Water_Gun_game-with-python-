import random


my_list=["s","w","g"]
chances=5
no_out_of_chances=0
Mynumber=0
computer_number=0

print("s for snake \n w for water \n g for gun")
while no_out_of_chances<chances:
    Input=input("Enter s,w,g : ")
    Random=random.choice(my_list)
    if Random==Input:
        print("Both are get 0 point")
    elif Input=="s" and Random=="w":
        computer_number=computer_number+1
        print(f"Your guess is{Input} and computer guess is {Random}\n Computer gain 1 point")
    elif Input=="w" and Random=="g":
        computer_number=computer_number+1
        print(f"Your guess is{Input} and computer guess is {Random}\n Computer gain 1 point")
    elif Input == "w" and Random == "s":
        computer_number = computer_number + 1
        print(f"Your guess is{Input} and computer guess is {Random}\n Computer gain 1 point")
    elif Input=="s" and Random=="g":
        Mynumber=Mynumber+1
        print(f"Your guess is{Input} and computer guess is {Random}\n You gain 1 point")
    elif Input=="w" and Random=="s":
        Mynumber=Mynumber+1
        print(f"Your guess is{Input} and computer guess is {Random}\n You gain 1 point")
    elif Input=="g" and Random=="w":
        Mynumber=Mynumber+1
        print(f"Your guess is{Input} and computer guess is {Random}\n You gain 1 point")
    else:
        print("Your input is wrong")
    no_out_of_chances=no_out_of_chances+1
    print(f"{no_out_of_chances} is left out of {chances}")

print("Game over")

if Mynumber<computer_number:
    print("You are Win")
elif computer_number<Mynumber:
    print("Computer win")