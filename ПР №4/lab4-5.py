n_soldier = int(input("Введите количество призывников:"))

from prettytable import PrettyTable
table_s = PrettyTable()

table_s.field_names = ["Номер призывника", "Фамилия", "Имя", "Отчество", "Год рождения", "Заболевание"]
for i in range(1, n_soldier + 1):
    surname={}
    name = {}
    patronymic = {}
    birthday = {}
    ill = {}

    surname["Фамилия"] = input("Введите фамилию:")
    name["Имя"] = input("Введите имя:")
    patronymic["Отчество"] = input("Введите отчество:")
    birthday["Год рождения"] = input("Введите год рождения:")
    ill["Заболевание"] = input("Введите заболевание:")

    table_s.add_row([i, surname["Фамилия"], name["Имя"], patronymic["Отчество"], birthday["Год рождения"], ill["Заболевание"] ])
    print(table_s)