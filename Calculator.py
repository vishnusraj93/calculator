import parser
from tkinter import *
root = Tk()
root.configure(background="#8a8989")
root.geometry("155x215")
root.resizable(0,0)
root.title("Calculator")
display = Entry(root,font=('sans-serif', 10, 'bold'),
                     bd=3, insertwidth = 4, bg='#c4c2c2', fg='#000000', justify='right')
display.grid(columnspan=5,padx = 5, pady = 5)

i=0
def get_var(num):
    global i
    display.insert(i,num)
    i = i+1

def clear_all():
    display.delete(0,END)

def undo():
    entire_str = display.get()
    if len(entire_str):
        new_str = entire_str[:-1]
        clear_all()
        display.insert(0,new_str)
    else:
        clear_all()
        display.insert(0,"Error")

def get_operators(opr):
    global i
    length = len(opr)
    display.insert(i,opr)
    i = i+length

def calculate():
    entire_str = display.get()
    try:
        a = parser.expr(entire_str).compile()
        res = eval(a)
        clear_all()
        display.insert(0,res)
    except:
        clear_all()
        display.insert(0,"Error")

Button(root, bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "1",
       command=lambda :get_var(1)).grid(row = 5,column = 0,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "2",
       command=lambda :get_var(2)).grid(row = 5,column = 1,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "3",
       command=lambda :get_var(3)).grid(row = 5,column = 2,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "4",
       command=lambda :get_var(4)).grid(row = 4,column = 0,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "5",
       command=lambda :get_var(5)).grid(row = 4,column = 1,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "6",
       command=lambda :get_var(6)).grid(row = 4,column = 2,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "7",
       command=lambda :get_var(7)).grid(row = 3,column = 0,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "8",
       command=lambda :get_var(8)).grid(row = 3,column = 1,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "9",
       command=lambda :get_var(9)).grid(row = 3,column = 2,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "0",
       command=lambda :get_var(0)).grid(row = 6,column = 1,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = ".",
       command=lambda :get_operators('.')).grid(row = 6,column = 2,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "=",
       command=lambda :calculate()).grid(row = 6,column = 3,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "+",
       command=lambda :get_operators('+')).grid(row = 5,column = 3,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "-",
       command=lambda :get_operators('-')).grid(row = 4,column = 3,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "*",
       command=lambda :get_operators('*')).grid(row = 3,column = 3,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "÷",
       command=lambda :get_operators('/')).grid(row = 2,column = 2,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = ")",
       command=lambda :get_operators(')')).grid(row = 2,column = 1,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "(",
       command=lambda :get_operators('(')).grid(row = 2,column = 0,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "exp",
       command=lambda :get_operators('**')).grid(row = 1,column = 2,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "π",
       command=lambda :get_operators('*3.14')).grid(row = 1,column = 1,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "%",
       command=lambda :get_operators('%')).grid(row = 1,column = 0,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "⌫",
       command=lambda :undo()).grid(row = 2,column = 3,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "^2",
       command=lambda :get_operators('**2')).grid(row = 6,column = 0,sticky="nsew")

Button(root,bd=3,fg='#ffffff', bg='#000000', font=('sans-serif', 10, 'bold'),text = "AC",
       command=clear_all).grid(row = 1,column = 3,sticky="nsew")


root.mainloop()