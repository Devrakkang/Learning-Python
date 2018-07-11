# n = 2
# for i in range(13):
#     if i == 0 :
#         print("")
#     else :
#         print("2 x ",i," = ",n*i)
#
# print("------------------")
#
# for i in range(1,13):
#     print("2 x ",i," = ",n*i)
#
# print("------------------")
#
# for i in range(12):
#     num = i+1
#     print(num*2)
#
# print("------------------")

n = int(input("Enter Number : "))
if(n >= 0) :
    for i in range(1,13) :
        print(n," x ", i, " = ", (n*i))
else :
    print("Error")
