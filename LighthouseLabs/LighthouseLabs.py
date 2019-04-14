instructionsteps = [
    "turn left",
    "go straight for 2 blocks",
    "turn right",
    "keep going until you see the dog statue",
    "turn right",
    "turn right again",
    "park right on the street"
]

instructionScreemed = []
for nextinstruction in instructionsteps:
    upperinstruction = nextinstruction.upper()
    instructionScreemed.append(upperinstruction)
print(instructionScreemed, "you are there")