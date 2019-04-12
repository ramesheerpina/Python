subtotal = float(input("Please input yout subtotal: "))
tip = float(input("Please enter your tip percent: "))
people= float(input("How many people attended the party: "))
taxrate  = 0.25
tipamount = subtotal * (tip/100)
# use round function to round the decimal places to 2
tax  = round(subtotal*taxrate, 2)
total = round(subtotal + tax, 2) + tipamount
ppp = total/people
print("Each person should pay: " + str(ppp))
print("Your total amount is: " + str(total))
