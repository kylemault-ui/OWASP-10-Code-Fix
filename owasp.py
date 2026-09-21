# Broken Access Control

def get_profile(current_user_id, profile_id):
    if current_user_id != profile_id:
        return "Access denied"

    return "Profile information"


print(get_profile(1, 1))
print(get_profile(1, 2))


# Broken Access Control

def get_account(current_user_id, account_id):
    if current_user_id != account_id:
        return "Access denied"

    return "Account information"


print(get_account(1, 1))
print(get_account(1, 2))



# Cryptographic Failures 

import bcrypt

def hash_password(password):
    password = password.encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


password = "MyPassword123"
hashed_password = hash_password(password)

print("Password was hashed.")
print(hashed_password)


# Cryptographic Failures 

import bcrypt

def hash_password(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )


password = "MyPassword123"
hashed = hash_password(password)

print("Password was hashed.")
print(hashed)



# Injection 

import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("CREATE TABLE users (username TEXT)")
cursor.execute("INSERT INTO users VALUES ('kyle')")

username = input("Enter username: ")

cursor.execute(
    "SELECT * FROM users WHERE username = ?",
    (username,)
)

user = cursor.fetchone()

if user:
    print("User found.")
else:
    print("User not found.")

connection.close()



# Injection 

def find_user(username):
    if not isinstance(username, str):
        return "Invalid username"

    if len(username) > 50:
        return "Username is too long"

    return "Searching for user: " + username


username = input("Enter username: ")
print(find_user(username))




# Insecure Design 

import secrets
import bcrypt

reset_token = secrets.token_urlsafe(32)

def reset_password(token, correct_token, new_password):
    if token != correct_token:
        return "Invalid reset token"

    hashed_password = bcrypt.hashpw(
        new_password.encode(),
        bcrypt.gensalt()
    )

    return "Password reset successfully"


password = input("Enter new password: ")
token = input("Enter reset token: ")

print(reset_password(token, reset_token, password))




# Software and Data Integrity Failures 

import hashlib

def check_file(file_name, expected_hash):
    with open(file_name, "rb") as file:
        file_data = file.read()

    actual_hash = hashlib.sha384(file_data).hexdigest()

    if actual_hash == expected_hash:
        return "File is safe."
    else:
        return "File has been changed."


print("File integrity checker")




# Server-Side Request Forgery 

from urllib.parse import urlparse
import requests

url = input("Enter URL: ")
parsed = urlparse(url)

if parsed.scheme not in ["http", "https"]:
    print("Invalid URL")
else:
    try:
        response = requests.get(url, timeout=5)
        print(response.text)
    except requests.RequestException:
        print("Could not connect to the URL.")




# Identification and Authentication Failures 

import bcrypt

password = "MyPassword123"

stored_password = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)

input_password = input("Enter password: ")

if bcrypt.checkpw(input_password.encode(), stored_password):
    print("Login success")
else:
    print("Login failed")