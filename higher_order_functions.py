#x = int(input())
#y = int(input())

#def sum(x, y):
#    return x + y
#print(sum(x,y))

#print(lambda x, y: x + y, 4, 2)

#data = [1, 2, 3, 4, 5, 6]
#first type
#out = []
#for i in data:
#    if i % 2 == 0:
#        out.append((i, i ** 2))
#print(out)

#def select(f, col):
#    return[f(x) for x in col]

#def where(f, col):
#   return[x for x in col if f(x)]
#data = [1, 2, 3, 4, 5, 6]
#res = select(int, data)
#res = where(lambda x: x % 2 == 0, res)
#print(res)
#res = list(select(lambda x: (x, x ** 2), res))
#print(res)

#list_1 = [x for x in range (1, 20)]
#list_1 = list(map(lambda x: x + 10, list_1))
#print(list_1)
"""
def where(f, col):
    return[x for x in col if f(x)]

data = '1 2 3 34 5 56 6 66'.split()

res = map(int, data)

res = where(lambda x: x % 2 == 0, res)

res = list(map(lambda x: (x, x ** 2), res))
print(res)
"""

data = '1 2 3 34 5 56 6 66'.split()

res = map(int, data)

res = filter(lambda x: x % 2 == 0, res)

res = list(map(lambda x: (x, x**2), res))

print(res)















