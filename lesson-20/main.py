class Person:
    def __init__(self , first_name , last_name , age):
        self.__first_name = first_name
        self.last_name = last_name
        self.__age = age

    @property
    def name(self):
        return self.name

    def set_name(self , new_name):
        assert self.__age >= 18 , ValueError("Age must be grater than 18!")
        self.__age = new_name

        return self.__first_name
    @property
    def age(self):
        return self.__age

    def __str__(self):
        return f"{self.last_name} {self.__first_name}"


people = Person("Otabek", "Xurramov", 20)
print(people.set_name("Ozodbek"))