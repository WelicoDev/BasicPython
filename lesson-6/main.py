# x = 20
# y = 14
# while x > y :
#     print("Assalom aleykum !")
#     y +=1

# a = int(input())
# b = int(input())
# l = int(input())
# N = int(input())
# print(2*l+2*a*N+(N-1)*2*b)

# n = int(input())
# print(f"The next number for the number {n} is {n+1}.")
# print(f"The previous number for the number {n} is {n-1}.")

# balance = input("balance : ")
# balance = int(balance)
# while balance-5 > 2:
#     balance -= 2
#     print("Hello World !")

# n = int(input("n : "))
# S = 0
# while n > 0:
#     S += n
#     n -=1
# print(S)


# n = int(input("n : "))
# i = 0
#
# while i < n:
#     i += 1
#     print(i , end=" ")

a = int(input("a : "))
b = int(input("b : "))
juft = []
toq = []
while a <= b:
    if a % 2 == 0:
        juft.append(a)
    else:
        toq.append(a)
    a += 1
for i in juft:
    print( i , end=" ")
print("\n")
for i in toq:
    print( i , end=" ")

