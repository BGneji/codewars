# Odd or Even?
def odd_or_even(arr):
    s = sum(arr)
    if s%2==0:
        return "even"
    else:
        return "odd"


print(odd_or_even([0, 1, 2]))


# String ends with?
def solution(text, ending):
    otvet = text[-len(ending):]
    if ending == otvet:
        return True
    return False


print(solution('abc', 'bc'))
print(solution("fails",   "ails"))
print(solution("sumo",    "omo"))


def reverse_words(s):
    if s == '':
        return ''
    for x in range(len(s)):
        return ' '.join([x[::-1] for x in s.split(' ')])


print(reverse_words(''))
print(reverse_words('double  spaced  words'))





