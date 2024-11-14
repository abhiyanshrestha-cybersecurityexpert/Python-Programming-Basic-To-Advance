# Data Type

# String (text data)

# ''
# ""
# """ """ 

#################################################
a = "hello world's"
print(a)
##################################################

a = '"hello" world'
print(a)

##################################################

a = ''' "hello" world's " '''
print(a)
####################################################

# Number

# integer (without decimal)
123

# FLoat (with decimal number)
2.45

# Group (multiple data define)

# List (Mutable)
a = ['hello','world',25,'new world'] # List data with multiple entry
a = ['hello','world',25,'new world',[10,11,12,13,14]] # List data with multiple entry

# Tuple (Imutable)
b = ('hello','world',23,4,5)
b = ('hello','world',23,4,5,(1,2,3,4,5))  

# Set
c = {1,2,3,'hello'} # number and string

print(a)
print(b)
print(c) 

# Dictionary
d = {'a':"World"} # Key (any data) and value (string only)
d = {'a':{'World'}} # Key (any data) and value (string only)
d = {'username':'ram','password':'ram@123'} # Key (any data) and value (string only)

print (d)

# Boolen  data type (true or false)

# none type (no data is none)

e = None

# Operators ()

# Arithematic Operator (bodmas rule)

# Add Operator (number or string both)

f = 23 + 34
f = 'hello' + 'world'
f = [1,2,3,4,5] + [1,2,3,4,5]
f = 20.5 + 20
print(f)

# Substraction operator

g = 23 - 20
#g = 'hello' - 'world' # unsupported
#g = [1,2,3,4,5] - [1,2,3,4,5] # unsupported
g = 20.5 - 20
print(g)

# Multiplicaion Operator

h = 23 * 2
h = 23 * 2.5
h = 'hello' * 2 # other data type also allowed
h = [1,2,3,4,5] * 2
# h = [1,2,3,4,5] * 'hello' # not valid in multiplication
print(h)

# Division Operator

i = 20 / 2 # only number only allowed with demicmal number output
print(i)

# Floor Operator
j = 20 // 2  # as division and output is not in decimal number
print(j)

# Modulus Operator
k = 13 % 2 # reminder value is generated
print (k)

# Exponential Operator
l = 2 ** 2
print(l)
#####################################################################

# Assignment Operator

# = (assignment operator)

m = 'hello'
n = m
print(n)

# Add Assignment Operator

o = 23
o += 34
o -= 40 
print(o)

# Comparision Operator

# Greater than operator

p = 23
q = 34

r = p > q
print(r)

# Less than Operator

s = 23
t = 34

u = s < t
print(u)

# Equals to operator

#v = 40
#w = 44

#x = v == w
#print(x)

#Not Equals to operator

#v = 40 # text or number any of both can be used
#w = 44

#x = v != w
#print(x)

# Greater then or equals to operator

#v = 44 # 
#w = 44

#x = v >= w
#print(x)

# Less than or equals to operator
#v = 23
#w = 44

#x = v <= w
#print(x)

# Logical Operator

# And Operator (both operation must be true to get true result or output is false)
#v = 34
#w = 44
#x = 45

#y = v > w and w >x
#print(y)

# Or Operator (if one of the value is true output is will be true)

#v = 34
#w = 44
#x = 45

#y = v > w or w < x
#print(y)

# Not Operator (oposite value)

v = 34
w = 44

x = not(v > w)
print(x)

# Membership operator (not arethematic one)
# To check if they are member of the data that is to be checked

# In Operator (number is not allowed)

#hello =  'new   '
#world = 'new data' 
#worlds =  hello in world
#print(worlds)

hello =  '23'
world = ['new data',23]
worlds =  hello in world
print(worlds)

# Not in Operator (not in)

jk = "hello"
kj = "hello world"
kl = jk not in kj
print(kl)

# identity operator
# Is Operator (variable data same then true and if not same false is output)
# Ram Location Checking
lk = 'hello'
io = 'hello'
po = lk is io
print(po)

# Is not operator (opposite of Is operator)

nk = 'hello'
kn = 'world'
lm = nk is not kn
print(lm)