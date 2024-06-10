import zipfile
def crak_password(passwords_list, archiv):
    idx = 0
    with open(passwords_list, "rb") as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    archiv.extractall(pwd=word)
                    print("пароль был найден")
                    print("пароль-", word.decode())
                    return True
                except:
                    print(word.decode(), "не подходит")
                    continue
    return False
passwords_list = "rockyou.txt"

archiv = input("ведите название архива")
obj = zipfile.ZipFile(archiv)

cnt = len(list(open(passwords_list, "rb")))
crak_password(passwords_list, obj)
if crak_password(passwords_list, obj) == False:
    print("в файле", passwords_list, "не найдено необходимого пароля")