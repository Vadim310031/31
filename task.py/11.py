print("Программа запущена")
n = int(input("Введите свой возраст: "))
if n > 0:
    if n <= 13:
        print("Вам подходит фильм №1")
    elif n <= 17:
        print("Вам подходит фильм №2")
    else:
        print("Вам подходит фильм №3")
else:
    print("Вы ввели некорректный возраст")
print("Конец программы")