from random import randint
class Auto:
    def __init__(self , model , name , quantity , price):
        self.model = model
        self.name = name
        self.quantity = quantity
        self.price = price


    def __str__(self):
        return f"{self.model} {self.name}"

class Cars(Auto):
    def __init__(self , model , name , quantity , price , color , prabeg , year):
        super().__init__(model , name , quantity , price)
        self._id = randint(100000 , 999999)
        self.color = color
        self.__prabeg = prabeg
        self.__year = year

    def change_km(self , new_km):
        if new_km > 0:
            self.__prabeg + new_km

            return self.__prabeg
        else:
            return "Invalid KM"
    def __get_proveg(self):
        return self.__prabeg
    def __str__(self):
        return f"{self.__prabeg} km yurgan {self.__year} yil  {self.color} {self.model} {self.name}"

    def __len__(self):
        return self.name

    def __repr__(self):
        return f"{self.color}  {self.model} {self.name}"

car = Cars("Chevrolet" , "Malibu", 12 , 34000 , "black" , 44000 , 2023)
car.change_km(-1000)
print(car)