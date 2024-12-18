# a function to generate a random password
# function name: generate_password
# input: length of the password
# output: password
# requirements:
# 1. password length should be equal to the input length
# 2. password should contain at least 2 uppercase letter
# 3. password should contain at least one lowercase letter
# 4. password should contain at least 3 digit
# 5. password should contain at least 1 special character in ">" and "<"
# 6. password should not contain any space
# 7. password should begin with an uppercase letter
def generate_password(length):
    import random
    import string
    password_list = []
    password_list.append(random.choice(string.ascii_uppercase))
    password_list.append(random.choice(string.ascii_lowercase))
    password_list.append(random.choice(string.digits))
    password_list.append(random.choice(['>', '<']))
    for i in range(4, length):
        password_list.append(random.choice(string.ascii_letters + string.digits + ['>', '<']))
    random.shuffle(password_list)
    return ''.join(password_list)