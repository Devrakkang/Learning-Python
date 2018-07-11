# lang = ["C#", "Java", "Python", "Go", "Ruby", "Swift", "PHP"]
num = []
count = 5
for i in range(count) :
    # num += input("Input Number : ")           #string
    num.append(int(input("Input Number : ")))   #int
index = int(input("Enter Print Index >>> "))
print(num[index])
print(num)
