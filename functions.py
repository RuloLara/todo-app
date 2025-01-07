def readfile():
    with open('todos.txt', 'r') as file:
        read_list = file.readlines()
    return read_list

def writefile(todos_in):
    with open('todos.txt', 'w') as file:
        file.writelines(todos_in)

def show():
    show_list= readfile()
    if show_list:
        for index, todo in enumerate(show_list):
            print(f"{index + 1} - {todo.strip()}")
    else:
        print("Empty list...")