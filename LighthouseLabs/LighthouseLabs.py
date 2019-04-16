# excercise = password checker

pwd = ("123456")
initialcount = 0
finalcount = 5
while initialcount < finalcount:
    initialcount += 1
    password1 = input("Please enter your password")
    if len(password1) < 8:
        print("password too short")

    elif len(password1) > 8:
        print("password too long")

    elif len(password1) == 8:
        print("you password is 8 characters")
        while initialcount < finalcount :
            initialcount += 1
            password2 = input("Please enter your password again")
            if initialcount < finalcount and password1 == password2:
                print("You have succesfully set your password")
                break
            if initialcount < finalcount and password1 != password2:
                print("passwords didnt match")
            else:
                print("passwords didnt match and maximum attempts reached")
        break