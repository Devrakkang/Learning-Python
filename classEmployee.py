class Employee:
    name = ""
    hr = 0
    money = 35

    def InEmpName(self, reqName):
        self.name = reqName

    def InEmpHr(self, reqHr):
        self.hr = reqHr

    def OutEmpName(self):
        return self.name
        
    def OutEmpHr(self):
        return self.hr*35

Emp1 = Employee()
Emp2 = Employee()
Emp3 = Employee()

Emp1.InEmpName(input("Input Employee Name : "))
Emp1.InEmpHr(int(input("Input Work Hour : ")))
print("-----------------")
Emp2.InEmpName(input("Input Employee Name : "))
Emp2.InEmpHr(int(input("Input Work Hour : ")))
print("-----------------")
Emp3.InEmpName(input("Input Employee Name : "))
Emp3.InEmpHr(int(input("Input Work Hour : ")))
print("-----------------")


print("Employee Name = ",Emp2.OutEmpName())
print("Salary = ",Emp2.OutEmpHr())
print("-----------------")