# firstnum = int(input())
# secondnum = int(input())
# if firstnum > secondnum:
#     max = firstnum
# else:
#     max = secondnum
# print(max)

# n = int(input())
# m = int(input())
# k = int(input())
# desk1 = (n+1)//2
# desk2 = (m+1)//2    
# desk3 = (k+1)//2
# summa = desk1 + desk2 + desk3
# print(summa)    


# a = 3
# b = 2
# # c = 4
# # a = int(input())
# # b = int(input())
# # c = int(input())        
# # if (a * b >= c) and ((c % a == 0) or (c % b == 0)):
# #     print("yes")
# # else:
# #     print("no")

# # Дан список чисел. Определите, сколько в нем встречается различных чисел.Input: [1, 1, 2, 0, -1, 3, 4, 4]

# # list1 = [1, 1, 2, 0, -1, 3, 4, 4, 8, 11, 0]
# # list2 = []
# # count = 0
# # for i in list1:
# #     if i not in list2:
# #         list2.append(i)
# #         count +=1
           
# # print(count) 
   
# # digit = [1, 1, 2, 0, -1, 3, 4, 4]
# # digit1 = []
# # digit1 = set(digit)
# # count_digit = len(digit1)
# # print(len(digit1))
# # print(count_digit)

# # Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# # (сдвиг - циклический) на K элементов вправо, K –положительное число.Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

# # list = [1, 2, 3, 4, 5]
# # k = 3
# # k = k % len(list)
# # first_p = list[k:]
# # second_p = list[:k]
# # list_new = list[k:] + list[:k]
# # print(list_new)

# # Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# # Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

# # Пример:


# # list_1 = [1, 2, 3, 4, 7]
# # k = 6
# # close_num = list_1[0]
# # min_dif = abs(k - list_1[0])
# # for i in list_1:
# #     current_dif = abs(k - i)
# #     if current_dif < min_dif:
# #         min_dif = current_dif
# #         close_num = i
# # print(close_num)

# # В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# # В случае с английским алфавитом очки распределяются так:

# english_scores = {
#     'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#     'D': 2, 'G': 2,
#     'B': 3, 'C': 3, 'M': 3, 'P': 3,
#     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#     'K': 5,
#     'J': 8, 'X': 8,
#     'Q': 10, 'Z': 10
# }
# russian_scores = {
#     'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#     'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#     'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#     'Й': 4, 'Ы': 4,
#     'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#     'Ш': 8, 'Э': 8, 'Ю': 8,
#     'Ф': 10, 'Щ': 10, 'Ъ': 10
# }
# # Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# # Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# # Пример:


# k = 'БОКА'
# # 12
# language = 'english' and 'russian'
# count = 0
# for i in k:
#     if language == 'english':
#         count += english_scores[i]
#     else:
#         count += russian_scores[i]    
   
# print(count)
       
#  Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2      


# stroka = "a a a b c a a d c d d"
# stroka_1 = stroka.split()      # функция split() переобразует строку в массив
# result = {}          # kolichstvo povtaryayushiy elementa


# for i in stroka_1:
#     if i in result:
#         print(f'{i}_{result[i]}', end = ' ')
#     else:
#         print(i, end = ' ')
#     result[i] = result.get(i, 0) + 1 

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# stroka = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# words = stroka.split()
# unique_words = set(words)
# print(len(unique_words))

# или
# stroka_1 = stroka.split()
# words = set(stroka_1)
# for i in stroka_1:
#     words.add(i.lower())
# print(len(words))

# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# n, m = map(int, var1.split())
# set1 = set(map(int, var2.split()))
# set2 = set(map(int, var3.split()))

# intersection = sorted(set1.intersection(set2))

# print(*intersection)

# В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих
# модулей.# Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится
# перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.
# Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать 
# один собирающий модуль за один заход, находясь перед некоторым кустом грядки.

# Входные данные:

# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка 
# не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, 
# находясь перед некоторым кустом грядки.

# pupil_rating = [1, 2, 3, 4, 4, 3]
# pupil_rating_1 = []
# max_n = max(pupil_rating)
# min_n = min(pupil_rating)
# for i in pupil_rating:
#     if pupil_rating[i] == max_n:
#         pupil_rating[i] = min_n
#     pupil_rating_1.append(pupil_rating[i])
# print(pupil_rating_1)

# def simple_number(n):
#     if n % 2 ==0:
#         True
# print(simple_number(10))

# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

# def find_indices_in_range(list_1, min_number, max_number):
#     indices = []
#     for i, num in enumerate(list_1):
#         if min_number <= num <= max_number:
#             indices.append(i)
#     return indices

# result_indices = find_indices_in_range(list_1, min_number, max_number)
# print(*result_indices, sep='\n')


# другой вариант

# indices = []
# for index in range(len(list_1)):
#     value = list_1[index]
    
#     if min_number <= value <= max_number:
#         indices.append(index)
# print(*indices, sep='\n') 
         
# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , разность d и количество элементов 
# n будет задано автоматически. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Пример

# На входе:


# a1 = 2
# d = 3
# n = 4  
# def arf_progres(a1, d, n):
#     progres = []
#     for i in range(n):
#         progres.append(a1 + i* d)
#     return progres  
               
# progres = arf_progres(2, 3, 4)
# for num in progres:
#     print(num)
  

# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. По умолчанию номер столбца и строки = 9.

# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

# Пример

# На входе:

def print_operation_table(operation, num_rows=9, num_columns=9):
    if num_rows <= 2 or num_columns <= 2:
        print('Ошибка')
        return
    for i in range(1, num_rows + 1):
        row = []
        for j in range(1, num_columns + 1):
            row.append(str(operation(i, j)))
        print(" ".join(row))
   



print_operation_table(lambda x, y: x * y, 4, 4)
print_operation_table(lambda x, y: x * y, 2, 5)

        





            


    

    



     