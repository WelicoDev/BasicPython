import random

d = {
    "students":[]
}

n = int(input("Nechta student kiritmoqchisiz ? >> "))

for i in range(1 , n+1):
    print(f"Student {i}")

    d_s = {
        "name": f"name{i}",
        "email":f"email{i}",
        "avg":random.randint(1 , 100)
    }

    d["students"].append(d_s)

answer = input("Studentlarni avg bo'yicha o'sish tartibida chiqarmoqchimisiz ?(ha/yo'q) >> ")
if answer == "ha":
    d["students"].sort(key=lambda x : x["avg"])
else:
    d["students"].sort(key=lambda x: -x["avg"])

for student in d["students"]:
    print(student["name"] , student["email"], student["avg"])
