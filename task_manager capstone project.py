user_file = open("user.txt", 'r+')
login = False

# get user info and check if details are correct
while login == False:
    username = input("please enter username: ")
    password = input("please enter password: ")

    for line in user_file:
        valid_user, valid_password = line.split(", ")
        # check if the login details are the same as in the file
        if username == valid_user and password == valid_password:
            login = True
            print("welcome, you have successfully logged in")

    # displayed once user enters incorrect information
    if login == False:
        print("incorrect details! please enter valid username and password ")

    # to start at the beginning of the file
    user_file.seek(0)

user_file.close()

# menu options
choice = input("""Please select one of the following options
r - register user
a - add task
va - view all tasks
vm - view my tasks
e - exit
""")

# register user
if choice == "r":
    tasks = open("tasks.txt", 'a+')
    new_username = input("please enter the username you would like to create: \n")
    new_password = input("please enter your password: \n")
    confirm_password = input("please confirm password: ")
    # write to the users file
    user_file.write((new_username, new_password))
    tasks.close()

user_file.close()