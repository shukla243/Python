class Student:
    def __init__(self,name,subject,grade):
        self.name = name
        self.subject = subject
        self.grade = grade

    def Details(self):
        print("Student name:",self.name)
        print("Subject:",self.subject)
        print("Grade:",self.grade)

class School(Student):
    def __init__(self,name,subject,grade,fees):
        self.fees = fees
        Student.__init__(self,name,subject,grade)

    def Fees(self):
        Student.Details(self)
        print("Fee status:",self.fees)

student1 = School("Shukla","python","A",bool(0))

student1.Fees()
print()

student2 = School("Dakshayini","python","A",bool(1))

student2.Fees()
