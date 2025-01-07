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

if __name__ == "__main__":
    message = """This can be used to debug. 
    This lines will be executed only when functions.py is executed directly"""
    print(message)