username = input("username : ")
password = input("password : ")

true_username = "welicodev"
true_password = "Otabek2004"

if len(username) >= 5 and len(password) >= 8:
    if username == true_username:
        if password == true_password:
            print("Xush kelibsiz websitega !\nMuaffaqiyatli tizimga kirdingiz ✅")
        else:
            print("Parolingiz xato ! \nQayta urining ❗️")
    else:
        print("username xato ! \nQayta kiriting ❗️")
else:
    print("Username va password kerakli uzunlikka ega emas ❗️ \n"
          "Username 5 belgidan va password 8 belgidan kam bo'lmasligi kerak ❗️")