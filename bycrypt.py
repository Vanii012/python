import bcrypt

# Hash a password
password = "my_secure_password"
salt = bcrypt.gensalt()  # Generate a salt
hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

print("Hashed Password:", hashed_password)

# Verify a password
input_password = "my_secure_password"
if bcrypt.checkpw(input_password.encode('utf-8'), hashed_password):
    print("Password matches!")
else:
    print("Password does not match.")
