"""
@author: Saurabh Shroti
@goal: Calculator GUI

"""

from tkinter import *
import tkinter.messagebox
import sys

lo = None
root = None
r = None
frame1 = None
frame2 = None


def outbox(lc):
    global lo

    if lo:
        lo.destroy()

    lo = Label(frame2, text=lc, font=('courier', '40'))
    lo.grid(row=0, column=0, sticky=E)


def calculate():
    Lc = []
    Lo = ['/', 'x', '-', '+']
    ipt = r.get()
    count = 0
    a = ''
    tmp = 0

    if len(ipt) != 0:
        if ipt[0] != '+' and ipt[0] != 'x' and ipt[0] != '/' and ipt[-1] != '+' and ipt[-1] != '-' and ipt[-1] != 'x' and ipt[-1] != '/':
            for i in range(0, len(ipt)):
                if ipt[i] == '0' or ipt[i] == '1' or ipt[i] == '2' or ipt[i] == '3' or ipt[i] == '4' or ipt[i] == '5' \
                        or ipt[i] == '6' or ipt[i] == '7' or ipt[i] == '8' or ipt[i] == '9' or ipt[i] == '.':
                    a = a + ipt[i]
                elif ipt[i] == '+' or ipt[i] == '-' or ipt[i] == '/' or ipt[i] == 'x':
                    if ipt[i + 1] == '+' or ipt[i + 1] == '-' or ipt[i + 1] == '/' or ipt[i + 1] == 'x':
                        tmp = 1
                        tkinter.messagebox.showerror("Invalid Operation", "please check yor expression")
                        break
                    Lc.append(a)
                    a = ''
                    Lc.append(ipt[i])
                    count = count + 1
                else:
                    tkinter.messagebox.showerror("Invalid Input", "Character Not allowed")
                    tmp = 1
                    break
        else:
            tkinter.messagebox.showerror("Invalid Operation", "please check yor expression")
            tmp = 1
    else:
        tkinter.messagebox.showerror("Invalid Input", "Expression Empty")
        tmp = 1

    if tmp != 1:
        Lc.append(a)
        for n in range(0, len(Lc), 2):
            if Lc[n] != '':
                try:
                    if int(Lc[n]):
                        Lc[n] = int(Lc[n])
                    else:
                        Lc[n] = 0
                except ValueError:
                    Lc[n] = float(Lc[n])
    else:
        Lc.clear()

    x = 1
    for y in Lo:
        while x <= count:
            flag = 0
            for j in range(1, len(Lc) - 1, 2):
                if Lc[j] == y:
                    if y == '/':
                        if Lc[j + 1] == 0:
                            tkinter.messagebox.showerror("ERROR", "Dividing by 0")
                            Lc = []
                            break
                        temp = Lc[j - 1] / Lc[j + 1]
                        if Lc[j - 1] % Lc[j + 1] == 0:
                            temp = int(temp)
                    elif y == 'x':
                        temp = Lc[j - 1] * Lc[j + 1]
                    elif y == '+':
                        temp = Lc[j - 1] + Lc[j + 1]
                    elif y == '-':
                        if Lc[j - 1] == '':
                            if Lc[j + 1] == '0':
                                temp = 0
                            else:
                                temp = - Lc[j + 1]
                        else:
                            temp = Lc[j - 1] - Lc[j + 1]
                    else:                                 # no need, just for future update in code
                        print("invalid operator")
                        sys.exit(-1)
                    Lc[j - 1] = temp
                    Lc.pop(j + 1)
                    Lc.pop(j)
                    x = x + 1
                    flag = 1
                    break
            if flag == 0:
                break
    if Lc:
        outbox(Lc)


def root_window():
    global root, r, frame1, frame2
    root = Tk()
    root.title("Calculator")
    root.config(padx=2, pady=2)
    root.rowconfigure(3, weight=1)
    root.columnconfigure(0, weight=1)
    root.geometry('500x400')
    root.minsize(500, 500)
    root.maxsize(700, 700)

    def opts(op):
        box.insert(INSERT, op)

    def nums(ns):
        box.insert(INSERT, ns)

    def all_clear():
        box.delete(0, END)

        if lo:
            lo.destroy()

    def clear():
        box.delete(len(r.get()) - 1)

    def exit_button():
        if tkinter.messagebox.askyesnocancel("Are you sure ?", "Do you want to exit?"):
            sys.exit()

    def onReturnKey(event):
        calculate()

    frame = Frame(root)
    frame.grid(row=0, column=0, sticky=N)

    frame1 = Frame(root)
    frame1.columnconfigure(0, weight=1)
    frame1.grid(row=1, column=0, sticky=E+W)

    l1 = Label(frame, text='Calculator', font=('arial', '20'))
    l1.grid(row=0, column=0, sticky=N, ipadx=5, ipady=5, padx=2, pady=2)

    r = StringVar()

    box = Entry(frame1, textvariable=r, fg='black', cursor='xterm', font=('courier', '35'), justify=RIGHT)
    box.grid(row=0, column=0, sticky=E+W, ipadx=3, ipady=3, padx=2, pady=2)
    box.bind('<Return>', onReturnKey)
    box.focus()

    frame2 = Frame(root)
    frame2.grid(row=2, column=0, sticky=E)

    frame3 = Frame(root)
    frame3.rowconfigure((0, 1, 2, 3,), weight=1)
    frame3.columnconfigure((0, 1, 2, 3, 4), weight=1)
    frame3.grid(row=3, column=0, sticky=N+E+W+S)

    b1 = Button(frame3)
    b1.configure(text='+', fg='black', font=('courier', '20'), command=lambda: opts('+'))
    b1.grid(row=3, column=0, sticky=N+E+W+S)

    b2 = Button(frame3)
    b2.configure(text='-', fg='black', font=('courier', '20'), command=lambda: opts('-'))
    b2.grid(row=2, column=0, sticky=N+E+W+S)

    b3 = Button(frame3)
    b3.configure(text='x', fg='black', font=('courier', '20'), command=lambda: opts('x'))
    b3.grid(row=1, column=0, sticky=N+E+W+S)

    b4 = Button(frame3)
    b4.configure(text='/', fg='black', font=('courier', '20'), command=lambda: opts('/'))
    b4.grid(row=0, column=0, sticky=N+E+W+S)

    b5 = Button(frame3)
    b5.configure(text='7', fg='black', font=('courier', '20'), command=lambda: nums('7'))
    b5.grid(row=0, column=1, sticky=N+E+W+S)

    b6 = Button(frame3)
    b6.configure(text='8', fg='black', font=('courier', '20'), command=lambda: nums('8'))
    b6.grid(row=0, column=2, sticky=N+E+W+S)

    b7 = Button(frame3)
    b7.configure(text='9', fg='black', font=('courier', '20'), command=lambda: nums('9'))
    b7.grid(row=0, column=3, sticky=N+E+W+S)

    b8 = Button(frame3)
    b8.configure(text='4', fg='black', font=('courier', '20'), command=lambda: nums('4'))
    b8.grid(row=1, column=1, sticky=N+E+W+S)

    b9 = Button(frame3)
    b9.configure(text='5', fg='black', font=('courier', '20'), command=lambda: nums('5'))
    b9.grid(row=1, column=2, sticky=N+E+W+S)

    b10 = Button(frame3)
    b10.configure(text='6', fg='black', font=('courier', '20'), command=lambda: nums('6'))
    b10.grid(row=1, column=3, sticky=N+E+W+S)

    b11 = Button(frame3)
    b11.configure(text='1', fg='black', font=('courier', '20'), command=lambda: nums('1'))
    b11.grid(row=2, column=1, sticky=N+E+W+S)

    b12 = Button(frame3)
    b12.configure(text='2', fg='black', font=('courier', '20'), command=lambda: nums('2'))
    b12.grid(row=2, column=2, sticky=N+E+W+S)

    b13 = Button(frame3)
    b13.configure(text='3', fg='black', font=('courier', '20'), command=lambda: nums('3'))
    b13.grid(row=2, column=3, sticky=N+E+W+S)

    b14 = Button(frame3)
    b14.configure(text='0', fg='black', font=('courier', '20'), command=lambda: nums('0'))
    b14.grid(row=3, column=1, columnspan=2, sticky=N+E+W+S)

    b15 = Button(frame3)
    b15.configure(text='.', font=('courier', '20'), command=lambda: nums('.'))
    b15.grid(row=3, column=3, sticky=N+E+W+S)

    comp = Button(frame3)
    comp.configure(text='=', fg='green', font=('courier', '20', 'bold'), command=calculate)
    comp.grid(row=0, column=4, sticky=N+E+W+S)

    cl = Button(frame3)
    cl.configure(text='AC', fg='red', font=('courier', '20'), command=all_clear)
    cl.grid(row=1, column=4, sticky=N+E+W+S)

    bs = Button(frame3)
    bs.configure(text='C', fg='red', font=('courier', '20'), command=clear)
    bs.grid(row=2, column=4, sticky=N+E+W+S)

    ex = Button(frame3)
    ex.configure(text='exit', font=('courier', '20'), command=exit_button)
    ex.grid(row=3, column=4, sticky=N+E+W+S)

    root.mainloop()


root_window()
