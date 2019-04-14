instructionsteps = [
    "turn left",
    "go straight for 2 blocks",
    "turn right",
    "keep going until you see the dog statue",
    "turn right",
    "turn right again",
    "park right on the street"
]


for nextinstruction in instructionsteps:
    instructionScreemed = []
    upperinstruction = nextinstruction.upper()
    instructionScreemed.append(upperinstruction)
print(instructionScreemed, "you are there")