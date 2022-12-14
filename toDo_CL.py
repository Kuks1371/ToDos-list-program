#from todo_todo_functions import get_todos, write_todos
import todo_functions
import time

now = time.strftime("%H:%M:%S - %B %d, %Y")
print("It is:", now)

while True:
    action = input("Type add, show, edit, complete or exit: ")
    action = action.strip()

    if action.startswith('add'):
        text = action[4:]
        
        toDos = todo_functions.get_todos()

        toDos.append(text.capitalize() + "\n")

        todo_functions.write_todos(toDos)
        
    elif action.startswith('show'):

        toDos = todo_functions.get_todos()
        
        #new_toDos = [item.strip("\n") for item in toDos]     #list comprehension
        for index, item in enumerate(toDos):
            item = item.strip("\n")
            print(f"{index+1}.{item}")

    elif action.startswith('edit'):
        try:
            number = int(action[5:])
            number -= 1

            toDos = todo_functions.get_todos()
            
            new_todo = input("Enter new todo: ")
            toDos[number] = new_todo.capitalize() + "\n"
        
            todo_functions.write_todos(toDos)

        except ValueError:
            print("Your command is invalid!")
            continue


    elif action.startswith('complete'):
        try:
            number = int(action[9:])
            toDos = todo_functions.get_todos()
            index = number - 1
            todo_to_remove = toDos[index].strip("\n")
            toDos.remove(toDos[index])
            todo_functions.write_todos(toDos)
            print(f"Todo: {todo_to_remove} was deleted from the list.")
        except IndexError:
            print("There is no item with that number!")
            continue
        
    elif action.startswith('exit'):
        break

    else:
        print("Command is not valid!")
    

print("Good luck and bye!")