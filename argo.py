from argon2 import PasswordHasher

# Create an instance of PasswordHasher
ph = PasswordHasher()

# Hash a password
password = "my_secure_password"
hashed_password = ph.hash(password)

print("Hashed Password:", hashed_password)

# Verify a password
input_password = "my_secure_password"

try:
    # Verify if the entered password matches the stored hash
    ph.verify(hashed_password, input_password)
    print("Password matches!")
except Exception as e:
    print("Password does not match:", e)
