yearofbirth = int(input("Введите год рождения А.С.Пушкина от Р.Х.: "))
dayofbirth = "6 июня"

if yearofbirth == 1799:
    print("Верно!")
    dayofbirth = input("А теперь введи его день Рождения: ")
    if dayofbirth == "6 июня":
        print("Верно!")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год рождения")
