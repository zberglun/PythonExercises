#Exercises for 21 Generators
def createSquare():
    i=1
    while True:
        yield i * i
        i += 1

for n in createSquare():
    if n>25:
        break
    print(n)


    