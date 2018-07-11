import random

num = [1, 2, 3, 4, 5]
list = []
for item in range(5) :
    i = (len(num)-1)
    ran = num[random.randint(0, i)]
    num.remove(ran)
    list.append(ran)

print(len(num))
print(list)
    