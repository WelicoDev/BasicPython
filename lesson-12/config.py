# shablon  = "Xurmatli {} , sizni {} universitetiga qabul qilindingiz !"

# def number(n):
#     for i in range(1, n+1):
#         print(i , end=" ")

# from datetime import datetime
#
# day = datetime.now().day
# mon = datetime.now().month
# print(mon)
# year = datetime.now().year
# months = {
#     "1":"yanvar",
#     "2":"Fevral",
#     "3":"Mart",
#     "4":"April",
#     "5":"May",
#     "6":"Iyun",
#     "7":"Iyul",
#     "8":"Avgust",
#     "9":"Sentyabr",
#     "10":"Oktyabr",
#     "11":"Noyabr",
#     "12":"Dekabr"
# }
# print(f"{day}-{months.get(str(mon))} {year}")

# from datetime import datetime
#
# b_day = int(input("birthday day : "))
# b_mon = int(input("birthday month : "))
# b_year = int(input("birthday year : "))
#
# months = {
#     "1":"yanvar",
#     "2":"Fevral",
#     "3":"Mart",
#     "4":"April",
#     "5":"May",
#     "6":"Iyun",
#     "7":"Iyul",
#     "8":"Avgust",
#     "9":"Sentyabr",
#     "10":"Oktyabr",
#     "11":"Noyabr",
#     "12":"Dekabr"
# }
#
# t_day = datetime.now().day
# t_mon = datetime.now().month
# t_year = datetime.now().year
# t_hour = datetime.now().hour
# t_min = datetime.now().minute
# t_sec = datetime.now().second
# print(f"{t_day}-{months.get(str(t_mon)).lower()} {t_year} yil / {t_hour}:{t_min}:{t_sec}")

# from datetime import datetime
#
# date_now = datetime.now()
# print(date_now.strftime("%d/%m/%y")) # bugungi sanani chiqaradi ! output : 01/07/24 kun/oy/yil
# print(date_now.strftime("%A")) # hafta kunini chiqarib  beradi ! output : Monday
# print(date_now.strftime("%a")) # hafta kunini qisqarmasini chiqarib  beradi ! output : Mon
# print(date_now.strftime("%c")) # Bugungi sana va vaqtni ko'rsatib beradi ! output : Mon Jul  1 23:11:35 2024
# print(date_now.strftime("%x")) # Sanani format ko'rinishida chiqarib beradi ! output : 07/01/24
# print(date_now.strftime("%G")) # Bu yilni chiqaradi ! output : 2024

from datetime import datetime