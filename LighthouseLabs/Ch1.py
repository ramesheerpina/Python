correct_email = "ram.eerpina"
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    email = input("Please enter your email: \n")
    if email == correct_email:
        print("Log in is Succesful")
        break
    else:
        print("Incorrect login")
        guess_count += 1
else:
    print("Maximum Attempts Reached")