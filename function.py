# def max(a, b):
#     if a > b:
#         return a
#     # return b

# посмотрим рекурсию по числом фибаначи

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)  # здес вызов функцтя а значит рекурсия
# list_1 = []
# for i in range(1, 15):
#     list_1.append(fib(i))
# print(list_1)

# бистроая сортировка в рукурси

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot] 
    
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([1, 15, 6, 7, 58, 0, 3, 12]))   

# сортировка с слиянием

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] <right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i] 
#             i += 1
#             k += 1
            
#         while j < len(right):
#             nums[k] = right[j] 
#             j += 1
#             k += 1
# list_1 = [1, 56, 34, 13, 99, 52, 5, 34, 0, 19]    
# merge_sort(list_1)
# print(list_1)


# def f(x):
#     return x*x
# print(f(6))
        
# def math(op, x, y):      # op это operation
#     print(op(x, y))
           
# calk1 = lambda a,b: a + b
# math(calk1, 5, 45)   

# # другой вариант   

# def math(op, x, y):      # op это operation
#     print(op(x, y))
# math(lambda a,b: a + b, 5, 45)       


# data = [1, 2, 3, 5, 7, 8, 15]  
# res  = list()  
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)

# переобразуем lambda функции

# def select(f, col):
#     return[f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]

# data = [1, 2, 3, 5, 7, 8, 15] 
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# применение функя map()

# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x+5, list_1))
# print(list_1)

# data = '5 125 147 325 5 108'
# print(data)
# data = data.split()
# print(data)

# data = '12 56 333 0 26'
# print(data)
# data = list(map(int, data.split()))
# print(data)

# функция filter() оно филтирует обект котррый нам нужно

# data = [12, 5, 60, 10, 55, 88]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)
# работа с файламы

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
    data.write('line 3\n')
print(56)
    


              
        
               
             