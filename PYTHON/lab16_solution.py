
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return None
    return a / b
def modulus(a, b):
    if b == 0:
        return None
    return a % b
def power(base, exp=2):
    return base ** exp
def format_number(n):
    if n == int(n):
        return int(n)
    return n
history = []
while True:
    print("\n========== ENTERPRISE MODULAR UTILITY CALCULATOR ==========")
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")
    choice = input("\nEnter your choice (1-8): ")
    if choice in ["1", "2", "3", "4", "5"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if choice == "1":
                result = add(a, b)
                operator = "+"
            elif choice == "2":
                result = subtract(a, b)
                operator = "-"
            elif choice == "3":
                result = multiply(a, b)
                operator = "*"
            elif choice == "4":
                result = divide(a, b)
                operator = "/"
            elif choice == "5":
                result = modulus(a, b)
                operator = "%"
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                a = format_number(a)
                b = format_number(b)
                result = format_number(result)
                print("Result:", result)
                record = f"{a} {operator} {b} = {result}"
                history.append(record)
        except ValueError:
            print("Invalid input! Enter numbers only.")
    elif choice == "6":
        try:
            base = float(input("Enter base: "))
            exp = input("Enter exponent (press Enter for default 2): ")
            if exp == "":
                result = power(base)
                exponent = 2
            else:
                exponent = float(exp)
                result = power(base, exponent)
            base = format_number(base)
            exponent = format_number(exponent)
            result = format_number(result)
            print("Result:", result)
            record = f"{base} ** {exponent} = {result}"
            history.append(record)
        except ValueError:
            print("Invalid input! Enter numbers only.")
    elif choice == "7":
        if len(history) == 0:
            print("No calculation history available.")
        else:
            print("\n===== CALCULATION HISTORY =====")
            for item in history:
                print(item)
    elif choice == "8":
        print("Thank you for using the calculator!")
        break
    else:
        print("Invalid choice! Please select between 1 and 8.")