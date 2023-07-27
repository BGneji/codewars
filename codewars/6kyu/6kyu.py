"""Moves in squared strings (II)"""
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

"""Mexican Wave"""
# def wave(people):
#     # l = []
#     # for i in range(len(people)):
#     #     s = people[i:i+1].upper()
#     #     if s != ' ':
#     #         w = people[:i]+s+people[i+1:]
#     #         l.append(w)
#     # return l
#
#     return [people[:i]+people[i:i+1].upper()+people[i+1:] for i in range(len(people)) if people[i:i+1].upper() != ' ']
#
#
# print(wave("hello"))
# print(wave("two words"))


'''CamelCase Method'''
# def camel_case(s):
#     return s.title().replace(' ','')
#
# print(camel_case("hello case"))

'''WeIrD StRiNg CaSe'''
# def to_weird_case(words):
#     # l1 = []
#     # s = ''
#     # for x, i in enumerate(words.split()):
#     #     g = 0
#     #     for y in i:
#     #         if g%2==0:
#     #             s+=y.upper()
#     #         else:
#     #             s+=y.lower()
#     #         g+=1
#     #     l1.append(s)
#     #     s = ''
#     # result = ' '.join(map(str,l1))
#     # return result
#     #
#     return ' '.join(
#         [''.join([i.upper() if x % 2 == 0 else i.lower() for x, i in enumerate(slovo)]) for slovo in words.split()])
#
#
# print(to_weird_case('Weird string case'))
# print(to_weird_case('THIs iS a TEST'))

"""Which are in?"""

# def in_array(array1, array2):
#     l2 = ' '.join(array2)
#     # l1 = []
#     # for i in array1:
#     #     s = l2.find(i)
#     #     if s != -1 and l2[s:s+len(i)] not in l1:
#     #         l1.append(l2[s:s+len(i)])
#     # l1.sort()
#     # return l1
#
#     lw = [''.join(array2)[''.join(array2).find(i):''.join(array2).find(i)+len(i)] for i in array1 if ' '.join(array2).find(i) != -1]
#     lw.sort()
#     return lw




# print(in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
# print(in_array(["tarp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))
# print(in_array(["arp", "mice", "bull"], ["lively", "alive", "harp", "sharp", "armstrong"]))
# print(in_array(['ple', 'or', 'tor', 'oesi', 'oes', 'ing', 've', 'byc', 'ou', 'pini', 'pinilo', 'ommo', 'ointer', 'tion', 'wh', 'vec', 'by', 'ect', 'ect', 'glac'],
# ['glad', 'best', 'your', 'for', 'the', 'ruby-doc.', 'I', 'have', 'for', 'have', 'have', 'your', 'known', 'versioning;', 'reference', 'to', 'does', 'input', 'mladens', 'here', 'a', 'what', 'Ruby', 'out', 'am', '1.9.2.', 'Ruby,', 'not', 'I', 'answer', 'should', 'is', 'that', 'the', 'using']))

