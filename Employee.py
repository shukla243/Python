class Employee():
    count = 0
    def __init__(self,*args,**kwargs):
        self.name = args[0]
        self.desig = args[1]
        self.salary = kwargs['s']
        Employee.count += 1

    def Display(self):
            print("There are %d employees" % Employee.count)
    def Emp(self):
            print("Name:",self.name,", Designation:",self.desig,", Salary:",self.salary)

e1 = Employee('Shukla','Manager',s=80000)
e1.Emp()

e2 = Employee('Dakshayini','Team Lead',s=50000)
e2.Emp()

e2.Display()



