from functions import readfile, writefile, show
import time
time_message = time.strftime('%b %d, %Y %H:%M:%S')
print('Today is ', time_message)
while True:
    selection = input("Add, edit, complete or exit: ").lower().strip()

    if selection.startswith("add"):
        insertion= selection.replace('add ', '', 1) + "\n"

        todolist = readfile()
        todolist.append(insertion)
        writefile(todos_in=todolist)

        show()

    elif selection.startswith("show"):
        show()

    elif selection.startswith("complete") or selection.startswith("delete"):
        try:
            element= int(selection.replace('complete ', '', 1))
            todolist = readfile()
            if element>len(todolist) or element<1:
                print("Value out of range")
            else:
                del todolist[element-1]
                writefile(todos_in=todolist)
                print("Remaining todos: ")
                show()
        except ValueError:
            print('Need to specify a value')

    elif selection.startswith("edit"):
        try:
            selection = int(selection.replace('edit ', '', 1))-1
            correction = input("Provide the edition: ") + "\n"
            todolist = readfile()
            todolist[selection] = correction
            writefile(todos_in=todolist)
            show()
        except ValueError:
            print("You must enter a number.")
        except IndexError:
            print("Value out of range")

    elif selection.startswith("exit"):
        break
    else:
        print("Command not recognized, please try again!")
print("Program terminated correctly.")


