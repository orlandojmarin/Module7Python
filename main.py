# Write a class called Student that has two instance variables, name and marks,
# and one class variable, passingMark. Assign 50 to passingMark. Within the
# class, you need to code the __init__ and __str__ methods. Next, write an
# instance method called passOrFail() within the Student class. This method
# returns the string "Pass" if marks is greater than or equal to passingMark
# or "Fail" if marks is lower than passingMark

class Student:
    # class variable passingMark is set to 50
    passingMark = 50
    
    # create the __init__ constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    # create the pass or fail method         
    def passOrFail(self):
        if (self.marks >= Student.passingMark):
            return "Pass"
        else:
            return "Fail"
    
    # create the __str__ method       
    def __str__(self):
        return f"Name: {self.name}, Marks: {self.marks}, Result: {self.passOrFail()}"


# create two students: student 1 and student 2
student1 = Student("Orlando", 93)
student2 = Student("Ronald", 45)

# print the results / information of the two students
print(student1)
print(student2)