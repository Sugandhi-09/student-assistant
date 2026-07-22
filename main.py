
def show_menu():
    print("\n" + "=" * 35)
    print("\t🎓 STUDENT TOOLKIT\t")
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
        print()
        print("\tCALCULATOR\t")
        print("_" * 30)

        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        print()
        if operator in ("+-*/"):
            if operator == "+":
                print("Answer =", num1 + num2)

            elif operator == "-":
                print("Answer =", num1 - num2)

            elif operator == "*":
                print("Answer =", num1 * num2)

            elif operator == "/":
                if num2 != 0:
                    print("Answer =", num1 / num2)
                else:
                    print("Error! Division by zero is not allowed.")

        else:
            print("Invalid operator!")
        print("\nThank you!! You may continue using other features :))")



    elif choice == "2":
        print()
        print("\tPERCENTAGE CALCULATOR\t")
        print("_" * 40)

        subjects = int(input("Enter the number of subjects: "))
        if subjects <= 0:
            print("Number of subjects must be greater than 0.")
        else:
            
            total = 0
            flag = True
            for i in range(subjects):
                marks = float(input(f"Enter marks for Subject {i+1}: "))
                if 100 >= marks >= 0:
                    total += marks
                else :
                    print("Invalid marks! Please enter a value between 0 and 100.")
                    flag = False
                    break
            if flag :
                percentage = total / subjects
                rounded_p = round(percentage,2)

                print("\nTotal Marks =", total)
                print("Percentage =", rounded_p, "%")

            #GRADE CALCULATION
                if rounded_p >= 90 :
                    print("Grade : A+")
                elif rounded_p >= 80 :
                    print("Grade : A")
                elif rounded_p >= 70:
                    print("Grade : B")
                elif rounded_p >= 60:
                    print("Grade : C")
                else:
                    print("Grade : D")
            print("\nThank you!! You may continue using other features :))")



    elif choice == "3":
        print()
        print("\tATTENDANCE CALCULATOR\t")
        print("_" * 40)

        total_classes = int(input("Enter total number of classes: "))
        attended_classes = int(input("Enter number of classes attended: "))

        if total_classes <= 0:
            print("Invalid! Total classes must be greater than 0.")

        elif attended_classes < 0 or attended_classes > total_classes:
            print("Invalid! Attended classes cannot be negative or greater than total classes.")

        else:
            attendance = (attended_classes / total_classes) * 100
            rounded_attendance = round(attendance, 2)

            print("\nAttendance =", rounded_attendance, "%")

            if rounded_attendance >= 75:
                print("Eligible for Exams ✅")
            else:
                print("Not Eligible for Exams ❌")
        print("\nThank you!! You may continue using other features :))")


    elif choice == "4":
        print()
        print("\t CGPA CALCULATOR\t")
        print("_" * 40)

        subjects = int(input("Enter the number of subjects: "))
        if subjects <= 0:
            print("Number of subjects must be greater than 0.")
        else :
            
            total_gpa = 0
            flag = True

            for i in range(subjects):
                gpa = float(input(f"Enter GPA for Subject {i+1}: "))

                if 0 <= gpa <= 10:
                    total_gpa += gpa
                else:
                    print("Invalid GPA! Please enter a value between 0 and 10.")
                    flag = False
                    break

            if flag:
                cgpa = total_gpa / subjects
                rounded_cgpa = round(cgpa, 2)

                print("\nCGPA =", rounded_cgpa)

                if rounded_cgpa >= 9:
                    print("Excellent Performance 🌟")
                elif rounded_cgpa >= 8:
                    print("Very Good 👍")
                elif rounded_cgpa >= 7:
                    print("Good 🙂")
                elif rounded_cgpa >= 6:
                    print("Average")
                else:
                    print("Needs Improvement 📚")
            print("\nThank you!! You may continue using other features :))")


    elif choice == "5":
        print()
        print("\nThank you for using Student Toolkit!")
        print("Have a great day! 👋")
        print("_" * 30)
        break

    else:
        print("Invalid choice! Please try again.")
