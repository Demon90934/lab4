"""
МНОЖЕСТВО в Python -  это структура данных, содержащая не повторяющиеся элементы в случайном порядке.
"""
a = set()  # Создание пустого множества
a.add(1)  # Добавление элемента в множество
a.add(2)
a.add(1)
print(a)  # вывелось два числа 1 и 2, несмотря на то, что мы дважды добавили 1 (строки 5 и 7)
b = set('hello')  # Преобразование строки в множество
print(b)  # выводятся буквы в случайном порядке, буква "l" выводится 1 раз


"""
Множества удобно использовать для удаления повторяющихся элементов из списка
"""
a = ['aa', 'ab', 'aa', 'ba']
print(set(a))
"""
Множества поддерживают стандартные операции других структур данных - len, in, clear и т.п. 
"""
# Вставьте пропущенную строку, чтобы оператор print выводил True
b = ['aa', 'ab', 'aa', 'ba']
b = set(b)
print(len(b) == 3)


"""
Помимо базовых операций, множества в Python поддерживают операции математических множеств (объединение(union), пересечение(intersection))
"""
a = {1, 2, 3, 4}  # Создание множества
b = {3, 4, 5, 6}
c = a.union(b)  # Объединение множества
print(c)
# Вставьте пропущенное действие, чтобы в консоль вывелось пересечение множеств a и b
d = a.intersection(b)
print(d)