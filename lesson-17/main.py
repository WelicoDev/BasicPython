# import random
# d = {
#     "cars":[]
# }
#
# n = int(input("number of cars>> "))
# for i in range(1 , n + 1):
#     d_c = {
#         "model":f"gentra-{i}",
#         "year": random.randint(2000 , 2024),
#         "price":random.randint(10000 , 20000),
#         "probeg":random.randint(0 , 300000)
#     }
#     d["cars"].append(d_c)
#
# answer = input("Do you want to sort card by price price/year/probeg ? >> ")
# if answer in ("price" , "year" , "probeg"):
#     d["cars"].sort(key=lambda x: x[answer])
# else:
#     print("Sorry , I didn't understand")
#     raise ValueError("You have to choose on of")
#
#
#
# for i in d["cars"]:
#     print(i["model"] , i["year"] , i["price"], i["probeg"])

# def cmx(x):
#     return (len(x) , x[0])

# lst = ["olma", "nok" , "olcha" , "shaftoli", "banan", "gilos"]
# lst.sort(key=lambda x : (len(x) , x[0]))
# print(lst)

