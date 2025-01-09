import functions
import FreeSimpleGUI as sg

todos = functions.readfile()

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do: ", key='input')
add_btn = sg.Button("Add")
edit_btn = sg.Button("Edit")
layout = sg.Listbox(values=todos, size=(50, 10), key='todolist', enable_events=True, bind_return_key=False)

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_btn, edit_btn],
                           [layout]],
                   font=('STXihei',12))
while True:
    event, value= window.read()
    print(event, value)
    match event:
        case "Add":
            new_todo = value['input']
            if new_todo:
                todos = functions.readfile()
                todos.append(new_todo + '\n')
                functions.writefile(todos)
                window['todolist'].update(todos)
                window['input'].update('')

        case "Edit":
            edit_todo = value['todolist'][0]
            new_todo = value['input']
            if edit_todo and new_todo:
                todo_index = todos.index(edit_todo)
                todos[todo_index] = new_todo + '\n'
                functions.writefile(todos)
                window['todolist'].update(todos)
                window['input'].update('')
        case "todolist":
            edit_todo = value['todolist'][0].strip()
            window['input'].update(edit_todo)


        case sg.WIN_CLOSED:
            break
window.close()
