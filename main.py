# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
print("Задание №1")
s1 = (1, "string", [1,2,3], 18.88)
print(list(map(type, s1)))


# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print("Задание №2")
input_string = input("Enter list separated by space ")

s1 = input_string.split()
s2 = []

# even
if len(s1) % 2 == 0:
    length = len(s1)
# odd
else:
    length = len(s1) - 1

for i in range(0, length, 2):
    s2.append(s1[i+1])
    s2.append(s1[i])

if len(s1) % 2 != 0:
    s2.append(s1[-1])

print(s2)

#print("Задание №2.2")
#s1 = input("Enter comma separated list: ")
#s2 = []
# even
#if len(s1) % 2 == 0:
#    length = len(s1)
# odd
#else:
#    length = len(s1) - 1
#
#
#for i in range(0, length, 2):
#    s2.append(s1[i+1])
#    s2.append(s1[i])
#
#if len(s1) % 2 != 0:
#   s2.append(s1[-1])
#
#print(s2)


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
print("Задание №3.1")
month = int(input("Введите номер месяца: "))

if month == 12 or (month > 0 and month < 3):
    print('Зима')
elif month > 2 and month < 6:
    print('Весна')
elif month > 5 and month < 9:
    print('Лето')
elif month > 8 and month < 12:
    print('Осень')
else:
    print('Такого месяца не существует')

print("Задание №3.2")
month = input("Введите номер месяца: ")
months_dict = {'1': 'Зима', '2': 'Зима', '12': 'Зима', '3': 'Весна', '4': 'Весна', '5': 'Весна', '6': 'Лето', '7': 'Лето', '8': 'Лето', '9': 'Осень', '10': 'Осень', '11': 'Осень'}
print(months_dict.get(month, "Такого месяца не бывает"))


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
print("Задание №4.1")
s = "Asya says hello"

list_strings = s.split(" ")

# print(list_strings)

# l = 2
l = len(list_strings)
r = range(l)


for i in r:
    print(str(i + 1) + " " + list_strings[i])

print("Задание №4.2")
s = "Hello world! Here I am"

list_strings = s.split(" ")

for i in range(len(list_strings)):
    print(str(i + 1) + " " + list_strings[i])
 #   for i in range(len(list_strings)):
 #       print()


# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
print("Задание №5")
number_2 = int(input("Введите число: "))
number_list = [7, 4, 3, 2]
c = number_list.count(number_2)
for element in number_list:
    if c > 0:
        i = number_list.index(number_2)
        number_list.insert(i+c, number_2)
        break
    else:
        if number_2 > element:
            j = number_list.index(element)
            number_list.insert(j, number_2)
            break
        elif number_2 < number_list[len(number_list) - 1]:
            number_list.append(number_2)
print(number_list)