import re

# Password strength check condition:
# min 8 chars, digit, uppercase, lowercase, special char

def check_pass_strength(password):
    # Check if the password length is at least 8 characters
    if len(password) < 8:
        return 'Weak: password not usefull'

    # Check if password contains at least one digit
    if not any(char.isdigit() for char in password):
        return "Weak: password must contain a digit"

    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Weak: password must contain an uppercase letter"

    # Check if password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return "Weak: password must contain a lowercase letter"
    
    # Check if password contains at least one special character
    if not re.search(r'[!@#$%^&*()\-+={}[\]|:"<>,./?]', password):
        return "Medium: password must contain a special character"
    
    return "Strong: Your password is secure!"

def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit):")
        
        if password.lower() == 'exit':
            print("Thank you for using this tool!")
            break
        
        result = check_pass_strength(password)
        print(result)

# Run the password checker tool
if __name__ == "__main__":
    password_checker()
