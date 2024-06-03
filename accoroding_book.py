# str  = input("hello world!,'this is not main rule i it'") # "" '' gjkpetncz lkz cnhjrb yj "" ,jktt njxtxtysq
# print(str.title())

# name = "MY Angel"
# print(name.title()) # сделает болшым первый букв каждый слов
# print(name.upper()) # переобразует все буков болши
# print(name.lower()) # наоборот

# first_name = "Doniyor"
# sure_name = "Jumaniyazov"
# full_name = first_name + " " + sure_name  # + обединает строки канкатация
# print(full_name)
# print("Hello " + full_name.upper() + " ! ")
# print("Hello " + full_name.lower() + " ! ")

# print("cashback")
# print("\tcashback \n \tbar \ncafe")   # \t типа пробел \т делает из строчный столбецев
# fav_language = " c+ ! "
# print(fav_language)
# print(fav_language.rstrip())  # rstrip() удаляет конечный отступи 
# print(fav_language.lstrip())  # наоборот
# print(2 + 3)
# print(6 * 5)
# print(40 / 15)
# print(0.2 + 0.3)
# print(2 * 0.3)      
   
#import this    
# список
# list_1 = [2, 3, 4, 5, 6]
# list_2 = []

# for i in list_1:
#     if i % 2 == 0:
#         list_2.append(i)  # чтробы создат или пополнит внутри новый список при условия вот так делается     
    
# print(list_2)
# names = ['asa', '22', 'dda', 'a1a1a', 'xzx']    
# lists = "my build " + names[2] + " hello"
# print(names[2], names[0])  # можно с помошю номера индекса показат значение
# print(names[4].upper())
# print(names[-2]) # показивает перед последный элемент


# print(lists)
# cars = ['bmw', 'malibu', 'tico']
# print(cars)
# cars[0] = 'damas' # изменение значение списка местами индекса
# print(cars)
# cars[1] = 'audi'
# print(cars)
# cars.append('hongi') # добавление новый значение
# print(cars)
# cars.insert(0, 'byd') # это означает добавление новые значение указанные индекса при этом не удалят и не потеряв сушуствуюший значение insert() добавляет новый место
# print(cars) 
#del cars[0]  # удаляет указенний индексе значение
# pop_cars = cars.pop() # pop() удаляет указаный элемент и показивет этот элемент
# print(cars)
# print(pop_cars)
# pop_cars = cars.pop()
# print(cars)
# print(pop_cars)
# pop_cars = cars.pop()
# print(cars)
# print(pop_cars)
# print(cars.pop(1))
# cars.remove('malibu') # если мы не знаем индекс поисковаемое нами значение можно написат имя значение которого мы ходели удалить
# print(cars)


# gosts = ['abba', 'adda', 'assa']
# print(gosts)
# print(gosts.pop(2))
# gosts.insert(0, 'alla')
# print(gosts)
# gosts.insert(3, 'agga')
# print(gosts)
# gosts.append('appa')
# print(gosts)
# gosts.pop()
# print(gosts)
# gosts.pop()
# print(gosts)
# del gosts[2]
# del gosts[0]
# print(*gosts)

# students = ['abba', 'affa', 'gabba', 'zazaz', 'diba']
# print(students)
# # # students.sort() # просто сортируют по алфавите
# # # print(students)
# # students.sort(reverse=True) # сортирует обрптном порядке
# # # # print(students)
# # # print(students)
# # # print(sorted(students)) # временно изменит порядок но исходный данные не потеряется
# # # print(students)
# # print(students)
# # print(students.reverse()) # согласно исходного списка обратный порядок (а не сортированные)
# print(len(students))

# # countries = ['Kongo', 'Uzbekistan', 'Russia', 'USA', 'China']
# # # print(countries)
# # # print(sorted(countries))
# # # print(countries)
# # # countries.reverse()
# # # print(countries)
# # # print(len(countries)) # дина списка именно колко значенеие находится в списке
# # for name in countries: # этот цикл выводит по каждосу элемента списка и выводит экран
# #      print(name.title() + " good place" + ".")
# #     print(name.title())
# # print(type(countries))

# # pizza = ['peperoni', 'lobo', 'sweet']
# # for i in pizza:
# #      print("I like " + i + ".") # введенный слови добавляется каждий i элементы
# # for numbers in range(1, 6):
# #      print(numbers)
# # numbers = list(range(1, 5))
# # print(numbers)

# # list_1 = list(range(1,10,3))  # это означает от 1 начинает слдеуший 3 шаг до окончание(последный элемент не включает) (1, 4, 7)
# # # print(list_1)
# # squares = []
# # for num in range(1,11):
# #      unknown = num**2 # kvadratniy znachenie
# #      squares.append(unknown)
# # print(squares)
# # декоратиры делают кода более понятным
# from time import time 

# def decor(func):
#      def wrapper(*args, **kwargs):
#           sum_time = 0
#           for _ in range(1000000):
#                t1 = time()
#                res = func(*args, **kwargs)
#                t2 = time()
#                sum_time += t2 - t1
#           return res, sum_time    
                         
#      return wrapper       # от начали до здес потом обязателно указат @decor и потом функции это показавает оберавание а именно сколко время потратит наш код для решение для любой функции подоедет

# @decor
# def power(i, j):
#      return i ** j
# print(power(10, 3))

# @decor     
# def find_sum(a, b, c):
#      return a + b + c
# print(find_sum(3, 4, 5))

# функция min() и max() определяет минималный и максималный число в списке min(list)

# list = []

# for i in range(1, 20):
#       list.append(i)
# print(list)
# # sum = (list[0] + list[len(list) - 1]) / 2 * len(list)
# # print(sum)
# print(min(list))
# print(max(list))
# print(sum(list))
# list_1 = list(range(1,20,2))
# print(list_1)

# Тройки: создайте список чисел, кратных 3, в диапазоне от 3 до 30. Выведите все числа
# своего списка в цикле for.
# list = []
# for i in range(3,31):
#      if i % 3 == 0:
#           list.append(i)
# # print(list)
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("these are my team")
# for player in players[2:4]:
#      print(player)

# cars = ['bmw', 'mers', 'audi']
# for car in cars:
#      if car == 'bmw':
#           print(car.upper())
#      else:
#           print(car)

# car = 'audi'
# if car != 'audi':
#     print(False)
# else:
#     print(True)
# age = int(input("first: "))
# age_1 = int(input("second:"))
# if age < 15 and age_1 < 15:
#      print('ok')
# else:
#   False      
# значение in проверяет естли внутри списка какой то элемент

# list = ['abba', 'acca', 'adda']
# if 'abba' in list:
#      print('ok')
# else:
#      list.append('abba')
#      print(list)     
   
# users = ['a', 'b', 'c', 'd'] 
# user = 'm'
# if user not in users:
#      print('good guy')
# else:  
#      print('bad guy')         

     
# age = int(input("age please: "))
# if age <= 5:
#      print('1$ for ticket')
# elif age > 5 and age < 10:
#      print('2$ for ticket')
# else:
#      print('3$ for ticket')

# alien_color = ['red', 'black', 'green']
# color = str(input(" please: "))
# if color == 'red':
#         print('you get 5 point')
# elif color == 'balck':
#         print('you get 20 point')
# else:
#         color == 'green'
#         print('you get 15 point')

# словары исползуется {} cловары хранит у себе ключ-значение то есть когда показиваем ключ указивает значение когда указиваем ключ ползуемся[]
# samiy_0 = {'age': 9, 'color eyes': 'black', 'surename': 'rustamov'}
# print(samiy_0['color eyes'])
# print(samiy_0)
# samiy_0['x_position'] = 0
# samiy_0['y_position'] = 25
# print(samiy_0)

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# pariy = {}
# pariy['age'] = 6
# pariy['hobby'] = 'lot speaking'
# print(pariy)
# pariy['age'] = 7
# print(pariy)
# del pariy['age']
# print(pariy)

# zombiy = {'x_position': 1, 'y_position': 5, 'speed': 'fast'}
# print(zombiy)
# if zombiy['speed'] == 'slow':
#     x_walking = 1
# elif zombiy['speed'] == 'medium':
#     x_walking = 2
# else:
#     x_walking = 5
# zombiy['x_position'] = zombiy['x_position'] + x_walking   
# print("New x_position: " + str(zombiy['x_position']))
# print(zombiy['x_position'])

# city = {'a': 'xiva',
#         'b': 'baltika',
#         'c': 'moskva',
#         }
# print(city)
# print("I like " + city['a'].title() + " !")

# atribute = {'name': 'doni',
#         'surename': 'jumaniyazov',
#         'lastname': 'rustamovich'
#         } 
# for k, v in atribute.items():  # функция items() это возврашает "ключ - значение"
#     print("key: " + k)
#     print("value: " + v)

# pupils = {'a': 1, 'w': 7, 'd': 5, 'l': 3}

# for pupil in sorted(pupils.values()):
#     print(pupil)    

# pupils = []
# for pupil_num in range(10):
#     new_pupils =  {'a': 1, 'w': 7, 'd': 5, 'l': 12}
#     pupils.append(new_pupils)
# for pupil in pupils[:]:
#     print(pupil)

doni = {'name': 'd', 'pol': 'male'}
pari = {'name': 's', 'pol': 'shemale'}
peoples = [doni, pari]
for people in peoples:
    print(people)
    