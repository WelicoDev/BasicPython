# class Person:
#     def __init__(self , first_name , last_name , age ):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def __str__(self):
#         return f"{self.age} yosh {self.last_name} {self.first_name}"
#
#     def __add__(self, other):
#         self.age = self.age + other
#         return self.age
#
# people = Person("Otabek" , "Xurramov", 20)
# print(people)
#
# class Student(Person):
#     def __init__(self,first_name , last_name , age,  study, profession, course, gpa):
#         # Person.__init__(self , first_name, last_name, age)
#         super().__init__(first_name, last_name, age)
#         self.study = study
#         self.profession = profession
#         self.course = course
#         self.gpa = gpa
#     def info_student(self):
#         return f"{self.course}-kurs talabasi {self.first_name} {self.last_name}"
#     def __str__(self):
#         return f"{self.study} universiteti {self.profession} {self.course}-talabasi {self.first_name} {self.last_name}"
#
#
# student = Student("Javohir", "Namazov" , 21 , "TUIT", "Software enegeer", 3 , 3.8)
# print(student)
# print(student.info_student())


class A:
    def info(self):
        print("A")

class B(A):
    def info(self):
        print("B")

class C:
    def info(self):
        print("C")

class D(B , C):
    pass

c = D()
c.info()