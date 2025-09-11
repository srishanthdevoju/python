class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Marks:", self.marks)
s1 = Student("Srishanth", 6752, 88)
s2 = Student("vignesh", 6741, 92)
s1.display()
s2.display()
