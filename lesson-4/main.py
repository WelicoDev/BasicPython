# a = 20
# b = "14"
#
# print(a+int(b))
# a += 1
# print(a)
# a -= 2
# print(a)
#
# a *= 2
# print(a)
#
# a //= 2
# print(a)
#

# text = "bomp hi there ... bompA BomP"
# print(text.count("bomp"))
#
# text = text.lower()
# print(text.count("bomp"))

# text = input("text : ")
#
# mylist = text.split()
# print(mylist)
# print(len(mylist))
#
# text_replace = text.replace('b', "B")
# print(text_replace)

# numbers = input("numbers : ")
# print(numbers.split(','))

# integer, float, string, bool , tuple , frozen_set - immutable
# list, dict , set - mutable

# text = input("text : ")
# number = ""
# for i in text.split():
#     number +=i
# print("number: ", number)
# print(int(number)**2)

# text = input("text : ")
# text = text.replace(" ", "")
# print(int(text)**2)

# print(sum([int(x) for x in input("numbers : ").split()]))

text = "salom hi there , history"
h_first = text.find('h')
h_last = text.rfind('h')
sub_text = text[h_first+1 : h_last]
print(sub_text.upper())
print(text[:h_first+1]+sub_text.upper()+text[h_last:])