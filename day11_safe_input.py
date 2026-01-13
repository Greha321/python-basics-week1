try:
    age = int(input("Enter your age: "))
    print(f"You are age is ",age)
except ValueError:
    print("Invalid input. Please enter a valid integer for your age.")