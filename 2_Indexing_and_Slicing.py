# Индексируемые последовательности (sequence)
# Строки (str)
# Списки (list)
# Кортежи (tuple)

list_ = ["а", "б", "в", "г", "д"]  # список строк
print(list_[0])  # "а"
print(list_[4])  # "д"
list_[0] = "А"
print(list_)  # ['А', 'б', 'в', 'г', 'д']
print(list_.index("А")) # 0

str_ = "Hello, World"
print(str_[-1])  # отрицательная индексация для получения элементов с конца последовательности
print(str_[-5])


# Срезы или слайсирование
list_ = ["а", "б", "в", "г", "д"]
print(list_[1:4]) # не включая 4-ый
print(list_[:4])
print(list_[1:])
print(list_[:])
print(list_[:-1])
print(list_[::-1])

list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл"]
# индекс середины
middle_index = len(list_players) // 2  # 2

left_team = list_players[:middle_index]  # list_players[:2]
right_team = list_players[middle_index:]  # list_players[2:]

print(left_team)
print(right_team)
