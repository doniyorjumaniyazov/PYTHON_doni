# a = int(input())
# b = int(input())
# print(a+b)

# num = int(input("введите число: "))
# if num % 2 ==0:
#     print("число четное")
# else:
#     print('нет')

# str = input("пишите строку: ")
# if str == str[::-1]:
#     print("yes")
# else:
#     print('no')

# def palindrom(str):
#     return  str == str[::-1]
# user = input(' ')
# if palindrom(user):
#     print('yes')
# else:
#     print('no')
# factorial_l = {}

# print(factorial(10))
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# n = int(input())
# res = factorial(n)
# print(res)

# n = int(input())
# i = 1
# res = 1
# while i <= n:
#     res *= i 
#     i +=1
# print(res) 

a = int(input("загадайте число: "))

while True:
    n = int(input("это число: "))
    if n > a: 
        
         print("слишком много")
    
    elif n < a:
        print("мало, придумай снова")
    
    else:
        print("точно отгадал")
        break

# a = int(input("Загадайте число: "))
# while True:
#     n = int(input("Введите ваше число: "))
#     if n > a:
#         print("Слишком много")
#     elif n < a:
#         print("Мало, попробуй снова")
#     else:
#         print("Точно отгадал!")
#         break

    

    

    