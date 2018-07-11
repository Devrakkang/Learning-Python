from statistics import mean
num = []

for i in range(5) :
    num.append(int(input("Input Number : ")))

# for i in num :
#     print(i)

#--Min--Max
# 20 10 50 30 40

Min = 9999999
Max = 0
total = 0
for i in range(5) :
    # Min
    if num[i] <= Min :
        Min = num[i]
    # Max
    if num[i] >= Max :
        Max = num[i]

    total+=num[i]

print("Min =", Min)
print("Max =", Max)
print("Sum =", total)
print("Lenght =", len(num))
print("AVG =", total/5)
print("Function------------")
print("Min = ", min(num))
print("Max = ", max(num))
print("Sum =", sum(num))
print("AVG =", sum(num)/len(num))
print(mean(num))
