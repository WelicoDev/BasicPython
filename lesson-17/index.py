class Person:
    def __init__(self , first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def info(self):
        return f"Assalom aleykum {self.last_name} {self.first_name} . Sizni yoshingiz {self.age}"
    def __str__(self):
        return f"{self.last_name} {self.first_name} yoshingiz {self.age} da"

    @staticmethod # decorator
    def calculate_salary(salary):
        return 12 * salary * 0.88


people = Person("Otabek", "Xurramov" , 20)
print(people.info())
salary = Person.calculate_salary(700)
print(salary)


