instructionsteps = [
    "turn left",
    "go straight for 2 blocks",
    "turn right",
    "keep going until you see the dog statue",
    "turn right",
    "turn right again",
    "park right on the street"
]

instruction = "First, "
for nextinstruction in instructionsteps:
    instruction = instruction + nextinstruction + " then "
print(instruction, "you are there")