import math

index = 0
while index < 101:
    if math.sqrt(index)%2 == 0:
        print("The square root of",index,"is",int(math.sqrt(index)))
    index += 1