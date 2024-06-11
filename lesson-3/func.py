a = "hi there !"

print(a.find('h'))
print(a.rfind('h'))
print(a.count('h'))

word = "assalom aleykum"

print(word.replace('a' , 'A'))
print(word.upper())
print(word.lower())
print(word.capitalize())

x = 20
print(type(x))
x = str(x)
print(type(x))

a = "3"
b = "8"
print(a + b , type(a+b))

a = int(a)
b = int(b)

print(a+b , type(a+b))

y = "44"
z = "ok"
print(y.isdigit())

print(z.isalpha())

k = "$"
print(k.isascii())