# write a program to find 'alomond milk' and 'right logo'
#now add else statment to know how many cartons have been looked at before getting the right one

cartoons = [
    ["not almond milk", 'wrong logo'],
    ["not almond milk", 'wrong logo'],
    ["almond milk", 'wrong logo'],
    ["almond milk", 'right logo'],
    ["almond milk", 'wrong logo']
]
cart = []
wrongcartoons = 0
for carton in cartoons:
    typeofMilk = carton[0]
    logo = carton[1]
    if typeofMilk is 'almond milk' and logo is 'right logo':
        cart.append(carton)
        break
    else:
        wrongcartoons += 1

if len(cart) is 0:
    cart.append("beer")

print(" I looked at " + str(wrongcartoons) + " cartons that were not almond milk and with out the logo")
