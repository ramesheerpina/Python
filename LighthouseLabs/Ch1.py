correct_email = "ram.eerpina"
password = "abc"
email_count = 0
email_limit = 3
pwd_count = 0
pwd_attempts = 3
while email_count < email_limit:
    email = input("Please enter your email: \n")
    email_count += 1
    if email == correct_email:
        print("Valid Email")
        while pwd_count < pwd_attempts:
            pwd = input("Please enter your password: \n")
            pwd_count += 1
            if pwd == password:
                print("Login Successful")
                break
            else:
                print("Login Failed, Wrong Password")
        else:
            print("Maximum Password attempts Reached")
        break
    else:
        print("Wrong email")
else:
    print("Maximum Email Attempts Reached")
