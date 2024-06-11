# a = int(input("a : "))
# b = int(input("b : "))
# amal = input("amal : ")
#
# if amal == "+" or amal == "-" or amal == "*" or amal == "/":
#     if amal == "+":
#         print(a, "+", b , "=",a+b)
#     if amal == "-":
#         print(a, "-", b ,"=", a-b)
#     if amal == "*":
#         print(a, "*", b ,"=", a*b)
#     if amal == "/":
#         print(a, "/", b ,"=", a/b)
# else:
#     print("Noto'g'ri amal kiritildi !")
#

x = int(input("number : "))
y = int(input("len : "))

for i in range(1, y+1):
    print(x , "x" , i , "=",  x * i)