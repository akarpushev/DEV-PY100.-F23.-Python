tuple_ = (1, 2, 3)


def append_to_tuple(local_tuple):
    local_tuple += (4,)  # конкатенация кортежей
    return local_tuple


modified_tuple = append_to_tuple(tuple_)
print(tuple_, modified_tuple)
print(tuple_ is modified_tuple)


list_ = [1, 2, 3]


def append_to_list(local_list):
    local_list += [4] # конкатенация списков
    # действует как метод extend, то есть добавляет элементы к исходному списку
    return local_list


modified_list = append_to_list(list_)
print(list_, modified_list)
print(list_ is modified_list)


list_ = [1, 2, 3]


def clear_append_to_list(local_list):
    local_list = local_list[:] # создание копии списка
    local_list += [4] # конкатенация списков
    return local_list


modified_list = clear_append_to_list(list_)
print(list_, modified_list)
print(list_ is modified_list)


# при объявлении функций в качестве значений для параметров по умолчанию
# не следует использовать изменяемые типы данных (например, списки или словари)
def incorrect_func(name_arg=[]):
    # name_arg является локальной переменной
    print("Аргумент до изменения", name_arg)
    name_arg += [1]
    print("Аргумент после изменения", name_arg)

incorrect_func()
print('-----')
incorrect_func() # при одних и тех же входных данных функция выдает разные результаты


# установим аргумент name_arg пустым а внутри функции будем проверять его
def correct_func(name_arg=None):
    if name_arg is None:
        name_arg = []  # Если пользователь не указал свой список, сделаем новый пустой
    print("Аргумент до изменения", name_arg)
    name_arg += [1]
    print("Аргумент после изменения", name_arg)

# вызовем два раза одну и ту же функцию
correct_func()
print('-----')
correct_func()
print('-----')
correct_func([123])
print('-----')
correct_func(name_arg=[])
print('-----')
correct_func()

"Hello World".lower()  # метод строки lower
str_ = "test"
str_.upper()  # метод строки upper
list_ = [1, 2, 3]
list_.append(4)  # метод списка append
