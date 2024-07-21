# Неизменяемые типы данных bool, int, float, tuple, str, frozenset
from unicodedata import decimal

x = 10
print(x, type(x), id(x))

x = 3.456
#x[1] = 4 # TypeError: 'float' object does not support item assignment
print(x, type(x), id(x))

x = 'Прювет!'
#x[2] = 'и' # TypeError: 'str' object does not support item assignment
# x = 'Привет!'
# print(x[2] == 'и')

tuple = (1, 2, 3, 4)
print(tuple, type(tuple), id(tuple))

#----------------------------------------------------------------------------------------------------

a = 123456
b = a

print("Переменные a и b это одно и то же?")
print(a is b)  # True
print(a, b)

a = a + 1  # изменим перемменную a
print("А теперь переменные a и b это одно и то же?")
print(a is b)  # False
print(a, b)  # 123457 123456

#----------------------------------------------------------------------------------------------------

# Изменяемые типы данных list, set, dict

x = ['Яблоко', 'Груша', 'Слива']
x[1] = 'Ананас'
print(x)
x = y =  ['Яблоко', 'Груша', 'Слива']
print(x is y)   # True
print(id(x), id(y), id(x) == id(y)) # (3240602862208, 3240602862208, True)
x.append('Персик')
print(x)   # ['Яблоко', 'Груша', 'Слива', 'Персик']

dict = {'Name':'Алиса', 'Age':27, 'Job':'Senior Python Developer'}
dict['Name'] = 'Роберт'
print(dict)   # {'Name': 'Роберт', 'Age': 27, 'Job': 'Senior Python Developer'}

tuple1 = ([1, 1], 2, 3)
list1 = [(1, 1), 2, 3]
tuple1[0][0] = 'Поменялся'
print(tuple1) # (['Поменялся', 1], 2, 3)
# list1[0][0] = 'Поменялся'
# print(list1) # TypeError: 'tuple' object does not support item assignment

#----------------------------------------------------------------------------------------------------

list_1 = ["а", "б", "в"]
list_2 = list_1

print("Переменные list_1 и list_2 это одно и то же?")
print(list_1 is list_2)  # True
print(list_1, list_2)

list_1[0] = "новое значение"
print("Переменные list_1 и list_2 это одно и то же?")
print(list_1 is list_2)  # True
print(list_1, list_2)

#----------------------------------------------------------------------------------------------------

float_ = 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1
print(float_)
#round(number[, ndigits=0])
num = 1.2344323
num = round(num, 3)
print(num)

# строкам не важно записаны они одинарными или двойными кавычками
str_ = "Hello" + 'World'  # конкатенация строк
print(str_)
print("z" * 25)  # клонирование строки

print([1, 2, 3] + [3, 2, 1]) # Списки можно складывать
print([0] * 5) # Списки можно умножать

print((1, 2, 3) + (3, 2, 1))

empty_tuple = ()  # пустой кортеж
a, b = 1, 2  # правильно
print(a, b)
tuple_vars = 1, 2  # тоже правильно, есть одно "но", значения будут помещены в кортеж
print(tuple_vars, type(tuple_vars))

grades = [4, 5, 4, 5, 5, 5, 3]  # список оценок
mean_grade = sum(grades) / len(grades)  # средняя оценка
print("Средняя оценка за первое домашнее задание,", round(mean_grade, 2))

set_1 = {1, 2, 'Hello World', ...}
print(set_1)
empty_set = set()
set_2 = {3, 2, 3, 3, 2, 1}
print(set_2, type(set_2))  # {1, 2, 3} <class 'set'>
print({2, 'Hello World', 1})
