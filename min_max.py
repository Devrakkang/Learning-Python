count  = int(input("Enter Round = "))
i = 0
while (i < count) :
    i = i + 1
    a  = int(input("Enter number 1 : "))
    b = int(input("Enter number 2 : "))

    if a > b :
        print("Max = ",a)
        print("Min = ",b)
    elif a == b :
        print("Equals")
        print(a," = ",b)
    else :
        print("Max = ",b)
        print("Min = ",a)

    print("----------------------")
