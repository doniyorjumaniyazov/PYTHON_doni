# print(7, 8, 9)

# n = 5
# print(n)

# n = 'fdsf'
# print(type(n))

# n = 131
#print(type(n))

# n = 'fdnkj\'sf'
# print(n)

# a = 5
# b = 1.32
# c = 'fsdf'

# print(a, b, c)


# a = 5
# b = 1.32
# c = 'fsdf'

# #print(f"{a} - {b} - {c}")   # или по другому нижее показиваем
# print("{} - {} - {}".format(a,b,c))

# print("введите первый строку")


# a = input()
# print(a)

# c = 2.12
# print(c)

# n = int(c)
# print(n)
# d = 5
# d = bool(d)
# print(d)
# print(type(d))



# n = int(input('введите первый число: '))

# m = int(input('введите второй число: '))

# print(n, ' + ', m, '=', n + m)

# a = 2.56854
# b = 6.345111
# print(a*b)

# a = 2.56854
# b = 6.345111
# print(round(a*b, 3)) # чтобы округлит остаток ползуется фу-я (round)

# a = 2.56854
# b = 6.345111
# print(round(a*b, 5))

# a = 1 > 4
# print(a)

# b = 5 > 2 and 3>1
# print(b)

# a = 1 < 5 < 3 > 2
# print(a)

# i = 0
# while (i < 5):
#     # if i == 3:
#     #     break
#      i = i + 1
# else:
#     print('Ну Да')
#     print('Да хватит')
# print(i)

# a = 'qwerty'
# print(a[0]) # это значит выводи букву стояший 0 индексе в строке

# a = 'qwerty'
# for i in a:
#     print(i)

# text = 'да поехали от сюда пока не позно'
# print(len(text))
# text = 'да поехали от сюда пока не позно'
# print(text[:]) # показивает вес текст
# print(text[:3]) # показивает до 3 значени массива не включит третий индекс значение
# print(text[15:])  # показивает с 15 индекса до конца
# print(text[7:-13]) # это все об срезе примеры


# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

# n = int(input())
# i = 1
# result = 1
# while i <= n:
#     result *= i
#     i += 1
# print(result)


# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.  Число фибоначчи это типа 0 1 1 2 3 5 8 13,,, передедуший 2 число следуший сло жение 0+1=1 1+1 =2

# n = int(input())
# n0 = 0
# n1 = 0
# n2 = 1
# i = 2
# while n0 < n:
#     n0 = n1 + n2
#     n1 = n2
#     n2 = n0
#     i += 1
#     if n0 > n:
#         i = -1
# print(i)

# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50

# n = int(input())   #количество дней
# k = 0 # оттопел дней
# max = 0 # tempratura

# for i in range(n):
#     x = int(input())
#     if x > 0:
#         k += 1
#     else:
#         if max < k:
#             max = k
#         k = 0
# print(max)           


#  Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза     

# n = int(input())
# max = -1
# min = 3001

# for i in range(n):
#     x = int(input())
#     if x > max:
#         max = x
#     if x < min:        
#         min = x
        
        
# print(max, min)


# Список
# list_1 = []
# list_1 = list()
# print(list_1)
# list_1 = []
# list_1 = [1, 2, 3]
# print(list_1)

# list_1 = []
# list_1 = [1, 2, 3]
# print(*list_1)     # для убрат [] нужно ставит *

# for i in list_1:
#     print(i)
#     print(len(list_1)) # это для определение длина спискоа
#     print(list_1[2]) # для определеня значение указанный номера элемента

# list = [2, 7]
# print(list)
# list.append(6)       #.append добавление элемента в спике следуюшим
# print(list)

# list = []
# print(list)

# for i in range(6):
#     list.append(i)
#     print(list) # этот код начиная с пустый [] до сначала 0 потом 0, 1 потом ... 0,1,2,3,4,5 шесть штук элементов


# функциия удаление это .pop  примери

# list = [2, 36, -16, 0]
# print(list.pop()) # если один раз удаляет последный элемент в списке это 0
# print(list)
# print(list.pop())
# print(list)
# print(list.pop())
# print(list)

#Удаление конкретного элемента

# list = [2, 36, -16, 0]
# print(list.pop(2)) # функсия удалить конкретного элементо здес второй индек (0 1 2 3)
# print(list)

# для добовление конкретный элемент конкретного позиции тогда исползуется

# list = [2, 55, -18, 1, -26]
# print(list.insert(2,31))  # этот функция добавит 31 месте 2 ого индекса
# print(list)

# Кортеж и свойства ползуется ( ) пара чисел или строк
# t = ()
# print(type(t))

# t = (1)
# print(type(t))

# t = (1, 2,)
# print(type(t))

# v = [1, 2, 3]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d)

# print(d['w'])


# Множнство {} using
 
# colors = {'red', 'white', 'green'}
# print(colors)

# colors.add('red')
# print(colors)

# colors.add('yellow')
# print(colors)
# colors.discard('white') # удаляет выше указанный цвет
# print(colors) 
# colors.clear()
# print(colors)

# a = {1, 2, 6, 3, 11}
# b = {3, 7, 9 , 2, 0}

# c = a.copy()    #копирования а как с будеть
# print(c)
# n = a.union(b) # обединение двухух значение как один
# print(n)

# l = a.intersection(b) # пересечение
# print(l)
# s = a.difference(b) # найдет не стиковку разнмцу здес приоритете cтроке'a' если начинат b.difference(a)
# print(s)

# # Замароженный множества

# f = {2, 0, 6}
# r = frozenset(f)
# print(r)

# создать список состаяший четныйх чисел диапазоне от 1 до 100 сначала обычный вариант потом list comprehinsion 

# list = []
# for i in range(1, 101):
#     list.append(i)
# print(list)
    
# list = [i for i in range(1, 101)]    # это от 1 до 100 подряд
# print(list)
  
# list = [i for i in range(1, 101) if i % 2 ==0]    # это от 1 до 100 подряд но тоько четный чисел
# print(list)  

# list = [(i, i) for i in range(1, 101) if i % 2 ==0]    # это от 1 до 100 подряд но тоько четный чисел еще это кортеж состоявшый из пара чисел
# print(list)  

# list = [i * 2 for i in range(1, 101) if i % 2 ==0]    # это от 1 до 100 подряд но тоько четный можно умножит делить и так далее
# print(list)

# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()


# input_string = "a a a b c a a d c d d"  # Пример ввода
# words = input_string.split()  # Разбиваем строку на слова
# char_count = {}  # Создаем словарь для отслеживания количества встреч каждого символа

# # Проходимся по каждому слову
# for word in words:
#     # Проходимся по каждому символу в слове
#     for char in word:
#         # Обновляем счетчик для текущего символа
#         char_count[char] = char_count.get(char, 0) + 1

# output_string = ""  # Создаем пустую строку для вывода результата

# # Проходимся по каждому слову
# for word in words:
#     # Проходимся по каждому символу в слове
#     for char in word:
#         # Формируем строку вывода, добавляя символ и его количество повторений
#         output_string += char + "_" + str(char_count[char]) + " "
#         # Уменьшаем счетчик повторений для текущего символа
#         char_count[char] -= 1

# # Выводим результат
# print("Output:", output_string.strip())

# следуюший вариант решений
# stroka = input().split()      # функция split() переобразует строку в массив
# result = {}          # kolichstvo povtaryayushiy elementa


# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end = ' ')
#     else:
#         print(i, end = ' ')
#     result[i] = result.get(i, 0) + 1        


# # Пользователь вводит текст(строка). Словом считается # последовательность непробельных символов идущих
# # подряд, слова разделены одним или большим числом# пробелов. Определите, сколько различных слов
# # содержится в этом тексте.
# # Input: She sells sea shells on the sea shore The shells # that she sells are sea shells I'm sure.So if she sells sea
# # shells on the sea shore I'm sure that the shells are sea # shore shells
# # Output: 13

# input_text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

# # Разбиваем текст на слова с помощью пробелов в качестве разделителя
# words = input_text.split()

# # Создаем множество для хранения уникальных слов
# unique_words = set(words)

# # Выводим количество уникальных слов
# print(len(unique_words))


# n = int(input())
# Другой вариант


stroka = input().split()
words = set()
for i in stroka:
    words.add(i.lower())
print(len(words))


# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первымф
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.



numbers = [3, 7, 2, 9, 0, 5, 4]  # Пример входной последовательности


max_value = float('-inf')  # Инициализируем максимальное значение как отрицательную бесконечность

for num in numbers:
    if num == 0:
        break  # Если встретили ноль, выходим из цикла
    if num > max_value:
        max_value = num  # Обновляем максимальное значение, если текущее число больше

print("Максимальное значение в последовательности:", max_value)
1
    