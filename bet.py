import random


for i in range(10) :
    ran = random.randint(0,999)
    if(ran < 10) :
        print("00",ran)
    elif(ran < 100) :
        print("0",ran)
    else :
        print(ran)
