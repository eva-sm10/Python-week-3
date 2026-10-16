correct_username = "harry"
correct_password = "potter"
username = input("Enter your username: ")
password = input("Enter your passsword: ")
if username == correct_username and password == correct_password:
    print("Welcome to Hogwarts!")
else:
    print("Access denied.")