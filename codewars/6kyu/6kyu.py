'''Moves in squared strings (II)'''
# def rot(strng):
#     s = strng[::-1]
#     return s
# def selfie_and_rot(strng):
#     s = ''
#     l = strng.split()
#     c = '.' * (len(l[0]))
#     for i in l:
#         s += (i + c) + '\n'
#     s = (s[:len(s) - 1])
#     s1 = strng[::-1]
#     l1 = s1.split()
#     s2 = ''
#     for i in l1:
#         s2+= (c + i) + '\n'
#     s2 = (s2[:len(s2)])
#
#     return s+'\n'+s2
#
#
# def oper(fct, s):
#     return (fct(s))
#
#
# print(rot("abcd\nefgh\nijkl\nmnop"))
# print(selfie_and_rot("abcd\nefgh\nijkl\nmnop"))

'''Mexican Wave'''
# def wave(people):
#     print(people)
#     l = []
#     q ="".join(people.split())
#
#     for i in range(len(people)):
#         s = people[i:i+1].upper()
#         if s != ' ':
#             w = people[:i]+s+people[i+1:]
#             l.append(w)
#     return l
#
# print(wave("hello"))
# print(wave("two words"))


'''CamelCase Method'''
# def camel_case(s):
#     return s.title().replace(' ','')
#
#
# print(camel_case("hello case"))



