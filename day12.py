# data type method
# Done By Abhiyan Shrestha
a = (1,2,2,2,3,4,3,5)
b = a.count(2)
print(b)

#output is:
# 3

c = (1,2,2,2,3,4,3,5)
d = c.count(3)
print(d)

#output is:
# 2

e = {1,2,3,4,5}
f = {6,7,8,9,10}
g = e.difference(f)
print(g)

#output is:
{1,2,3,4,5}

h = {1,2,3,4,5}
i = {6,7,8,9,10}
j = h.difference(i)
print(j)

#output is:
{1,2,3,4,5}

k = {'a': 'Hello','b': 'World'}
l = k.get('a')
print(l)

# Output is Hello