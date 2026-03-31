while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        rows = int(input("\nEnter number of rows: "))

        if rows <= 0:
            print("Invalid input!")
            break

        print()
        for i in range(1, rows + 1):   # to match your pattern style
            for j in range(i):
                print("*", end="")
            print()

    # -------- NUMBER ANALYZER --------
    elif choice == 2:
        start = int(input("\nEnter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        total = 0
        print()

        for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")

            total += num

        print(f"\nSum of all numbers from {start} to {end} is: {total}")

    # -------- EXIT --------
    elif choice == 3:
        print("\nExiting the program. Goodbye!")
        break

    else:
        print("\nInvalid choice! Please try again.")