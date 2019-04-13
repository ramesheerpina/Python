houseprice = 100000
userCreditRating = input("Please enter user credit rating (bad, fair, good, excellent: \n ")
if userCreditRating == "bad":
    print("Downpayment will be " + str(round(houseprice*0.2)))
elif userCreditRating == "fair":
    print("Downpayment will be " + str(houseprice*0.15))
elif userCreditRating == "good":
    print("Downpayment will be " + str(houseprice*0.1))
else:
    print("Downpayment will be " + str(round(houseprice*0.05)))