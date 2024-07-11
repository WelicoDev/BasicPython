class Item:
    def __init__(self , name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"{self.quantity} ta {self.name} , narxi : {self.price}"

class Phone(Item):
    def __init__(self , name , price , quantity , ram , memory , color , model):
        super().__init__(name , price , quantity)
        self.ram = ram
        self.memory = memory
        self.color = color
        self.model = model
    def __str__(self):
        return f"{self.ram}/{self.memory} {self.color} {self.model} {self.name}"
class Laptop(Phone):
    def __init__(self , name , price , quantity , ram , memory ,  color , model , yadro , protsessor):
        super().__init__(name , price , quantity , ram , memory,color , model)
        self.yadro = yadro
        self.protsessor = protsessor


    def __str__(self):
        return f"{self.protsessor} protsessor {self.ram}/{self.memory} {self.color} {self.model} {self.name}"

item = Item("Iphone 11 pro" , 450 , 44)
phone = Phone("Iphone 13 pro" , 650 , 100 , 8 , 128  , "black" , "Apple")
laptop = Laptop("Mackbook" , 1999 , 36 , 16 , 512 , "white" , "Apple" , 12 , "core i9")

print(item)
print(phone)
print(laptop)