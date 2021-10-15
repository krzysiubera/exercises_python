import os


file_retrieval_dir = "files/"
password_file_name = "password.txt"
password_file_path = f"{file_retrieval_dir}{password_file_name}"

user_input = input("Enter your code: ")

if password_file_name not in os.listdir(file_retrieval_dir):
    with open(password_file_path, "w") as file:
        file.write(user_input)
    print("Code saved")
else:
    with open(password_file_path, "r") as file:
        password = file.read()
    if password == user_input:
        print("Correct code entered")
    else:
        print("Incorrect code entered")
