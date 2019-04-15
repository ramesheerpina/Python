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

for index in range(0,len(actors)):
    print((actors[index])+ " as "+ (roles[index]))

print("Using 'Enumerate' function")
#  "Enumerate" is a function that gives us access to two variables on each iteration:
#  The list item itself, and that item's index.
for index, actor in enumerate(actors):
    print((actor)+ " as "+ (roles[index]))

enumerableActors = enumerate(actors)
