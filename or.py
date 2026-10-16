correct_username = "harry"
correct_password = "potter"
username = input("Enter your username: ")
password = input("Enter your passsword: ")
if username != correct_username or password != correct_password:
    print("Access denied. Go away!")
else:
    print("Welcome to Hogwarts!")