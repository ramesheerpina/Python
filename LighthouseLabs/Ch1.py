correct_email = "ram.eerpina"
password = "abc"
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    email = input("Please enter your email: \n")
    if email != correct_email:
        print("email not valid")
    else:
        pwd = input("Please enter your password: \n")
        if password == pwd:
            print("Login Successful")
            break
        else:
            print("Incorrect login")
            guess_count += 1
else:
    print("Maximum Attempts Reached")