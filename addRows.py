import random
i=0
j=0
while j<50:
    print("{",end=" ")
    while i<30:
        print(random.randint(0, 1),end=", ")
        i=i+1
    j=j+1
    i=0
    print("},")
