# เส้นรอบวง 2 x pi x r
# พื้นที่ pi x r^2
# r = int(input("Input Radius : "))


# pi = 22/7
# area = pi*(r*r)
# rounded = 2*pi*r

# print("Circle Area = %.3f" %area)
# print("Rounded Circle = %.3f" %rounded)

class Circle:
    R = 0
    Pi = 22/7

    def SetR(self, r):
        self.R = r

    def GetR(self):
        return self.R

    def GetArea(self):
        return self.Pi*(self.R*self.R)

    def GetRound(self):
        return 2*self.Pi*self.R

    
cir1 = Circle()

cir1.SetR(int(input("Input Radius : ")))

print("Circle Area = %.2f" %cir1.GetArea())
print("Rounded Circle = %.2f" %cir1.GetRound())
