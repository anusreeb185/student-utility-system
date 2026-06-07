while True:

    print("\n===== STUDENT UTILITY SYSTEM =====")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage Calculator")
    print("6. Grade Checker")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("Result:", a + b)

    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("Result:", a - b)

    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("Result:", a * b)

    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if b != 0:
            print("Result:", a / b)

        else:
            print("Cannot divide by zero")

    elif choice == 5:
        marks = float(input("Enter obtained marks: "))
        total = float(input("Enter total marks: "))

        percentage = (marks / total) * 100

        print("Percentage:", percentage)

    elif choice == 6:
        mark = float(input("Enter your mark: "))

        if mark >= 90:
            print("Grade: A+")

        elif mark >= 80:
            print("Grade: A")

        elif mark >= 70:
            print("Grade: B")

        elif mark >= 60:
            print("Grade: C")

        else:
            print("Grade: Fail")

    elif choice == 7:
        print("Thank you for using Student Utility System!")
        break

    else:
        print("Invalid choice")
