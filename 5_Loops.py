heights_list = [132, 176, 154, 182, 168]
# height = 0
# for i in range(len(heights_list)):
#     if heights_list[i] > height:
#         height = heights_list[i]
#         number = i+1
#
# print(height, number)

max_height = heights_list[0]  # пусть рост первого человека будет самым высоким

for current_height in heights_list:  # перебираем каждый рост
    if current_height > max_height:  # если текущий рост больше того, который встречали ранее
        max_height = current_height  # то перезаписываем максимальный рост

print("Рост самого высокого челокека:", max_height)

print(max(heights_list))

stop = 10  # конец
range_ = range(stop)

print("левая граница", min(range_))  # левая граница по умолчанию 0
print("правая граница", max(range_))  # правая граница у range невключительно
print("количество элементов", len(range_))  # количество элементов 10

start = 5  # начало
stop = 20  # конец

print(list(range(start, stop + 1)))  # stop + 1 чтобы правая граница была включительно

start = 5  # начало
stop = 20  # конец
step = 2  # шаг

print(sum(range(start, stop + 1, step)))  # сумма всех нечетных чисел от 5 до 20 включительно

count_stairs = 4  # количество ступеней

for i in range(count_stairs):  # 0, 1, 2, 3
    print("*" * (i + 1))

for i in range(1, count_stairs + 1):  # 1, 2, 3, 4
    print("*" * i)

# list_students = ["Маша", "Петя", "Саша", "Кирилл", "Оля"]
# heights_lists_tudents = [132, 176, 154, 182, 168]
# max_height_student = heights_lists_tudents[0]
#
# for i in range(len(heights_lists_tudents)):
#     current_height_student = heights_lists_tudents[i]
#     current_index = i
#     if max_height_student < current_height_student:
#         max_height_student = current_height_student
#         max_index = current_index
#         student = {list_students[max_index]: current_height_student}
#
# print(student)

list_students = ["Маша", "Петя", "Саша", "Кирилл", "Оля"]
heights_list = [132, 176, 154, 182, 168]

max_index = 0
for i in range(len(heights_list)):  # перебераем все индексы
    max_height = heights_list[max_index]
    current_height = heights_list[i]
    if current_height > max_height:  # если текущий рост больше того, который встречали ранее
        max_index = i  # то перезаписываем индекс максимального роста

print("Самый высокий человек -", list_students[max_index])
print("Его рост =", heights_list[max_index])

list_ = ["а", "б", "в"]
for i in range(len(list_)):
    print((i, list_[i]))

for i in enumerate(["а", "б", "в"]):
    print(i)

for index, value in enumerate(["а", "б", "в"]):
    print("Индекс:", index, "->", "Значение:", value)

for pos, value in enumerate(["а", "б", "в"], start=1):  # start по умолчанию равен 0
    print("Позиция:", pos, "->", "Значение:", value)

list_students = ["Маша", "Петя", "Саша", "Кирилл", "Оля"]
heights_list = [132, 176, 154, 182, 168]

max_index = 0
#max_height = heights_list[max_index]

for i, current_height in enumerate(heights_list):  # перебераем пары индекс - значение
    max_height = heights_list[max_index]
    if current_height > max_height:  # если текущий рост больше того, который встречали ранее
        max_index = i  # то перезаписываем индекс максимального роста
        max_height = heights_list[max_index]  # и перезаписываем рост

print("Самый высокий человек -", list_students[max_index])
print("Его рост =", max_height)

sum_ = 0
input_number = int(input("Введите число: "))

while input_number != 0:
    sum_ += input_number
    input_number = int(input("Введите число: "))

print("Ответ:", sum_)

sum_ = 0

while True:
    input_number = int(input("Введите число: "))
    if input_number == 0:
        break

    sum_ += input_number

print("Ответ:", sum_)
