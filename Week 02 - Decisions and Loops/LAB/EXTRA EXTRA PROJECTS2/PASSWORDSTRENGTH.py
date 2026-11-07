email = input("Enter your email: ")
password = input("Enter your new password: ")

if len(password) < 8:
    print("Password is too short. It must be at least 8 characters long.")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.")
elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")
else:
    print("Password is strong.")

print("Email:", email)
print("Password:", password)
