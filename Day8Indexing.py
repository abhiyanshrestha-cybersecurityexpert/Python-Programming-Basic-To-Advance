# Indexing
# Data Type Related Topic
# Done By Abhiyan Shrestha

# Positive Indexing Number (0,1,2,3,4 flow that is defined)
a = [1,2,3,4,5,'Hello']
b = a [0] # Calling 0 index data in the group
#sprint(a)
print(b)

c = 'Hello ' # Every thing is data in coation and data is string
d = c[0]
print(d)

e = (1,2,3,4,5,'hello')
f = e[0]
print(f)

g = {1,2,3,4,5,'hello','world'} # Set doesnt have defined index number to give output as entered and position is changed
print(g)

h = {'a': 'Hello','b': 'World'} # Postion is self ordered itself
i = h['a']
print(i)

# Negative Indexing (from last data is in postion 1 & starts from 1)

j = [1,2,3,4]
k = j[-1]
print(k)

# Index Value Changing
# Mutable Data
l = [1,2,3,4,5]
l [0] = 'Hello' # changed data list 1 to hello  and is temporary change
print(l)

#m = 'hello' # Data cant be changed cause it is im-mutable
#m [0] = 'k' # gives error
#print(m) # gives error

# Tuple (group of constant data)
#n = (1,2,3,4,5) # Error
#n [0] ='Hello'
#print(n)

n = (1,2,3,4,5) # CHaning the value forcefully
o = list (n)
o [0] ='Hello'
print(o)

p = {'a': 'Hello','b':"Python"} # Dictionary
p ['c'] = 'python' # Change is made by adding C key and value with python and change is temporary
print(p)