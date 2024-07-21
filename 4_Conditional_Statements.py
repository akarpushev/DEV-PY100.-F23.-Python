some_var = None
other_var = None

print(some_var is other_var)  # True
print(some_var == other_var) # True
#print(some_var in other_var)

str_ = "Строка с цифрой 1"

is_substr = "Строка" in str_  # True
print("В строке есть слово Строка?", is_substr)
print('1' in str_)
print('1' == str_)
print(is_substr is str_)

# ==: Проверяет равенство значений двух объектов.
# Например, 1 == 1 возвращает True, потому что значения равны.

# is: Проверяет, являются ли два объекта одним и тем же объектом в памяти.
# Например, a is b вернет True, если a и b указывают на один и тот же объект.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)  # True: значения равны
print(a is b)  # True: это один и тот же объект
print(a == c)  # True: значения равны
print(a is c)  # False: это разные объекты в памяти

number = 12

condition_1 = number % 2 == 0  # число кратно 2
condition_2 = number % 3 == 0  # число кратно 3

if condition_1 and condition_2: # if not condition_1 and condition_2:
    print('Число кратно 2 и 3')
else:
    print('Число не (кратно 2 и 3)')

year = [n for n in range(1, 13)]

str_1 = 'test'
str_2 = "test"
str_3 = '''test'''
str_4 = """test"""

print(str_1 == str_2 == str_3 == str_4)
print(
    (str_1 == str_2)
    and (str_2 == str_3)
    and (str_3 == str_4)
)

hour = 7

bad_condition = (6 <= hour) and (hour < 12)  # Плохая запись условия
good_condition = 6 <= hour < 12  # цепочки операторов всегда соединяются через AND
if good_condition:
    print("Утро!!!")

# Приоритет логических операторов:

# Первая очередь
# in, not in - Проверка принадлежности
# is, is not - Проверка тождественности
# < - Меньше — условие верно, если первый операнд меньше второго.
# > - Больше — условие верно, если первый операнд больше второго.
# <= - Меньше или равно.
# >= - Больше или равно.
# == - Равенство. Условие верно, если два операнда равны.
# != - Неравенство. Условие верно, если два операнда неравны.

# Вторая очередь
# not x - логическое "НЕ" или отрицание

# Третья очередь
# and - логическое "И" или "умножение"

# Четвертая очередь
# or - логическое "ИЛИ" или "сложение"

# Посчитаем пример
example = (2 > 3) and (2 < 2) or (1 != 5) and (not (5 < 3) or (3 == 1))

my_result = False and False or True and (not False or False)
my_result = False and False or True and (True or False)
my_result = (False and False) or (True and True)
my_result = False or True
my_result = True

print(example)
print(my_result)
print(example == my_result)

# В логике оператор or (или) возвращает True, если хотя бы одно из его операндов истинно.
# Вот почему True or False это True.
# Порядок операций
# Скобки: Сначала выполняются операции в скобках.
# not: Затем выполняется оператор not.
# and: Оператор and выполняется до оператора or.
# or: Оператор or выполняется последним.

list_ = [5, 6, 7, 8, 9]

result = 4 and 8 in list_ # Входят ли в список [5, 6, 7, 8, 9] числа 4 и 8?
print(result, '!')
result = (4 in list_) and (8 in list_)
print(result, '!!')

print(False and True) # Оператор and возвращает True только в том случае, если оба операнда истинны.
                      # В противном случае он возвращает False.
print(False or True)

print(bool(0))  # False
print(bool(1))  # True
print(bool(0.0))  # False
print(bool(1.0))  # True
print(bool("")) # False
print(bool("1"))  # True
print(bool([])) # False
print(bool([1]))  # True
print(bool({})) # False
print(bool({1: 22}))  # True

condition = ...  # True / False / None
if condition:
    print("True!!!")
else:
    print("False or None")

condition = ...  # True / False / None
if condition is None:
    print("None")
else:
    print("True or False!!!")

# # Плохо
# if password == "":
#    print("Вы забыли ввести пароль")
# else:
#    ...
#
# # Очень плохо
# if len(password) == 0:
#    print("Вы забыли ввести пароль")
# else:
#    ...
#
# # Хорошо
# if not password:
#    print("Вы забыли ввести пароль")
# else:
#    ...

number = 14
condition_1 = number % 2 == 0  # число кратно 2
condition_2 = number % 3 == 0  # число кратно 3

if condition_1 and condition_2:
    print('Число кратно 2 или 3')
elif condition_1:
    print('Число кратно 2')
elif condition_2:
    print('Число кратно 3')
else:
    print('Число не кратно 2 или 3')

num = 10

if num % 2 == 0:
    num_desc = "четное"
else:
    num_desc = "нечетное"

print("Число", num, num_desc)

num = 10
num_desc = "четное" if num % 2 == 0 else "нечетное"

print("Число", num, num_desc)
