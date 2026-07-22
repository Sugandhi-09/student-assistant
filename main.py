def show_menu():
    print("\n" + "=" * 35)
    print("🎓 SMART STUDENT ASSISTANT")
    print("=" * 35)
    print("1. Calculator")
    print("2. Percentage Calculator")
    print("3. Attendance Calculator")
    print("4. CGPA Calculator")
    print("5. Exit")
    print("=" * 35)


while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Calculator coming soon...")

    elif choice == "2":
        print("Percentage Calculator coming soon...")

    elif choice == "3":
        print("Attendance Calculator coming soon...")

    elif choice == "4":
        print("CGPA Calculator coming soon...")

    elif choice == "5":
        print("Thank you for using Smart Student Assistant!")
        break

    else:
        print("Invalid choice! Please try again.")
