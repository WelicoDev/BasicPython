# data = {
#     "name":"Otabek",
#     "age":20,
#     "study":"TUIT",
#     "is_activa":True
# }
#
# print(data["age"])
# print(data.get("study"))
# print(data.keys())
# print(data.values())
# print(data.items())

# numbers = [4 , -11 , 28 , 0 , 6 , 44 , -30 , 10]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print("reverse : " , numbers)

# def cmp(x):
#     print(x)
#     return x[-1]
#
# fruits = ["apple", "pair" , "cherry", "orange"]
#
# fruits.sort(key=cmp)
# print(fruits)

S = {}
lst = [44 , 5 , 14 , 24 , 39 , 96]
for num in lst:
    count = 0
    for i in range(1 , num+1):
        if num%i == 0:
            count += 1
    S[count]=num

lst = list(S)
lst.sort()
for i in lst:
    print(i , S[i])
