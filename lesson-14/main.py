# lst = [4 , 8 , 24, "hello", True , "world", 20 , 14]
# print(lst[6])

# dic = {
#     "key":"value",
#     "first_name":"Otabek",
#     "last_name":"Xurramov",
#     "age":20,
#     "study":"TUIT"
# }
#
# print(dic["first_name"])
# print(dic.get("study"))
# key : int , str , float -- > immutable (o'zgarmas) datetype
# value : pythonda bor hamma datetypelar (int , str , float , boolean , tuple , list , dictinary , set and other)

# numbers = {
#     1:"bir",
#     2:"ikki",
#     3:"uch",
#     4:"to'rt",
#     5:"besh",
#     6.38:"6 butun 38"
# }
#
# print(numbers[6.38])
# print(numbers[4])

# bio = {
#     "name":"Otabek"
# }
#
# bio["surname"] = "Xurramov"
# bio["age"] = 20
#
# print(bio)
# # change
# bio["name"] = "Ozodbek"
# print(bio)

# data = {
#     "student_id": 12,
#     "mark" : [44 , 68 , 58 , 88 , 96 , 100]
# }
#
# print(data["mark"][3])
# marks = data["mark"]

# print(sum(marks)//len(marks))

info = {
    "fakultet":"Dasturiy injinering",
    "students":[
        {
            "ism":"Otabek",
            "familya":"Xurramov",
            "gpa":3.94
        },
        {
            "ism":"Javohir",
            "familya":"Namazov",
            "gpa":4.17
        },
        {
            "ism":"Zohidjon",
            "familya":"Qodirov",
            "gpa":3.81
        },
{
            "ism":"Jahongir",
            "familya":"Qurbonov",
            "gpa":4.7
        }
    ],
    "course":4
}
data = {}
baholar = info["students"]
for i in baholar:
    data[i["gpa"]] = i["ism"] , i["familya"]

gpa_max = max(data.keys())
print(" ".join(data[gpa_max]) , gpa_max)