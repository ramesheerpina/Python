input1 = input("Enter name of a place: \n")
input2 = input("Enter name of abject: \n")
game ="Just as I arrived at place, I realized I had forgotten my object"
sentence = (game\
    .replace("place",input1)
    .replace("object",input2)
            )
print(sentence)