username = input("Enter your username: ")
password = input("Enter your password: ") 
print("==========================================")
print("       PASSWORD VALIDATION REPORT         ")
print("==========================================")
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")
print()
length_check = len(password) >= 8
length_msg = f"[PASS] Minimum 8 characters ({len(password)} characters)" if length_check else f"[FAIL] Minimum 8 characters ({len(password)} characters)"
digit_check = any(char.isdigit() for char in password)
digit_msg = "[PASS] At least one digit" if digit_check else "[FAIL] At least one digit"
upper_check = any(char.isupper() for char in password)
upper_msg = "[PASS] At least one uppercase letter" if upper_check else "[FAIL] At least one uppercase letter"
print("--- Validation Rules ---")
print(length_msg)
print(digit_msg)
print(upper_msg)
print()
print("--- Result ---")
if length_check and digit_check and upper_check:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")
    print("Please meet all password requirements.")
print("==========================================")