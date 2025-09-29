from tkinter import *

window = Tk()
window.title('CALCULATOR USING TKINTER')
window.geometry('500x500')

#Entrybox
e = Entry(window, width=40,borderwidth=5, font=("Arial", 16))
e.place(x=5, y=10)

#Buttons

def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0 , str(result) + str(num))

button = Button(window, text = '1', width = 15, height = 2, command = lambda:click(1))
button.place(x=10, y=320)

button = Button(window, text = '2', width = 15, height = 2, command = lambda:click(2))
button.place(x=130, y=320)

button = Button(window, text = '3', width = 15, height = 2, command = lambda:click(3))
button.place(x=250, y=320)

button = Button(window, text = '4', width = 15, height = 2, command = lambda:click(4))
button.place(x=10, y=240)

button = Button(window, text = '5', width = 15, height = 2, command = lambda:click(5))
button.place(x=130, y=240)

button = Button(window, text = '6', width = 15, height = 2, command = lambda:click(6))
button.place(x=250, y=240)

button = Button(window, text = '7', width = 15, height = 2, command = lambda:click(7))
button.place(x=10, y=160)

button = Button(window, text = '8', width = 15, height = 2, command = lambda:click(8))
button.place(x=130, y=160)

button = Button(window, text = '9', width = 15, height = 2, command = lambda:click(9))
button.place(x=250, y=160)

button = Button(window, text = '0', width = 15, height = 2, command = lambda:click(0))
button.place(x=130, y=400)

def add():
    n1 = e.get()
    global math
    math = 'addition'
    global i
    i = int(n1)
    e.delete(0, END)

button = Button(window, text = '+', width = 15, height = 2, command = add)
button.place(x=370, y=320)

def sub():
    n1 = e.get()
    global math
    math = 'subtraction'
    global i
    i = int(n1)
    e.delete(0, END)

button = Button(window, text = '-', width = 15, height = 2, command = sub)
button.place(x=370, y=240)

def mult():
    n1 = e.get()
    global math
    math = 'multiplication'
    global i
    i = int(n1)
    e.delete(0, END)

button = Button(window, text = 'x', width = 15, height = 2, command = mult)
button.place(x=370, y=160)

def div():
    n1 = e.get()
    global math
    math = 'division'
    global i
    i = int(n1)
    e.delete(0, END)

button = Button(window, text = '/', width = 15, height = 2, command = div)
button.place(x=250, y=80)

def mod():
    n1 = e.get()
    global math
    math = 'modulo'
    global i
    i = int(n1)
    e.delete(0, END)

button = Button(window, text = '%', width = 15, height = 2, command = mod)
button.place(x=130, y=80)

def exp():
    n1 = e.get()
    global math
    math = 'exponentiation'
    global i
    i = int(n1)
    e.delete(0, END)

button = Button(window, text = '**', width = 15, height = 2, command = exp)
button.place(x=10, y=80)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, i + int(n2))
    elif math == 'subtraction':
        e.insert(0, i - int(n2))
    elif math == 'multiplication':
        e.insert(0, i * int(n2))
    elif math == 'division':
        e.insert(0, i / int(n2))
    elif math == 'modulo':
        e.insert(0, i % int(n2))
    elif math == 'exponentiation':
        e.insert(0, i ** int(n2))
button = Button(window, text = '=', width = 15, height = 2, command = equal)
button.place(x=370, y=400)

def clear():
    e.delete(0, END)

button = Button(window, text = 'Clear', width = 15, height = 2, command = clear)
button.place(x=250, y=400)

def backspace():
    n = e.get()
    new_text = n[:-1]
    e.delete(0, END)
    e.insert(0, new_text)

button = Button(window, text = 'Backspace', width = 15, height = 2, command = backspace)
button.place(x=370, y=80)

button = Button(window, text = 'Close', width = 15, height = 2, command = window.destroy)
button.place(x=10, y=400)

mainloop()