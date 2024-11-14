# Requirement for portal for student and teacher 
# Must have login, register and logut
# In register username, password and usertype is asked while registering
# In Login username and password is asked while loging in and checking the userdata in the file
#  Student can only view assignments, upload assignment and logout
# teacher can view assignment, add assignment, view results and logout
# if student wants to view assignment then show user its only assignment that he have uploaded
# if student want to upload assignment then ask the assignment name, task completed
# if teacher wants to add assignment then ask assignment name, tasks Requirement
# Done by Abhiyan Shrestha

def register():

    user_name = input('Enter Username: ')
    user_password = input('Enter Password: ')
    user_type = input('Enter Usertype (teacher/student): ')

    with open('teacherandstudentlogin.txt','a') as f:
        f.write(f'{user_name},{user_password},{user_type}\n')
        print('Registration Successful !')

def login():

    user_name = input('Username: ')
    user_password = input('Password: ')

    with open('teacherandstudentlogin.txt','r') as f:
        for line in f:
            username, password, user_type = line.strip().split(',')
            if user_name == username and user_password == password:
                print('Welcome Back Login Successful !') 
                return user_type
        print('Invalid username or password !')
        return None
    
def upload_assignment():

    assignment_name = input('Enter Assignment Name: ')
    task_completed = input('Enter Details: ')
    mark = float(input('Enter Mark: '))

    with open('studentassignments.txt','a') as f:
        f.write(f'{assignment_name},{task_completed},{mark}\n')
    print('Assignment uploaded Successfully!')

def view_studentassignment():

    try:
        with open('studentassignments.txt','r') as f:
            print('Assignment Name\t\t\t\tTask Completed\t\t\t\tmarks')
            for  line in f:
                try:
                    assignmentname, taskcompleted,mark = line.strip().split(',')
                    print(f'{assignmentname}\t\t\t\t{taskcompleted}\t\t\t\t{mark}\n')
                except ValueError:
                    print('Error: Invalid data format in studentassignment.txt')
    except FileNotFoundError:
        print('Error: File not found in studentassignment.txt')

def main():
    while True:
        choice = input('1. Register\t2. Login\tq. Quit: ')
        if choice == '1':
            register()
        
        elif choice == '2':
            user_type = login()
            if user_type:
                if user_type == 'teacher':
                    while True:
                        choice = input('1. View Student Assignment\t2. Upload Assignment\tq. Logout: ')
                        if choice == '1':
                            view_studentassignment()

                        elif choice == '2':
                            upload_assignment()

                        elif choice == 'q':
                            break
                        else:
                            print('Invalid Choice')
                else:
                    while True:
                        choice = input('1. View Assignment\t2. Upload Assignment\tq. Logout: ')
                        if choice == '1':
                            view_studentassignment()
                        
                        elif choice == '2':
                            upload_assignment()
                        
                        elif choice == 'q':
                            break

                        else:
                            print('Invalid Choice')
    
        elif choice == 'q':
            break
        else:
            print('Invalid Choice')
    
main()