'''
Name: Md Furkan Khan
Enrollment: 0157AL231123
Batch: 5
Batch Time: 10:30 - 12:10
'''

students = {}
logged_user = ''
logged = False

def register():
    global students
    username = input("Enter username: ")
    if username in students:
        print("Username already exists.")
        main()
        return
    password = input("Enter password: ")
    name = input("Enter full name: ")
    roll_no = input("Enter roll number: ")
    branch = input("Enter branch: ")
    year = input("Enter year: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    address = input("Enter address: ")
    dob = input("Enter date of birth: ")
    gender = input("Enter gender: ")
    students[username] = {
        'password': password,
        'name': name,
        'roll_no': roll_no,
        'branch': branch,
        'year': year,
        'email': email,
        'phone': phone,
        'address': address,
        'dob': dob,
        'gender': gender
    }
    print("Registration successful.")
    main()

def login():
    global logged_user, logged
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in students and students[username]['password'] == password:
        logged_user = username
        logged = True
        print("Login successful.")
    else:
        print("Invalid username or password.")
    main()

def show_profile():
    global logged_user, logged
    if not logged:
        print("Please login first.")
    else:
        user = students[logged_user]
        print("\nStudent Profile")
        for k, v in user.items():
            if k != 'password':
                print(f"{k.capitalize()}: {v}")
    main()

def update_profile():
    global logged_user, logged
    if not logged:
        print("Please login first.")
    else:
        user = students[logged_user]
        print("Enter new details (leave blank to keep current):")
        for field in user:
            if field != 'password':
                new_val = input(f"{field.capitalize()} ({user[field]}): ")
                if new_val.strip():
                    user[field] = new_val
        students[logged_user] = user
        print("Profile updated successfully.")
    main()

def logout():
    global logged_user, logged
    if logged:
        logged_user = ''
        logged = False
        print("Logged out successfully.")
    else:
        print("No user logged in.")
    main()

def terminate():
    exit()

def main():
    print("\nWelcome to LNCT")
    response = input('''
        Choose option:
        1. Registration
        2. Login
        3. Profile
        4. Update profile
        5. Logout
        6. Main Menu
        7. Exit

            select option 1/2/3/4/5/6/7: ''')

    if response == '1':
        register()
    elif response == '2':
        login()
    elif response == '3':
        show_profile()
    elif response == '4':
        update_profile()
    elif response == '5':
        logout()
    elif response == '6':
        main()
    elif response == '7':
        terminate()
    else:
        print("Invalid Choice, Please select correct option")
        main()

print("Welcome to LNCT Student System")
main()