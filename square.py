for i in range(10) :
    print("##########")
print("\n----------------\n")

for i in range(5) :
    print("0000000000")
print("\n----------------\n")

txt = ""
for i in range(1,10) :
    txt = txt + "*"
    print(txt)
print("\n----------------\n")

for i in range(1,10) :
    print("*"*i)
print("\n----------------\n")

num = 10
for i in range(num) :
    print("*"*(num-i))
print("\n----------------\n")

num2 = 10
for i in reversed(range(num)) :
    print("*"*(num2-i))
print("\n----------------\n")

num3 = 10
for i in reversed(range(num3)) :
    print("-"*i+"0"*(num3-i)+"0"*(num3-i-1)+"-"*i)
print("\n----------------\n")

num4 = 10
for i in range(num4) :
    print("-"*i+"0"*(num4-i)+"0"*(num4-i-1)+"-"*i)
print("\n----------------\n")


num5 = 1
num6 = 5
for i in range(num5) :
    print("0"*10)
    for i in range(num6) :
        print("0"+"-"*8+"0")
    print("0"*10)
