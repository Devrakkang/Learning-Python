import random

name = input("Input Your Name : ")
user = input("Input Username : ")
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
passwd = []

for i in range(8):
    ran = random.randint(0, 61)
passwd += char[ran]

# print(passwd)
print("Lenght = ", len(passwd))
outPass = passwd[0] + passwd[1] + passwd[2] + passwd[3] + passwd[4] + passwd[5] + passwd[6] + passwd[7]

print("Name  =", name)
print("User = ", user)
print("Password = ", outPass)
# random.choice
