
import time
bacteria ="\U0001F952"
generations = 10
for generation in range(0,generations):
    bacteria = bacteria*2
    print(generation)
    print(bacteria)
    time.sleep(0.3)