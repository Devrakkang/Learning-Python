list = []
new_list = []
for iten in range(5):
    num = int(input("Input Number : "))
    list.append(num)

print("Input = ",list)

# for i in list:
#     Min = list[0]
#     for i in list:
#         if i < Min:
#             Min = i
#         new_list.append(Min)
#         list.remove()
# print("Number = ",new_list)

while list :
    Min = list[0]
    for i in list :
        if i < Min :
            Min = i
    list.append(Min)
    list.remove(Min)
print("Sort :",new_list)