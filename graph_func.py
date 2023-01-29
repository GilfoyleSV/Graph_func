import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, tan, pi, arctan, arctanh, tanh, arcsin, arccos, arctan2
from tkinter import *

win = Tk()
win.title('Калькулятор')
win.geometry('200x250+450+250')
win.resizable(False, False)

entry = Entry(win, font=('', 25))
entry.place(x=0, y=0, width=200, height=50)


def new_win():
    second_win = Toplevel(win)
    second_win.title('Функции')
    second_win.geometry('150x100+650+250')
    second_win.resizable(False, False)

    btn1 = Button(second_win, bg='black', fg='white', text='sin', command=lambda: input_inf('sin(x)'))
    btn1.place(x=0, y=0, width=50, height=50)
    btn2 = Button(second_win, bg='black', fg='white', text='cos', command=lambda: input_inf('cos(x)'))
    btn2.place(x=50, y=0, width=50, height=50)
    btn3 = Button(second_win, bg='black', fg='white', text='tg', command=lambda: input_inf('tan(x)'))
    btn3.place(x=0, y=50, width=50, height=50)
    btn4 = Button(second_win, bg='black', fg='white', text='x**', command=lambda: input_inf('x**'))
    btn4.place(x=50, y=50, width=50, height=50)
    btn5 = Button(second_win, bg='black', fg='white', text='arcsin', command=lambda: input_inf('arcsin(x)'))
    btn5.place(x=100, y=0, width=50, height=50)
    btn6 = Button(second_win, bg='black', fg='white', text='arccos', command=lambda: input_inf('arccos(x)'))
    btn6.place(x=100, y=50, width=50, height=50)


def input_inf(symbol):
    entry.insert(END, symbol)


def clear():
    entry.delete(0, END)
    try:
        plt.close()
    except:
        pass


def get_out():
    text = entry.get()

    def f(x):
        try:
            return eval(text)
        except:
            exit(0)

    x_axis = np.arange(-10 * pi, 10 * pi, 0.1)
    y_axis = np.array([f(i) for i in x_axis])
    plt.plot(x_axis, y_axis)
    plt.grid()
    plt.show()


btn1 = Button(win, bg='black', fg='white', text='1', command=lambda: input_inf('1'))
btn1.place(x=0, y=50, width=50, height=50)

btn2 = Button(win, bg='black', fg='white', text='2', command=lambda: input_inf('2'))
btn2.place(x=50, y=50, width=50, height=50)

btn3 = Button(win, bg='black', fg='white', text='3', command=lambda: input_inf('3'))
btn3.place(x=100, y=50, width=50, height=50)

btn4 = Button(win, bg='black', fg='white', text='4', command=lambda: input_inf('4'))
btn4.place(x=0, y=100, width=50, height=50)

btn5 = Button(win, bg='black', fg='white', text='5', command=lambda: input_inf('5'))
btn5.place(x=50, y=100, width=50, height=50)

btn6 = Button(win, bg='black', fg='white', text='6', command=lambda: input_inf('6'))
btn6.place(x=100, y=100, width=50, height=50)

btn7 = Button(win, bg='black', fg='white', text='7', command=lambda: input_inf('7'))
btn7.place(x=0, y=150, width=50, height=50)

btn8 = Button(win, bg='black', fg='white', text='8', command=lambda: input_inf('8'))
btn8.place(x=50, y=150, width=50, height=50)

btn9 = Button(win, bg='black', fg='white', text='9', command=lambda: input_inf('9'))
btn9.place(x=100, y=150, width=50, height=50)

btn_U = Button(win, bg='black', fg='white', text='*', command=lambda: input_inf('*'))  # умножение
btn_U.place(x=150, y=50, width=50, height=50)

btn_D = Button(win, bg='black', fg='white', text='/', command=lambda: input_inf('/'))  # деление
btn_D.place(x=150, y=100, width=50, height=50)

btn_P = Button(win, bg='black', fg='white', text='+', command=lambda: input_inf('+'))  # сложение
btn_P.place(x=150, y=150, width=50, height=50)

btn_M = Button(win, bg='black', fg='white', text='-', command=lambda: input_inf('-'))  # сложение
btn_M.place(x=150, y=200, width=50, height=50)

btn_C = Button(win, bg='black', fg='white', text='CE', command=clear)  # clear
btn_C.place(x=0, y=200, width=50, height=50)

btn_O = Button(win, bg='black', fg='white', text='=', command=get_out)  # out
btn_O.place(x=100, y=200, width=50, height=50)

btn_O = Button(win, bg='black', fg='white', text='func', command=new_win)  # новое окно
btn_O.place(x=50, y=200, width=50, height=50)

win.mainloop()
