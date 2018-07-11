n1 = 3
n2 = 2
n3 = 5
n4 = 4
n5 = 1

if n1>n2 and n1>n3 and n1>n4 and n1>n5 :
    max1 = n1
    print(max1)
elif n2>n1 and n2>n3 and n2>n4 and n2>n5 :
    max1 = n2
    print(max1)
elif n3>n1 and n3>n2 and n3>n4 and n3>n5 :
    max1 = n3
    print(max1)
elif n4>n1 and n4>n2 and n4>n3 and n4>n5 :
    max1 = n4
    print(max1)
elif n5>n1 and n5>n2 and n5>n3 and n5>n4 :
    max1 = n5
    print(max1)

# print(max1)
# print(n1)
# min1 = 0
# max1 = 5

for i in range(5) :
    if n1>=max1 :
        max1 = n1
    elif n2>=max1 :
        max1 = n2
    elif n3>=max1 :
        max1 = n3
    elif n4>=max1 :
        max1 = n4
    elif n5>=max1 :
        max1 = n5

    print("Max = ",max1)
