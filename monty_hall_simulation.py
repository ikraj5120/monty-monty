import random

def not_switch():
    doors = [1,2,3]
    choice = random.choice(doors)
    prize = random.choice(doors)
    
    if choice == prize:
        return 1
    else:
        return 0

def switch():
    doors = [1,2,3]
    choice = random.choice(doors)
    prize = random.choice(doors)

    if choice != prize:
        eleminate_doors = [1,2,3]
        eleminate_doors.remove(prize)
        eleminate_doors.remove(choice)
        doors.remove(eleminate_doors[0])
        doors.remove(choice)
        second_choice = doors[0]
        if second_choice == prize:
            return 1
        else:
            return 0
    else:
        eleminate_doors = [1,2,3]
        eleminate_doors.remove(choice)
        doors.remove(random.choice(eleminate_doors))
        doors.remove(choice)
        second_choice = doors[0]
        if second_choice == prize:
            return 1
        else:
            return 0

def simulation():
    trials = 100000
    switch_result = 0
    non_switch_result = 0
    for i in range(trials):
        switch_result += switch()
        non_switch_result += not_switch()
    print("Non Switched wins: ",non_switch_result)
    print("Switched wins: ",switch_result)

if __name__=='__main__':
    simulation()
    
# results
# Non Switched wins:  33346
# Switched wins:  66701
