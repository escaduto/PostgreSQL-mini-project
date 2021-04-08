# regular method 
student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence): 
    return sum(sequence) / len(sequence) 

print(average(student['grades']))

# object-oriented-programming method 

class Student: 
    def __init__(self, name, grades): 
        self.name = name
        self.grades = grades

    def average(self): 
        return sum(self.grades) / len(self.grades) 

student = Student("Bob", (89, 90, 93, 78, 90))
student2 = Student("Rolph", (100, 92, 93, 78, 90))

print(student.name)
print(student.grades)
print(Student.average(student))
print(student.average())
print(student2.average())
