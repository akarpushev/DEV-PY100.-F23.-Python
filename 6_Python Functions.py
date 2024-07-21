# list_ = [1, 2, 3, 4, 5]
# a = list_[len(list_) // 3]
#
# for b in range(len(list_)):
#     if list_[b] < a:
#         a = list_[b]
#
# print(a)


def min_(list_):
    a = list_[len(list_) // 3]

    for b in range(len(list_)):
        if list_[b] < a:
            a = list_[b]

    return a


list_ = [-1, 0, 1, 2, 3, 4, 5]
min_(list_)
print(min_(list_))

# Принцип DRY (Don't Repeat Yourself)
# Вместо этого кода
list_1 = [1, 2, 3]
list_2 = [6, 5, 4]

min_1 = list_1[0]
for value in list_1:
    if value < min_1:
        min_1 = value

min_2 = list_2[0]
for value in list_2:
    if value < min_2:
        min_2 = value

result = min_1 + min_2
print(result)


# Надо этот код
def min_(list_):
    min_value = list_[0]
    for value in list_:
        if value < min_value:
            min_value = value

    return min_value


list_1 = [1, 2, 3]
list_2 = [6, 5, 4]
result = min_(list_1) + min_(list_2)
print(result)


# пример простейшей функции
def empty_func():
    pass  # pass можно заменить на ...


result = empty_func()  # но даже такая функция всё равно возвращает результат None
print(result)  # None


def return_tuple_with_values():
    return 1, 2, 3  # по умолчанию python возвращает кортеж


result = return_tuple_with_values()
print(type(result), result)  # <class 'tuple'> (1, 2, 3)
a, b, c = return_tuple_with_values()  # множественная распаковка значений
print(a, b, c)
result = return_tuple_with_values()
a, c = result[0], result[-1]  # взять из результата первое и последнее значение
print(a, c)
a, _, c = return_tuple_with_values()
print(a, c)


def multi_return():
    first_number = ...
    second_number = ...
    if first_number > second_number:
        return "первое число больше"
    elif first_number < second_number:
        return "второе число больше"
    else:
        return "числа равны"


def add_func(a, b):
    add = a + b
    return add


# при указании наименования переменных их порядок не важен
print(add_func(b=4, a=3))  # add_func(a, b) -> a = 3, b = 4
# часть аргументов можно оставить позиционными, а часть именованными
print(add_func(6, b=10))
# Нельзя чтобы позиционные аргументы следовали за именованными:


def pow_func(base, pow_=2):
    return base ** pow_


print(pow_func(4))  # по умолчанию возводим число в степень два
print(pow_func(3, pow_=3))  # переопределяем аргумент по умолчанию
print(pow_func(5))  # опять по умолчанию возводим число в степень два
print(pow_func(2, 5))  # используем позиционные аргументы
print(pow_func(pow_=2, base=8))  # используем именованные аргументы

print(help(print))
print(1, 2, 3, "_")  # "_" будет воспринято как символ для печати
print(1, 2, 3, sep="_")  # "_" будет воспринято как разделить между значениями
print(1, 2, 3, end=" | ")  # указали своё значение, которое будет добавлено в конец
print(3, 2, 1)


# Порядок вызова функций
def main():
    # что-то выполняем
    sub_func()  # вызов функции которая объявлена дальше
    # что-то выполняем


def sub_func():
    ...


main()


# Локальная и глобальная переменная
a = 5  # глобальная переменная


def func():
    a = 1  # локальная переменная


func()
print(a)

GLOBAL_VAR = 15  # глобальная переменная


def func():
    print(GLOBAL_VAR)


func()


global_var = 88  # глобальная переменная


def func():
    print(global_var)
    # global_var = 99
    print("Локальная переменная: ", global_var)


func()


global_var1 = 188  # глобальная переменная


def func():
    global_var1 = 99  # global_var локальная переменная, хоть названия и совпадают
    print("Локальная переменная: ", global_var1)


func()
print(global_var1)

CONST_VAR = 99  # глобальная переменная


def func(local_var):
    local_result = CONST_VAR + local_var
    return local_result


# первый вызов функции с аргументом 1
CONST_VAR = func(1)
print(CONST_VAR)

# второй вызов функции с аргументом 1
print(func(1))


global_var3 = 288  # глобальная переменная


def func():
    global global_var3  # переменная global_var не локальная, а ссылается на глобальную
    global_var3 = global_var3 + 1  # изменяю глобальную переменную

func()
print(global_var3)
# Не нужно менять значение глобальных # переменных внутри функции!!!


global_var4 = 388  # глобальная переменная

def func(local_var):
    return local_var + 1  # изменяю локальную переменную

global_var4 = func(global_var4)
print(global_var4)  # 389
