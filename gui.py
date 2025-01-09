import functions
import FreeSimpleGUI as sg

todos = functions.readfile()

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do: ", key='input')
add_btn = sg.Button("Add")
edit_btn = sg.Button("Edit")
delete_btn = sg.Button("Complete", key='delete')
layout = sg.Listbox(values=todos, size=(50, 10), key='todolist', enable_events=True, bind_return_key=False)
output = sg.Text(key='output')

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_btn, edit_btn],
                           [layout],
                           [delete_btn, output]
                           ],
                   font=('STXihei',12))

#The while is to read the events happening in the window with the method .read()
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
        case "delete":
            try:
                print('1 step')
                input_todo = value['input']
                edit_todo = value['todolist'][0]
                print(f'Value of the input: {input_todo}')
                print(f'Value of the list: {edit_todo}')
                if input_todo:
                    index = todos.index(edit_todo)
                    print(f'The index of the element: {index}')
                    del todos[index]
                    functions.writefile(todos)
                    window['todolist'].update(todos)
                    window['input'].update('')
            except ValueError:
                window['output'].update('Select a value in the list for deletion')
        case "todolist":
            try:
                edit_todo = value['todolist'][0].strip()
                window['input'].update(edit_todo)
            except IndexError:
                "nothing"

        case sg.WIN_CLOSED:
            break
window.close()
