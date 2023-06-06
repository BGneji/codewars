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


def number(lines):
    return [f'{n}: {i}' for n, i in enumerate(lines, start=1)]





print(number(["a", "b", "c"]))
print(number([]))