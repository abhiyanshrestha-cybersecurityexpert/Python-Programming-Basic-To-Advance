# For Loop
# for loop runs using group data
# Done by Abhiyan Shrestha

# iterable - group data including sting.

# iteration - loop process of going from 0 index data value to end index value in iterable data.

# Iterator - A variable which does iteration.

# For Loop

#a = ['Hello', 'World','Python','Nepal','Django']

#for i in a: # I is puting value in 5 list of string and ends after it
    #print('Hello') # Output is printed hello 5 times

    # Output is:
    # Hello
    # Hello
    # Hello
    # Hello
    # Hello

a = ['Hello', 'World','Python','Nepal','Django']

for i in a: # I is puting value in 5 list of string and ends after it
    print('Hello') # Output is printed hello 5 times
    
    for j in i: # j will be doing iteration in i
        print(j)

##############################################################################################
b = ['Hello', 'World','Python','Nepal','Django']

for i in b:
    if i == "Python":
        break

##############################################################################################

c = ['Hello', 'World','Python','Nepal','Django']

for i in c:
    if i == "python":
        continue
    print(i)

###############################################################################################


