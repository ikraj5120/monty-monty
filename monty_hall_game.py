import random
doors = [1,2,3]
prize = random.choice(doors)
print(prize)
user_choice = int(input("Enter your choice (1,2,3): "))
if user_choice==prize:
    doors.remove(user_choice)
    door_open = random.choice(doors)
    print(f"\nBehind door {door_open} is a Goat....")
    switch = input("\nDo you want to switch (y/n): ")
    if switch == 'y':
        doors.remove(door_open)
        remaining = doors[0]
        print(f"\nBehind door {remaining} is a Goat....")
        print("\nOops! You have lost. Try again....")
    else:
        print(f"\nBehind door {user_choice} is a Car....")
        print("\nCongratulations! You have won...")
else:
    doors.remove(user_choice)
    doors.remove(prize)
    door_open = doors[0]
    print(f"\nBehind door {door_open} is a Goat....")
    switch = input("\nDo you want to switch (y/n): ")
    if switch == 'y':
        print(f"\nBehind door {prize} is a Car..")
        print("\nCongratulations! You have won...")
    else:
        print(f"Behind door {user_choice} is a Goat....")
        print("\nOops! You have lost. Try again....")
