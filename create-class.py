class Student:
    sid = ""
    fname = ""
    lname = ""
    age = ""

    def funcId(self, reqId):
        output = self.sid = reqId
        return output

    def funcFname(self, reqFname):
        output = self.fname = reqFname
        return output

    def funcLname(self, reqLname):
        output = self.lname = reqLname
        return output

    def funcAge(self, reqYear):
        output = self.age = reqYear
        return output

s1 = Student()
s2 = Student()

inSid = input("Input ID : ")
inFname = input("Input Fname : ")
inLname = input("Input Lname : ")
inYear= input("Input Year : ")

inSid2 = input("Input ID : ")
inFname2 = input("Input Fname : ")
inLname2 = input("Input Lname : ")
inYear2 = input("Input Year : ")

print("---------------------")
print(" ")
print("ID = "+s1.funcId(inSid))
print("Firstname = "+s1.funcFname(inFname))
print("Lastname = "+s1.funcLname(inLname))
print("Age = "+s1.funcAge(inYear))
print("---------------------")
print(" ")
print("ID = "+s2.funcId(inSid2))
print("Firstname = "+s2.funcFname(inFname2))
print("Lastname = "+s2.funcLname(inLname2))
print("Age = "+s2.funcAge(inYear2))
print("---------------------")
