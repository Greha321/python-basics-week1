def is_valid_username(username):
    username = username.strip()

    if len(username) < 5:
        return "Username is too short"
    elif " " in username:
        return "Username should not contain spaces"
    else:
        return "Username is valid"
user = input("Enter Username: ")
result = is_valid_username(user)
print (result)