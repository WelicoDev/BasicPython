# n = int(input())
# print(f"The next number for the number {n} is {n+1}.\nThe previous number for the number {n} is {n-1}.")

# def addnumber(a , b):
#     result = a + b
#     global c
#     c = b - a
#     return result
#
# value = addnumber(14 , 20)
# print(value)
# print(c)

# def add(a , b):
#     print(a + b)
#
# def inc(a , b):
#     print(a * b)

# def sub(a , b):
#     print(a - b)
#
# def div(a , b):
#     print(a / b)
# a = int(input("a : "))
# b = int(input("b : "))
# add(a , b)
# sub(a , b)
# inc(a , b)
# div(a , b)

# def add(a , b):
#     c = a + b
#     return c
#
# result = add(14 , 20)
# print(result ** 2)

# def full_name(name , surname):
#     return f"name : {name}\nsurname : {surname}"
#
# name = input("name : ")
# surname = input("surname : ")
# fullname = full_name(name , surname)
# print(fullname)

# def piramit(n):
#     for i in range(1, n+1):
#         for a in range(1 , i+1):
#             print('*' , end="")
#         print()
#
# n = int(input("n : "))
# piramit(n)

# def ekub(n):
#     for i in range(1, n+1):
#         if n%i == 0:
#             print(i , end=" ")
#
#
# n = int(input())
# ekub(n)

n = int(input("enter number : "))
s = 0
for i in range(1, n+1):
    if n%i == 0:
        s += i

if s == n + 1:
    print("TUB son")
else:
    print("TUB son emas !")