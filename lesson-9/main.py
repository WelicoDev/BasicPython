# n = int(input("n : "))
# m = int(input("m : "))
# S = []
# for i in range(n , m+1):
#     S.append(i)
#
# print(S)

# n = int(input("n : "))
# S = []
# for i in range(n):
#     a = int(input(f"number{i+1} : "))
#     S.append(a)
# print("sum : " , sum(S))

# print("sum : ",sum([int(input(f"number{i+1} : ")) for i in range(int(input("n : ")))]))

# n = int(input("n : "))
# lst = [i for i in range(1, n+1)]
# print(sum(lst))

# text = "2 3 4 76 79 80 -9 45 32"
# text = [int(i) for i in text.split()]
# print(sum(text))
# print(max(text))
# print(min(text))

# lst = [1 , 3, 5, 7, 9, 2, 4, 6, 8, 10]
# for i in range(len(lst)):
#     print(lst[i] , end=" ")


# juft = []
# toq = []
# for i in range(int(input("n : "))):
#     x = int(input(f"number{i+1} : "))
#     if x%2 == 0:
#         juft.append(x)
#     else:
#         toq.append(x)
# print("Juft : ", juft)
# print("Toq : ", toq)