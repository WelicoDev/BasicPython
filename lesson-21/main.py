# lst = [7 , 12, 14, 20, 27]
# for i in range(len(lst)):
#     print(lst[i], end=" ")
#
# print()
#
# for i in lst:
#     print(i , end=" ")

# lst = ["Hello", "My", "name", "John"]
# info = " ".join(lst)
# print(info)
#
# lst = [
#     [2, 5, 7],
#     [14, 20, 27 , {"name":"Otabek"}],
#     [16, 18, 22]
# ]
#
# for i in lst:
#     for j in i:
#         print(j , end=" ")
#     print()

# lst = [
#     [2, 5, 7],
#     [14, 20, 27],
#     [16, 18, 22],
#     [44, 47, 49]
# ]
#
# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         print(lst[i][j] , end=" ")
#     print()



# lst = [[int(i) for i in input().split()] , [int(i) for i in input().split()] , [int(i) for i in input().split()]]
#
#
# d1 = 0
# d2 = 0
# for i in range(len(lst)):
#     s = 0
#     v = 0
#     for j in range(len(lst[i])):
#         s += lst[i][j]
#         v += lst[j][i]
#     d1 += lst[i][i]
#
#     print(f"gorizantal : {s} , vertikal {v}")
# print(f"dioganal 1 : {d1}")

# print()
# print("vertikal : ", end=" ")
# for i in range(len(lst)):
#     S = 0
#     for j in range(len(lst[i])):
#         S += lst[j][i]
#
#     print(S , end=" ")



n = int(input("n : "))
lst = []
for i in range(n):
    lst.append([int(i) for i in input().split()])

d1 = 0
d2 = 0
j = len(lst) - 1
for i in range(len(lst)):
    s = 0
    v = 0
    for j in range(len(lst[i])):
        s += lst[i][j]
        v += lst[j][i]
        if i == j:
            d1 += lst[i][j]
            d2 += lst[j][i]
    print(f"gorizantal : {s} , vertikal {v}")

print(f"dioganal 1 : {d1} \ndioganal 2 : {d2}")

