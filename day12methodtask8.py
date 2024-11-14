# All methods pratice file
# Done by Abhiyan Shrestha

a = [1,2,3,4,5]
a.append(1)
print(a)

########################################

# Positive Indexing Number (0,1,2,3,4 flow that is defined)
b = [1,2,3,4,5,'Hello']
c = b [0] # Calling 0 index data in the group
#sprint(a)
print(c)

########################################

e = (1,2,3,4,5,'hello')
f = e[0]
print(f)
############################################
g = {1,2,3,4,5,'hello','world'} # Set doesnt have defined index number to give output as entered and position is changed
print(g)

#########################################
j = [1,2,3,4]
k = j[-1]
print(k)

############################################
l = [1,2,3,4,5]
l [0] = 'Hello' # changed data list 1 to hello  and is temporary change
print(l)
##################################################################
n = (1,2,3,4,5) # CHaning the value forcefully
o = list (n)
o [0] ='Hello'
print(o)
###############################################################
p = {'a': 'Hello','b':"Python"} # Dictionary
p ['c'] = 'python' # Change is made by adding C key and value with python and change is temporary
print(p)