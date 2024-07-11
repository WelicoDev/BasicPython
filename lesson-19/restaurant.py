from random import randint
class Menu:
    def __init__(self , name , price , amount):
        self.name = name
        self.price = price
        self.amount = amount

    def __repr__(self):
        return f"{self.amount} {self.name} narxi : {self.price}"

class Client(Menu):
    def __init__(self , full_name):
        self._id = randint(100000 , 999999)
        self.full_name = full_name
        self.order = []

    def add_order(self , other):
        self.order.append(other)

        return self.order

    def get_order(self):
        return f"Orders : \n{self.order}"

    def __str__(self):
        return f"{self.full_name} \nOrders : {[i for i in self.order]}"

meal1  = Menu("Osh" , 22000 , "1 porsiya")
meal2  = Menu("Qozon Kabob" , 50000 , "1 porsiya")
meal3  = Menu("Shashlik" , 14000 , "1 six")
meal4  = Menu("Lag'mon" , 30000 , "1 porsiya")

client = Client("Otabek Xurramov")
client.add_order(meal1)
client.add_order(meal4)
print(client.get_order())
# print(client)