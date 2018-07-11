my = int(input("My Year Of Birth(BE) : "))
mom = int(input("Mom Year Of Birth(BE) : "))
dad = int(input("Dad Year Of Birth(BE) : "))

def calcYear(be) :
    return be-543

print("My Year Of Birth(BC) = ", calcYear(my))
print("Mom Year Of Birth(BC) = ", calcYear(mom))
print("Dad Year Of Birth(BC) = ", calcYear(dad))
