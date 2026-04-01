# 1. The Global Data (Your Dictionary)
student_database = {"vishnu": "absent", "gojo": "absent", "luffy": "absent"}

# 2. The Main Loop (Keeps the app running)
while True:
    print("""
======= 🏫 SMART ATTENDANCE SYSTEM =======
1. MARK STUDENT AS PRESENT
2. VIEW ATTENDANCE
3. EXIT
==========================================
""")
    
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        # Convert input to lowercase to match your dictionary keys perfectly
        name_in_database = input("Enter student name: ").lower()
        
        # The instant dictionary lookup
        if name_in_database in student_database:
            student_database[name_in_database] = "present"
            print(f"✅ Success: {name_in_database.capitalize()} has been marked as PRESENT!")
        else:
            print(f"❌ Error: Student '{name_in_database}' not found in the class registry.")

    elif choice == '2':
        print("\n=== CURRENT ATTENDANCE LOG ===")
        # .items() lets us grab both the key (student) and value (status) at the same time
        for student, status in student_database.items():
            print(f"- {student.capitalize()}: {status.capitalize()}")
        print("==============================")

    elif choice == '3':
        print("Saving data... Exiting system. Goodbye! 👋")
        break # This instantly kills the while loop

    else:
        print("❌ Invalid input! Please type 1, 2, or 3.")