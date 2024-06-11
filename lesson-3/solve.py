n = int(input("tayoqchalar sonini kiriting : "))
q = n%4

if q == 1:
    print("yutishni iloji yo'q !")
elif q == 2:
    print(1)
elif q == 3:
    print(2)
elif q == 4:
    print(3)
else:
    print("Butun son kiriting !")

from math import ceil
print(ceil(int(input())/2)+ceil(int(input())/2)+ceil(int(input())/2))

