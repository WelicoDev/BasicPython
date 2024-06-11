# a = 20
# c = 0
# try:
#     x = a / c
#     print(x)
# except ZeroDivisionError:
#     print("Sonni no'lga bo'lib bo'lmaydi !")
#
# print("another code .... ")

# a = 6
# b = "14"
#
# try:
#     print(a + b)
# except TypeError:
#     print("String va integer qiymatlarini qo'shish mumkin emas !")
#
# print("another code ...")

# a = 20
# b = 14
# try:
#     print(a + b + c)
# except Exception:
#     print("Code error !")
#
# print("another code !")

# a = 20
# b = "Otabek"
#
# try:
#     print(a + b)
# except Exception as e:
#     print(e)
#
# print("another code ....")

age = int(input())
year = 2024

try:
    if age < 0:
        raise ValueError("Musbat son kiritishingiz shart !")
    else:
        birthday = year - age
        print(birthday)
except Exception as e:
    print("Yoshingiz 150 dan katta bo'la olmaydi !")
    print(e)