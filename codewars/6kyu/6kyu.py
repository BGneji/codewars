# Moves in squared strings (II)
def rot(strng):
    s = strng[::-1]
    return s
def selfie_and_rot(strng):
    s = ''
    l = strng.split()
    c = '.' * (len(l[0]))
    for i in l:
        s += (i + c) + '\n'
    s = (s[:len(s) - 1])
    s1 = strng[::-1]
    l1 = s1.split()
    s2 = ''
    for i in l1:
        s2+= (c + i) + '\n'
    s2 = (s2[:len(s2)])

    return s+'\n'+s2


def oper(fct, s):
    return (fct(s))


print(rot("abcd\nefgh\nijkl\nmnop"))
print(selfie_and_rot("abcd\nefgh\nijkl\nmnop"))
