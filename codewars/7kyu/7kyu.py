# # Odd or Even?
# def odd_or_even(arr):
#     s = sum(arr)
#     if s%2==0:
#         return "even"
#     else:
#         return "odd"
#
#
# print(odd_or_even([0, 1, 2]))
#
#
# # String ends with?
# def solution(text, ending):
#     otvet = text[-len(ending):]
#     if ending == otvet:
#         return True
#     return False
#
#
# print(solution('abc', 'bc'))
# print(solution("fails",   "ails"))
# print(solution("sumo",    "omo"))
#
#
# # Reverse words
# def reverse_words(s):
#     if s == '':
#         return ''
#     for x in range(len(s)):
#         return ' '.join([x[::-1] for x in s.split(' ')])
#
#
# print(reverse_words(''))
# print(reverse_words('double  spaced  words'))
#
# # Find the divisors!
# def divisors(integer):
#     otwet =[]
#     n = 1
#     l= []
#     while integer > n:
#         if integer%n == 0:
#             s = integer//n
#             l.append(s)
#         n+=1
#     otwet = l[1:]
#     if otwet == []:
#         return f"{integer} is prime"
#     return otwet[::-1]
#
#
# print(divisors(12))
# print(divisors(13))
import time

# # # Имеется отсортированный список из 128 имен, и вы ищете в нем значение методом бинарного поиска. Какое максимальное количество
# # # проверок для этого может потребоваться?
# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#     print(high)
#     count = 0
#     while low <= high:
#         mid = int((low + high) / 2)
#         guess = list[mid]
#         count += 1
#         if guess == item:
#             return mid,  count
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#
#     return None
#
#
# l = [i for i in range(1, 130)]
# print(binary_search(l, 3))
# print(binary_search(l, -1))


# def number(lines):
#     return [f'{n}: {i}' for n, i in enumerate(lines, start=1)]
#
#
#
#
#
# print(number(["a", "b", "c"]))
# print(number([]))


# #The highest profit wins!
# def min_max(lst):
#     return [min(lst), max(lst)]
#
# print(min_max([1]))

# # Sort array by string length
#
# def sort_by_length(arr):
#     l = sorted(arr, key=lambda el: len(el))
#     return l
#
#
#
# print(sort_by_length(['beg', 'i', 'life', 'to']))

# #Make a function that does arithmetic!
#
# def arithmetic(a, b, operator):
#     if operator == 'add':
#         return a + b
#     elif operator == 'subtract':
#         return a - b
#     elif operator == 'multiply':
#         return a*b
#     else:
#         return a/b
#
#
#
#
# print(arithmetic(1, 2, "add"))
# print(arithmetic(5, 2, "divide"))

# # Find the middle element
# def gimme(input_array):
#     for i in input_array:
#         if i == sorted(input_array)[1]:
#             return input_array.index(i)
#
#
# print(gimme([2, 3, 1]))


# #Round up to the next multiple of 5
#
# def round_to_next5(n):
#     while n%5 != 0:
#         n+=1
#     return n
#
# print(round_to_next5(0))
#
# of a sequence

# def sequence_sum(begin_number, end_number, step):
#     l = []
#     for i in range(begin_number, end_number+1, step):
#         l.append(i)
#     return sum(l)
#
#
# print(sequence_sum(1, 5, 1))
# Don't give me five!
# def dont_give_me_five(start, end):
#     n = [i for i in range(start, end + 1) if not '5' in str(i)]
#     return len(n)
#
#
# print(dont_give_me_five(1, 90))
# print(dont_give_me_five(110, 151))

# print(56%5)
# print(56%10)
# print(133%5)
#
# def dont_give_me_five(start, end):
#     l = []
#     for i in range(start, end + 1):
#         if i%5 != 0  and i%5 != i%10:
#             l.append(i)
#     print(l)
#         # return len(l)
#
#
# print(dont_give_me_five(1, 90))
# print(dont_give_me_five(110, 151))

# Find the stray number
# def stray(arr):
#     arr = sorted(arr)
#     n = [arr[i] for i in reversed(range(len(arr))) if arr[i] != arr[i-1]  and arr[i] != arr[i-2]  ]
#
#     return n[0]
# print(stray([1, 1, 1, 1, 1, 1, 2]))
# print(stray([2, 3, 2, 2, 2]))
# print(stray([3, 2, 2, 2, 2]))

# import  math
# a,b,c = map(int, input().split())
#
#
#
# s = 2*(a*c +b*c)
# print(math.ceil(s/16))
# num = ''
# stroka = 'qwe234'
# for i in 'qwe234':
#     if i.isdigit():
#         num+=i
# print(num)
# import time
# start_time = time.time()
#
# l = [i for i in "qwe209070лпломолмшггадлтщг0-80-7-0нполиле8998еш34" if i.isdigit()]
# print(l)
#
# print("--- %s seconds ---" % (time.time() - start_time))

#Sort Numbers
# import time
# start_time = time.time()
#
#
# def solution(nums):
#     return sorted(nums) if nums else []
#
# print(solution([1,2,3,10,5]))
# print(solution(None))
# print(solution([]))
#
# print("--- %s seconds ---" % (time.time() - start_time))

# import time
# start_time = time.time()
#
# def aa():
#     pass
# print("--- %s seconds ---" % (time.time() - start_time))

import time
start_time = time.time()


def remove_url_anchor(url):
    return url.split('#')[0]
print(remove_url_anchor("www.codewars.com#about"))




print("--- %s seconds ---" % (time.time() - start_time))

