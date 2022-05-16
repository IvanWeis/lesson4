"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""
# ОПРЕДЕЛЕНИЯ ПЕРЕМЕННЫХ И ФУНКЦИЙ
remains = 0  # обнуляем остаток денег на счету (глобальная переменная)
kwargs = {}  # в данном словаре храним историю покупок (глобальная переменная)

def top_ap(remains): # определяем функцию пополнения счета
    print("У Вас на счету: ", remains)
    result = remains + int(input("Введите сумму пополнения счета: "))
    print("У Вас на счету: ", result)
    return result

def top_up(remains): # определяем функцию уменьшение счета при покупке
    result = remains - summa  # уменьшаем остаток на сумму покупки
    print("Покупка произведена. Остаток денег на Счете: ", result)
    return result

def purchases_history(): # определяем функцию формирования истории покупок
    kwargs[naimen] = summa  # добавляем строку в историю покупок
    print(kwargs)
    return kwargs # возвращаем изменившуюся историю

# ИСПОЛНЯЕМАЯ ЧАСТЬ ПРОГРАММЫ:
while True:
    print()                        # печатаем пустую строку (для удобства восприятия)
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        remains = top_ap(remains)      # вызываем функцию пополнения счета
    elif choice == '2':
        spisok = input("Введите через пробел Наименование и Сумму покупки: ") # вводим строку из 2-х элементов
        spisok = spisok.split(" ")  # разбиваем строку на 2 элемента массива через пробел
        naimen = spisok[0]  # вытаскиваем первый элемент списка (Наименование)
        summa = int(spisok[1]) # вытаскиваем второй элемент списка (Сумма)
        if remains - summa < 0:  # если остаток на счете меньше суммы покупки
            print("Не хватает денег. Пополните счет")
        else:                    # если денег на счете хватает для осуществления покупки
            remains = top_up(remains)     # уменьшение счета
            kwargs = purchases_history()  # формирование истории покупок
    elif choice == '3':
        print("История Ваших покупок: ")  # вывод истории покупок
        print(kwargs)
    elif choice == '4':
        break                             # выход из программы
    else:
        print('Неверный пункт меню')