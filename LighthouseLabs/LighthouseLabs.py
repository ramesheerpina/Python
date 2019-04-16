# excercise = password checker

pwd = ("123456")
initialcount = 0
finalcount = 5
while initialcount < finalcount:
    initialcount += 1
    password = input("Please enter your password")
    if password == pwd:
        print("You are in")
        break
    else:
        print("WRONG PASSWORD")