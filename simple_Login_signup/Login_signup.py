print("Create Account now")

username = input("Enter username: ")
password = input("Enter password: ")

print("Your account has been created successfully")
print("Log in now!")

username_log = input("Enter username: ")
password_log = input("Enter password: ")

if username == username_log and password == password_log:
    print(f"Log in successfull, Welcome {username}")
else:
    print("One or more of your creadentials don't match")
