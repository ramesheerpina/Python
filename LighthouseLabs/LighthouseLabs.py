# write a program to find 'alomond milk' and 'right logo'

cartoons = [
    ["not almond milk", 'wrong logo'],
    ["not almond milk", 'wrong logo'],
    ["almond milk", 'wrong logo'],
    ["almond milk", 'right logo'],
    ["almond milk", 'wrong logo']
]
cart = []
for carton in cartoons:
    typeofMilk = carton[0]
    logo = carton[1]
    if typeofMilk is 'almond milk' and logo is 'right logo':
        cart.append(carton)
        break
if len(cart) is 0:
    cart.append("beer")

print(cart)
