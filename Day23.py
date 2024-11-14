# Exception Handling

#num1 = int(input('Enter a number: '))
#check = num1.isdigit()

#if check:
    #print(num1 * 2)

#else:
    #print('Invalid Output, Enter a number please!')

# try and except exception handeling
while True:
    try:
        num1 = int(input('Enter a number: '))
        print(num1 * 2)
        break

    except ValueError:
        print('Invalid Data')

while True:
    try:
        a = int(input('Enter a number: '))
        print(a * 2)
        break
    
    except ValueError:
        print(a)

while True:
    try:
        b = int(input('Enter a number: '))
        print(b * 2)
        break
    
    except Exception as e: # For Debugging this code can be useful
        print(e)


