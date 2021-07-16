f = open("baza.txt", 'w')
username = "Narzullaev"
password = "1234"
f.write(username + '\n' + str(hash(password)))
f.close()

print("Tizimga kirish: ")
username = input("Login: ")
password = input("password: ")

f = open("baza.txt", 'r')

login = username in f.readline()
passw = str(hash(password)) in f.readline()

if login and passw:
    print("tizimdan o'tdingiz!")
else:
    print("login yoki parol xato!")