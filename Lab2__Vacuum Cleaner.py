def vacuum_simulation():
    cost = 0
    
    # Get initial states and location
    state_A = int(input("Enter state of A (0 for clean, 1 for dirty): "))
    state_B = int(input("Enter state of B (0 for clean, 1 for dirty): "))
    location = input("Enter location (A or B): ").upper()

    # Vacuum operation loop
    while True:
        if location == 'A':
            if state_A == 1:
                print("Cleaning A.")
                state_A = 0
                cost += 1
            elif state_B == 1:
                print("Moving vacuum right")
                location = 'B'
                cost += 1
            else:
                print("Turning vacuum off")
                break
                
        elif location == 'B':
            if state_B == 1:
                print("Cleaning B.")
                state_B = 0
                cost += 1
            elif state_A == 1:
                print("Moving vacuum left")
                location = 'A'
                cost += 1
            else:
                print("Turning vacuum off")
                break

    print(f"Cost: {cost}")
    print(f"{{'A': {state_A}, 'B': {state_B}}}")
    print("1BM23CS341")

vacuum_simulation()

OUTPUT

Enter state of A (0 for clean, 1 for dirty): 1
Enter state of B (0 for clean, 1 for dirty): 1
Enter location (A or B): A
Cleaning A.
Moving vacuum right
Cleaning B.
Turning vacuum off
Cost: 3
{'A': 0, 'B': 0}
1BM23CS341


Enter state of A (0 for clean, 1 for dirty): 1
Enter state of B (0 for clean, 1 for dirty): 0
Enter location (A or B): A
Cleaning A.
Turning vacuum off
Cost: 1
{'A': 0, 'B': 0}
1BM23CS341

Enter state of A (0 for clean, 1 for dirty): 0
Enter state of B (0 for clean, 1 for dirty): 1
Enter location (A or B): A
Moving vacuum right
Cleaning B.
Turning vacuum off
Cost: 2
{'A': 0, 'B': 0}
1BM23CS341


Enter state of A (0 for clean, 1 for dirty): 0
Enter state of B (0 for clean, 1 for dirty): 1
Enter location (A or B): B
Cleaning B.
Turning vacuum off
Cost: 1
{'A': 0, 'B': 0}
1BM23CS341

Enter state of A (0 for clean, 1 for dirty): 0
Enter state of B (0 for clean, 1 for dirty): 0
Enter location (A or B): A
Turning vacuum off
Cost: 0
{'A': 0, 'B': 0}
1BM23CS341
