# Functions
# It Stores statements and makes those statements reuseable
# Done by Abhiyan Shrestha

def hello_world():
    print('Hello World')
    print('-----------')
    print('Hello World')
    print('-----------')
    print('Hello World')
    print('-----------')
    print('Hello World')
    print('-----------')
    print('Hello World')
    print('-----------')
hello_world() # Calling hello world function and using the inside statements

def signin():
    print('--- Sign In ---')
signin()    

#hello_world() # calling the function

#############################################
# Arguments & Parameter of functions (working for multiple data)

num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))
def add(number1,number2):# Parameter for passing data through it(required)
    print(number1 + number2)

add(num1,num2) # Positional arguments

num3 = 45
num4 = 20
add(num3,num4)

