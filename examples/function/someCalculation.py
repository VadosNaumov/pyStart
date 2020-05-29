va1 = '321**'
va2 = '35%'
va3 = '5+4'
va4 = '5-4'
va5 = '5*4'
va6 = '5/4'
sign = {'+', '-', '*', '/'}


def fuck(s):
    c = list(s)
    gg = 0
    if c[len(c) - 1] == '*':
        k = len(c)
        for i in range(1, k - 1):
            gg *= 10
            gg = gg + int(c.pop(0))
        return gg ** 2
    if c[len(c) - 1] == '%':
        k = len(c)
        for i in range(1, k):
            gg *= 10
            gg = gg + int(c.pop(0))
        return round(gg * 0.01, 4)
    else:
        k = len(c)
        a = 0
        for i in range(1, k + 1):
            zn = c.pop(0)
            if zn in sign:
                ddd = zn
                b = a
                a = 0
            else:
                a *= 10
                a = a + int(zn)
        if ddd == '+':
            gg = a + b
        elif ddd == '-':
            gg = b - a
        elif ddd == '*':
            gg = b * a
        elif ddd == '/':
            gg = b / a
    return gg


print(fuck(va1))
print(fuck(va2))
print(fuck(va3))
print(fuck(va4))
print(fuck(va5))
print(fuck(va6))
