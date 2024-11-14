# SLicing
# Data Slicing Work just a certain
# Done by Abhiyan Shrestha

a = 'Hello World'
b = a [0:5] # calling value from 0 to 5 and output is Hello 
print(b)

c = 'Hello World'
d = c [6:12] # calling value from 6 to 12 and output is World 
print(d)

e = 'Hello World'
f = e [6:] # calling value from 6 and output is World 
print(f)

g = 'Hello World'
h = g [0:5:2] # calling value from taking gab 2  and output is Hlo
print(h)

i = [1,2,3,4,5]
j = i [1:4] 
print(j) # output will be 2,3,4

k = [1,2,3,4,5]
l = k [-4:-1] # negative slicing
print(l) # output will be 2,3,4

m = [1,2,3,4,5]
m [1:3] = [5,6]
print(m) # output is 1,5,6,4,5