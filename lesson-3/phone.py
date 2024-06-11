phone = input("phone : ")
collect = ""
for i in phone:
    if i.isdigit():
        collect+=i
if collect[:3]==998:
    print(f"+{collect}")
else:
    print(f"+998{collect}")
