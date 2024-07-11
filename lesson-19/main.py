class User:
    def __init__(self , first_name , last_name ,age , username, password):
        self._id = 47811
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__username = username
        self.password = password

    def __get_age(self):
        return self.age
    def __str__(self):
        return f"{self.last_name} {self.first_name} username >> {self.__username} / {self.__get_age()} years old."

class Student(User):
    def __init__(self , first_name , last_name ,age , username, password , study , profession , course , gpa):
        super().__init__(first_name , last_name , age , username , password)
        self.study = study
        self.profession = profession
        self.course = course
        self.gpa = gpa

    def __str__(self):
        return f"{self.profession} {self.course}-kurs talabasi {self.first_name} {self.last_name}"

user = User("Otabek", "Xurramov" , 20 , "welicodev" , "Developer2024")
user.first_name = "Ozodbek"

print(user)