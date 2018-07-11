num = []
for i in range(3) :
    num.append(int(input("Input Number : ")))

for i in range(len(num)-1):
    for j in range(len(num)-1):
        if num[j] < num[j+1]:
            Min = num[j]
            num[j] = num[j+1]
            num[j+1] = Min

print(num)
num.reverse()
print(num)
