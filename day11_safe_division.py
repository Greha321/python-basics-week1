try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print(f"Result is {result}")
except ValueError:
    print("Invalid input. Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")