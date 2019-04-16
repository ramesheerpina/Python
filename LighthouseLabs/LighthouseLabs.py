# math game
questions  = [
    [1,2],
    [2,3],
    [3,4],
    [5,6]
]
score = 0
for a, b in questions:
    userresponse = int(input("What is the sum of " + str(a) + " " + str(b)))
    if userresponse == a+b:
        score +=1
        print("yay, you are correct, you scored 1 point")
    else:
        score = score
        print("not as much success, you scored no points")

if score > len(questions)/2:
    print("Great job! you score is " + str(score)+ " out of " + str(len(questions)))
else:
    print("Ahh shucks. you score is " + str(score)+ " out of " + str(len(questions)))