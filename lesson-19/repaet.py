# users = []
#
# count = int(input("number >>> "))
#
# for i in range(count):
#     users.append(input("info user : ").title())
#
# print(users)
# print(len(users))

a = input(" >> ").split(",")
S = 0
for i in a:
    assert int(i)!= 0 , "Invalid input"
    S += int(i)
print("sum : " , S)

