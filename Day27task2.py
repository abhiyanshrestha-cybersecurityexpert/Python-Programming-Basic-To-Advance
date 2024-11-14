# Requirement
# Accounting System
# login and register
# Give user choices 1. add balance 2. view balance 3. reedem balance
# 1. add balance: ask the amount to add to the user and store it in a place
# 2. view balance: Print the user's total balance
# 3. reedem balance: ask the amount for the reedem, deduct it from the user account

def register():
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    usertype = input('Enter usertype(accoutant): ')
    
    with open('loginregister.txt','a') as f:
        f.write(f'{username},{password},{usertype}\n')
        print('Registration Successfull!')
        
def login():
    username = input('Username: ')
    password = input('password: ')
    
    with open('loginregister.txt','r') as f:
        for line in f:
            users_name, users_password,usertype = line.strip().split(',')
            if users_name == username and users_password == password:
                print('Welcome to Account Management System')
                return usertype
            print('Invalid Username or Password')
            return None

def add_balance():
    amount = float(input('Enter amount: '))
    username = input('Enter Username: ')
    
    with open('balance.txt','a') as f:
        f.write(f'{amount},{username}\n')
        print('Balance Added Successfully!')

def view_balance():
    try:
        with open('balance.txt','r') as f:
            print('Amount\t\t\t\tusername')
            for line in f:
                try:
                    user_ammount,user_name = line.strip().split(',')
                    print(f'{user_ammount}\t\t\t\t{user_name}')
                
                except ValueError:
                    print('Error: Invalid data format balance.txt')
    except FileNotFoundError:
        print(print('Error: Invalid data format in balance.txt'))
        
def reedem_balance():
    
    amount = float(input('Enter Amount to Redeem: '))
    username = input('Enter Username: ')
    
    try:
        with open('balance.txt', 'r') as f, open('tempbalance.txt', 'w') as f_new:
            for line in f:
                balance, user_name = line.strip().split(',')
                if user_name == username:
                    new_balance = float(balance) - amount
                    if new_balance >= 0:
                        f_new.write(f'{new_balance},{user_name}\n')
                        print(f'Total Balance: {new_balance}')
                        print('Redeem Successfull!')
                    else:
                        print('Insufficient balance')
                else:
                    f_new.write(line)
    except FileNotFoundError:
        print('Error: File not found in balance.txt')
    
            
def main():
    while True:
        print('\nAccount Management System')
        choice = input('1. Register 2. Logins: ')

        if choice == '1':
            register()
        
        elif choice == '2':
            usertype = login()
        
            if usertype:
        
                if usertype == 'accountant':
            
                    while True:
                        choice = input('1. add balance 2. view balance 3. reedem balance q. Logout: ')

                        if choice == '1':
                            add_balance()
                        
                        elif choice == '2':
                            view_balance()
                        
                        elif choice == '3':
                            reedem_balance()

                        elif choice == 'q':
                            break
                        else:
                            print('Invalid Choice!')


main()