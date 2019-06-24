import random

# initialize
doors = [1,2,3]
prize = random.choice(doors)
user_choice = int(input("Enter your choice (1,2,3): "))

# If you have chose door 1, and Car is also behind door 1.
if user_choice==prize:
    doors.remove(user_choice)
    # Open any of the other two doors, both will have goat behind them.
    door_open = random.choice(doors)
    print(f"\nBehind door {door_open} is a Goat....")
    switch = input("\nDo you want to switch (y/n): ")
    if switch == 'y':
        doors.remove(door_open)
        # Since you had chosen the correct door and you decided to switch, So you loose.
        remaining = doors[0]
        print(f"\nBehind door {remaining} is a Goat....")
        print("\nOops! You have lost. Try again....")
    else:
        # If you dont switch , well you had selected the correct door in the first place. 
        print(f"\nBehind door {user_choice} is a Car....")
        print("\nCongratulations! You have won...")

# If you have chose door 1, and Car is also behind door 2.
else:
    doors.remove(user_choice)
    # You have chosen door 1. Monty will never open the door 2 behind which Car is, where is the fun in that.
    doors.remove(prize)
    # Only remaining choice is door 3.
    door_open = doors[0]
    print(f"\nBehind door {door_open} is a Goat....")
    switch = input("\nDo you want to switch (y/n): ")
    if switch == 'y':
        # Since you had chosen the incorrect door 1 and you have seen whats behind door 3. 
        # you decided to switch to door 2,and you won.
        print(f"\nBehind door {prize} is a Car..")
        print("\nCongratulations! You have won...")
    else:
        # If you dont switch , well you had selected the incorrect door in the first place. 
        print(f"Behind door {user_choice} is a Goat....")
        print("\nOops! You have lost. Try again....")
