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

# doni = {'name': 'd', 'pol': 'male'}
# pari = {'name': 's', 'pol': 'shemale'}
# peoples = [doni, pari]
# for people in peoples:
#     print(people)
    # % - это для опредеоение остатка от деление
    
# n = 26
# k = 19
# a = n % k
# # print(a)
# message = ""
# #prompt = "tell me: "#message = input("") 
# # while message != 'quit':
# if message == 'quit':
#    # message = input("")
#    print(message)
 # когда в цикле много услови при катором код выполялся далше это затрудняет работы тогда исползуем flag оно может быт True or False
 

# flag = True
# while flag:
#     message = input("tell us smthing: ")
#     if message == 'quit':
#         flag = False
#     else:
#         print(message)

# while True:
#     city = input("")
#     if city == 'xiva':
#         break                # остановит цикл
#     else:
#         print("I love " + city.title() + "!")

# current_num = 0
# while current_num < 10:     
#        current_num +=1   
#        if current_num % 2 == 0: 
#            continue
        
#        print(current_num)        
# users = ['alla', 'abba', 'adda']
# users_new = []

# while users:
#     current_user = users.pop()
#     print("veryfiring users: " + current_user.title())  
#     users_new.append(current_user)
# print("\nThe users confirmed: ")
# for new_user in users_new:
#     print(new_user.title())  
   #remove() исполуется для удаление какой то строки в списке и .remove() после имен списка
   
# animals = ['cat', 'dog', 'rat', 'cat', 'fish', 'cat']
# print(animals)
# while 'cat' in animals:
#     animals.remove('cat')
# # print(animals)
   
# dict_1 = {}
# polling_active = True
# while polling_active:
#     name = input("whats your name? ")
#     dict = input("which is your favorite? ")
#     dict_1[name] = dict
#     answer = input("would you like some cofee? (yes/ no) ")
#     if answer == 'no':
#         polling_active = False
# print("\n--- Dont catch---")
# for name, dict in dict_1.items():
#     print(name + " very like " + dict + ".")    

# ФУНКЦИЯ

# def greet_user():
    
#     print('sup')
# greet_user()    

# def greet_user(username):
#     print("Hello " + username.title() + " !")
# greet_user('dida')

# def describe(cat_type, cat_name):
   
#   print("i ve " +  cat_type + "!")
#   print("it is " + cat_type.title() +  " " + cat_name.title() + ".")
# describe('miko', 'tiko') 
# describe('pinto', 'chuchu')
# def show_animal(animal_type, animal_name = 'rick'):
    
#     print("i like " + animal_type + " dont like " + animal_name)
    

# show_animal('benny')

# 8-3. Футболка: напишите функцию make_shirt(), которая получает размер футболки и текст,
# который должен быть напечатан на ней. Функция должна выводить сообщение с размером
# и текстом. Вызовите функцию с использованием позиционных аргументов. Вызовите функцию во второй раз с использованием именованных аргументов.
# 8-4. Большие футболки: измените функцию make_shirt(), чтобы футболки по умолчанию
# имели размер L, и на них выводился текст «I love Python.». Создайте футболку с размером
# L и текстом по умолчанию, а также футболку любого размера с другим текстом.
# 8-5. Города: напишите функцию describe_city(), которая получает названия города и страны.
# Функция должна выводить простое сообщение (например, «Reykjavik is in Iceland»).
# Задайте параметру страны значение по умолчанию. Вызовите свою функцию для трех разных
# городов, по крайней мере один из которых не находится в стране по умолчанию.

# def make_shirt(size_shirt, text_shirt):
#     print("my shirts size " + size_shirt + " undo on it written " + text_shirt)
# make_shirt('41', 'do it again')

# def make_city(country, city):
#     print("i love " + country.title() + " more than city " + city.title())
# make_city('uzbekistan', 'new_york')    

# def known_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name
# builder = known_name('asad', 'adda')
# print(builder)

# def get_color(like, dislike):
#     describing ={'red': like, 'blue': dislike}
    
#     return describing
# wondering = get_color('dog', 'cat')
# print(wondering)

# def make_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name
# while True:
#     print("whats you name: ")
#     f_name = input(" my name ")
#     l_name = input("my sure name ")
#     # if f_name == 'joni':
#     #     break
    
#     formatted_name = make_name(f_name, l_name)
#     print(formatted_name)

# def greet_users(names):
#     for name in names:
#         print('Hello ' + name.title() + ' !')
# names_1 = ['doni', 'samiy', 'pariy']
# greet_users(names_1)

# def print_models(unprinted_designs, completed_models):
 
#   while unprinted_designs:
#     current_design = unprinted_designs.pop()

#  # Имитация печати модели на 3D-принтере.
#   print("Printing model: " + current_design)
#   completed_models.append(current_design)

# def show_completed_models(completed_models):

#  print("\nThe following models have been printed:")
#  for completed_model in completed_models:
#   print(completed_model)

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# Фокусники: создайте список с именами фокусников. Передайте список функции show_
# magicians(), которая выводит имя каждого фокусника в списке.

# def show_magicans(magicans):
#     for magicman in magicans:
#         print("hello " + magicman)
    
# magicman_1 = ['alan', 'rabo', 'boda']    
# show_magicans(magicman_1)    

# . Великие фокусники: начните с копии вашей программы из упражнения 8-9. Напишите
# функцию make_great(), которая изменяет список фокусников, добавляя к имени каждого
# фокусника приставку «Great». Вызовите функцию show_magicians() и убедитесь в том, что
# список был успешно изменен

# def show_magicans(magicans):
#     for magicman in magicans:
#         print("hello " + magicman)            
        
# def make_great(magicans):                      # втрой йункции связанно аргументов текуший функции
#     for i in range(len(magicans)):
#         magicans[i] = "Great" + " " +magicans[i]
                 
    
# magicman_list = ['alan', 'rabo', 'boda']    
# make_great(magicman_list)
# show_magicans(magicman_list) 

# def make_pizza(*toopings):  # *argument (создает пустой кортеж)это означает заране не известно сколко аргументов будет у функции
#     print(toopings)
    
# make_pizza('peperoni')  
# make_pizza('lakka', 'faqqa') 



# def make_pizza(*toppings):  
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#       print("- " + topping)
    
# make_pizza('peperoni')  
# make_pizza('lakka', 'faqqa') 


 
# def build_profile(first, last, **user_info):  # **user_info это позваляет столко нужно кол-во имя-значения типа словар
 
#   profile = {}
#   profile['first_name'] = first
#   profile['last_name'] = last
#   for key, value in user_info.items():
#     profile[key] = value
#   return profile
# user_profile = build_profile('albert', 'einstein',
#  location='princeton',
#  field='physics')
# print(user_profile)

# . Сэндвичи: напишите функцию, которая получает список компонентов сэндвича.
# Функция должна иметь один параметр для любого количества значений, переданных при вызове
# функции, и выводить описание заказанного сэндвича. Вызовите функцию три раза с разными количествами аргументов.

# def element_sendy(*elements):
#     print("sendy made by: ")
#     for element in elements:
#         print("- " + element) 
    
    
# element_sendy('tomat', 'salt', 'pepper')
# element_sendy('bread', 'sugar', 'pocco')

# . Автомобили: напишите функцию для сохранения информации об автомобиле в словаре.
# Функция всегда должна возвращать производителя и название модели, но при этом она
# может получать произвольное количество именованных аргументов. Вызовите функцию
# с передачей обязательной информации и еще двух пар «имя—значение» (например, цвет
# и комплектация). Ваша функция должна работать для вызовов следующего вида:
# car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
# Выведите воз

# def super_car(models, kind,  **car_info):
    
#     instruments = {}
#     instruments['model'] = models
#     instruments['speed'] = kind
#     for k,value in car_info.items():
#         instruments[k] = value 
#     return instruments

# car = super_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)
#               ИЛИ

# def super_car(models, kind,  **car_info):
    
#     instruments = {}
#     instruments['model'] = models
#     instruments['speed'] = kind
#     for k,value in car_info.items():
#         instruments[k] = value 
#     return instruments

# print(super_car('subaru', 'outback', color='blue', tow_package=True))

# def max_of_three(a,b,c):
#     max_num = max(a,b,c)
#     print(max_num)
# max_of_three(-7,-15,-8)  # это для проста вывода


# ниже для возврашение
# def max_of_three(a,b,c):
#     max_num = max(a,b,c)
#     return max_num

# def show_square(max_num):
#     square = max_num**2
#     return square

# res = max_of_three(13,0,129)
# print(res)
# res_1 = show_square(res)
# print(res_1)

# def is_palindrom(str):
#     return str == str[::-1]
    
    
# print(is_palindrom('rembo'))   

   
# def sort_list(*list_num):
#     sorted_list = sorted(list_num)
#     return sorted_list
    

# res = sort_list(1,3,5,4,12)
# print(res)
       

# def sort_list(list_num):
#     # Сортируем список
#     sorted_list = sorted(list_num)
#     return sorted_list

# # Пример использования
# res = sort_list([1, 3, 5, 4, 12])
# print(res)  # Output: [1, 3, 4, 5, 12]
    
    
   
