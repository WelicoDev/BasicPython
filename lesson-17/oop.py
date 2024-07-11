# class Person:
#     pass
#
# p = Person()
# p.name = "Ali"
# p.age = 20
#
# print(p.name , p.age)
# print(type(p))

# class Person():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def full_name(self):
#         return f"{last_name} {first_name}"
#
# n = int(input("number of information person : >> "))
# lst = []
# for i in range(1 ,n+1):
#     first_name = input(f"your name - {i} : ")
#     last_name = input(f"your surname - {i} : ")
#
#     people = Person(first_name, last_name)
#
#     lst.append(people.full_name())
# for i in lst:
#     print(i)

# class Student:
#     def __init__(self , name , surname):
#         self.name = name
#         self.surname = surname
#     def __str__(self):
#         return f"{self.name} {self.surname}"
#
# talaba = Student("Otabek" , "Xurramov")
# print(talaba)

class Cars:
    def __init__(self , name , model , probeg , price , color):
        self.name = name
        self.model = model
        self.probeg = probeg
        self.price = price
        self.color = color

    def __str__(self):
        return str(self.price)

    def __add__(self , other):
        self.price =  self.price + other.price
        return self

car = Cars("Gentra" , "Chevrolet", 12000 , 16000 , "qora")
car2 = Cars("Malibu" , "Chevrolet", 4000 , 36000 , "qora")
car3 = Cars("BYD" , "BuildDreams", 14000 , 28000 , "qora")
print(car + car2 + car3)

