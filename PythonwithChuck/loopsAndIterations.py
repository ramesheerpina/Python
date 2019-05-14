smallest = None
for value in [10, 12, 5, 89, 9, 2, 67]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)