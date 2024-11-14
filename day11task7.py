# Task-7
# todo 
    # Enter ur choice(add,remove,viewtodo)
    # Enter your todo
    #  add to do must add it
    # remove to do and ask id to remove it
    # viewtodo
# Done by Abhiyan Shrestha

todo_list = []
id_counter = 1

while True:
    choice = input("Enter Ur Choice (add,remove,viewtodo): ")

    if choice == "add":
        todo = input("Enter A Todo: ")
        todo_list.append({"id": id_counter, "todo": todo })
        id_counter += 1
        print("Todo Successfully Added")

    elif choice == "remove":
        if not todo_list:
            print("Empty List")
            
        else:
            for todo in todo_list:
                print(f"{todo['id']}. {todo['todo']}")
                remove_id = int(input("Enter the Id you want to delete: "))
                found = False
                for i, todo in enumerate(todo_list):
                    if todo['id'] == remove_id:
                        del todo_list[i]
                        found = True
                        break
                if found:
                    print("Successfull Deleted")

                else:
                    print("todo not found")

    elif choice == "viewtodo":
        if not todo_list:
            print("Todo list is empty!")

        else:
            for todo in todo_list:
                print(f"{todo['id']}.{todo['todo']}")
               