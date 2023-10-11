from random import choice

heads=0
for _ in range(1000000):
    result=choice(["H","T"])
    if result=="H":
        heads+=1
print(heads)