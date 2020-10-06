import math

for element in range(0,9):
    if element%2 == 0:
        print("The square root of",element,"is",math.sqrt(element))
        

index = 0
while index < 9:
    if index%2 == 0:
        print("The square root of",index,"is",math.sqrt(index))
    index += 1


