# def add(*args):
#     print(sum(args))
#     for i in args:
#         print(i , end=" ")
#     print()
#
# add(7 , 3, 12, 8)
# add(44 , 56, 50 , 27)

# def add(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     if kwargs.get("name") is "Otabek":
#         print("Shaxs aniqlandi !")
#     else:
#         print("Error")
#
# add(name="Otabek")
# add(meva = ["olma", "anor" , "nok"])

def problem(*args , **kwargs):
    print("args : ", args)
    print("kwargs : ", kwargs)
    result = sum(args)

    if kwargs.get("show") is True:
        print(result)

problem(2 , 4, 5, 7 , 11, 14 , show=True)