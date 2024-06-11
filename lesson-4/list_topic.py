# x = [14 , 20 , "Otabek", "TUIT"]
# print(x)
#
# print("# append method")
# x.append("Software engineer")
# print(x)
#
# x.pop()
# print("# pop method")
# print(x)
#
# x.remove(14)
# print(x)

# a = [24 , 14, -33 , 77 , 91 , -44]
#
# print(len(a))
#
# print(a[3])
# print(a[-1])
# print(a[::2])
# print(a[::-1])

a = [24 , 14, -33 , 77 , 91 , -44]
a.remove(-44)
print("remove", a)
a.pop()
print("pop", a)
a.pop(2)
print("pop index", a)
a.remove(a[1])
print("remove value index", a)