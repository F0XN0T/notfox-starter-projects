from cryptography.fernet import Fernet
import os


def load_key():
    # Use the absolute path to your 'key.key' file
    key_file_path = "D:/VSCode/September/key.key"
    if os.path.isfile(key_file_path):
        with open(key_file_path, "rb") as key_file:
            key = key_file.read()
        return key
    else:
        print("Key file 'key.key' not found.")
        exit(1)


def retrieve_password():
    # Full path to 'passwords.txt'
    password_file_path = "D:/VSCode/September/passwords.txt"
    with open(password_file_path, "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if " | " in data:
                user, passw = data.split(" | ")
                try:
                    decrypted_password = fer.decrypt(passw.encode()).decode()
                    print(user, ",", decrypted_password)
                except Exception as e:
                    print("Error decrypting password:", str(e))
            else:
                print("Invalid format in passwords.txt:", data)


def store_password():
    # Full path to 'passwords.txt'
    password_file_path = "D:/VSCode/September/passwords.txt"
    name = input("login name: ")
    pwd = input("password: ")

    # Encrypt the password and format it as a valid entry
    encrypted_password = fer.encrypt(pwd.encode()).decode()
    entry = f"username: {name} | password: {encrypted_password}\n"

    with open(password_file_path, "a") as f:
        f.write(entry)


key = load_key()
fer = Fernet(key)

while True:
    mode = input(
        "Do you want to store a password (s) or retrieve a password (r)? press (q) to quit: ").lower()
    if mode == "q":
        break

    if mode == "s":
        store_password()
    elif mode == "r":
        retrieve_password()
    else:
        print("Invalid mode.")
        continue
