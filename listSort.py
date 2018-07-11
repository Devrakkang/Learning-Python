num = []
new_num = []
for i in range(3) :
    num.append(int(input("Input Number : ")))

for i in range(3):
    Min = num[0]
    for i in num :
        if i < Min :
            Min = i
    new_num.append(Min)
    num.remove(Min)
print("Sort :",new_num)

