# Объект является хешируемым, если от него работает встроенная функция hash.

# Большинство неизменяемых типов в Python (int, float, str, bool, и т.д.) – хешируемые.

# Неизменяемые коллекции, например tuple, являются хешируемыми, если хешируемы все их элементы.

print(hash("sdkfjsdkjfnksjdnfkjsdnfkjsndfkjsndfkjsndfkjsnd"))
print(hash("sdkfjsdkjfnksjdnfkjsdnfk"))

set_1 = (2, 'Hello World', 1)
set_2 = (2, 'Hello World', [1])
print(hash(set_1))
# print(hash(set_2)) # TypeError: unhashable type: 'list'

print(set_1.__hash__())
print(set_1.__hash__().bit_length())
print(set_1.__hash__().bit_count())
