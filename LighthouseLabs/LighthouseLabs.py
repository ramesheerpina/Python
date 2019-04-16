actors = [
    "Nathan Fillion",
    "Gina torres",
    "Alan Tudyk",
    "Morena Baccrin",
    "Adam Baldwin"
]
roles = [
    "Capatain Malcolm Reynolds",
    "Zoe Wasburn",
    "Hoban Washburn",
    "Inara Serra",
    "Jayne Cobb"
]
print("Featuring \n"
      "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

enumerableActors = enumerate(actors)
enumerableActorsList = list(enumerableActors)
print(enumerableActorsList)

for index, actor in enumerableActorsList:
    print(index)
    print(actor)

print(list(enumerate(actors)))

for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print(letter + " is the "+ str(index+1) + "th letter of alphabet")
