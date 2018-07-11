def TriArea(reqBase,reqHeight) :
    half = 0.5
    area = half*reqBase*reqHeight
    return area

base = float(input("Input Base Size : "))
height = float(input("Input Height Size :"))

print("Triangle Area = ",TriArea(base,height))
