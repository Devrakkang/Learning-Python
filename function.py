# 1 inch = 2.54 cm.
def convertInchToCm(inch):
    cm = 2.54
    return inch * cm


width = float(input("Enter Wide : "))
height = float(input("Enter High : "))
depth = float(input("Enter Deep : "))

print("Wide ",width," = ", convertInchToCm(width))
print("High ",height," = ", convertInchToCm(height))
print("Deep ",depth," = ", convertInchToCm(depth))
