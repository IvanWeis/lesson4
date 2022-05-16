"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""

def simple_separator():  # объявляем функцию  simple_separator (рисует 10 звездочек) без параметров
    print ('*' * 10)   # печатаем строку из 10 символов "звездочка" (символ, умноженный на 10)
    return '*' * 10    # для проверки
    """
    Функция создает красивый резделитель из 10-и звездочек (**********)
    :return: **********  # возвращает функции значение (чтобы можно было устроить проверку)
    """
    # pass  # заглушка

print(simple_separator() == '**********')  # True  вызываем функцию simple_separator
# и, если напечатанная строка не сопадает с '**********', то выдается False
# simple_separator()  # просто вызываем функцию simple_separator без параметров


def long_separator(count):  # определяем функцию long_separator (рисует count звездочек) count - параметр
    print ('*' * count)   # печатаем строку из count символов "звездочка" (символ, умноженный на count)
    return '*' * count    # для проверки

    """
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """
    # pass


print(long_separator(3) == '***')  # True вызывем функцию с параметром count равным 3
print(long_separator(4) == '****')  # True вызывем функцию с параметром count равным 4


def separator(simbol, count): # объявляем функцию с двумя параметррами: simbol b count
    print (simbol * count)   # печатаем строку из count символов simbol (simbol, умноженный на count)
    return simbol * count    # для проверки

    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
    # pass


print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True


def hello_world():
    separator('*', 10)
    print('Hello World!')
    separator('#', 10)
    """
    Функция печатает Hello World в формате:
    **********
    Hello World!
    ##########
    :return: None
    """
    # pass


'''
**********
Hello World!
##########
'''
hello_world() # вызываем функцию hello_world


def hello_who(who='World'): # по умолчанию параметр who равен 'World'
    separator('*', 10)
    print(f'Hello {who} !') # применяем форматированный вывод
    separator('#', 10)

    """
    Функция печатает приветствие в красивом формате
    **********
    Hello {who}!
    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    # pass


'''
**********
Hello World!
##########
'''
hello_who()  # вызываем без параметра -> используем значение по умолчанию World
'''
**********
Hello Max!
##########
'''
hello_who('Max') # вызываем с параметром равным Max
'''
**********
Hello Kate!
##########
'''
hello_who('Kate')  # вызываем с параметром равным Kate


def pow_many(power, *args):        # *args - любое количество элементов
    summa = 0                      # обнуляем переменную summa
    for number in args:            # проходим в цикле по массиву args
        summa = summa + number     # в переменной summa накапливаем сумму
        result = summa**power      # переменную summa  возводим в степень power
    return result                  # возвращаем функции значение переменной result

"""
    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    :param power: степень
    :param args: любое количество цифр
    :return: результат вычисления # True -> (1 + 2)**1
"""
    # pass


print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


def print_key_val(**kwargs): # передаем любое количество параметров по имени: имя -> значение в любой последовательности
    for k, v in kwargs.items():  # проходим в цикле
        print(f'{k} --> {v}')    # форматированный вывод

    """
    Функция выводит переданные параметры в фиде key --> value
    key - имя параметра
    value - значение параметра
    :param kwargs: любое количество именованных параметров
    :return: None
    """
   # pass


"""
name --> Max
age --> 21
"""
print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
print_key_val(animal='Cat', is_animal=True)


def my_filter(iterable, function):
    """
    (Усложненое задание со *)
    Функция фильтрует последовательность iterable и возвращает новую
    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
    (примеры ниже)
    :param iterable: входаня последовательности
    :param function: функция фильтрации
    :return: новая отфильтрованная последовательность
    """
    pass


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True