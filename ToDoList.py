'''
TASK 1 : TO-DO LIST
A To-Do List Application is a useful project that helps users manage and organize their tasks efficiently.
This project aims to create a GUI-based application using Python, allowing users to create and delete their to-do lists.
'''

#import modules
from tkinter import *

#to display message box in case of no input
from tkinter import messagebox as msgbox

#configuration and creation of main window
mw = Tk()
mw.geometry('500x500+400+150')

#title of application
mw.title('TO-DO LIST')

#background color setup
mw.config(bg='#0E0962')

#to make the window fixed size
mw.resizable(width = False, height = False)

#to add the tasks
def addTask():
    task = entries.get()
    if task != '':
        listbox.insert(END, task)
        entries.delete(0,'end')
    else:
        msgbox.showwarning('Warning!!!','Please enter some task.')


#to delete the tasks
def deleteTask():
    listbox.delete(ANCHOR) #ANCHOR - selected item
    

#creation of widgets like frame, two buttons - add and delete ,listbox, scrollbar and entry
frame = Frame(mw)
frame.pack(pady = 10)

#listbox
listbox = Listbox(
    frame,
    width = 25,
    height = 8,
    font = ('Cambria', 18),
    bd = 0,
    fg = '#464646',
    highlightthickness = 0,
    selectbackground = '#a6a6a6',
    activestyle = 'none',
)
listbox.pack(side = LEFT, fill = BOTH)

#creating tasks
task_list = [
    'Drink water',
    'Do yoga at 7',
    'Clean the room',
    'Complete 5th chapter',
    'Meet ABC at 5',
    'Learn a new skill',
]

for item in task_list:
    listbox.insert(END, item)

task_list.sort()


#scrollbar
scbar = Scrollbar(frame)
scbar.pack(side = RIGHT, fill = BOTH)

listbox.config(yscrollcommand = scbar.set)
scbar.config(command = listbox.yview)

entries = Entry(
    mw,
    font = ('cambria',24)
)
entries.pack(pady = 20)

btn_frame = Frame(mw)
btn_frame.pack(pady = 20)

addButton = Button(
    btn_frame,
    text = 'ADD TASK',
    font = ('cambria 15'),
    bg = '#DDE61D',
    padx = 20,
    pady = 10,
    command = addTask
)
addButton.pack(fill = BOTH, expand = True, side = LEFT)

delButton = Button(
    btn_frame,
    text = 'DELETE TASK',
    font = ('cambria 15'),
    bg = '#E13D77',
    padx = 20,
    pady = 10,
    command = deleteTask
)
delButton.pack(fill = BOTH, expand = True, side = LEFT)





#run the main window loop
mw.mainloop()


