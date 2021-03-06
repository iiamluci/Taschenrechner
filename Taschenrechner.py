from tkinter import *
import math


class calc:

    def getandreplace(self):

        self.expression = self.e.get()
        self.newtext = self.expression.replace('/', '/')
        self.newtext = self.newtext.replace('x', '*')

    def equals(self):

        self.getandreplace()
        try:

            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Ungültige Eingabe!')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def squareroot(self):

        self.getandreplace()
        try:

            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Ungültige Eingabe!')
        else:
            self.sqrtval = math.sqrt(self.value)
            self.e.delete(0, END)
            self.e.insert(0, self.sqrtval)

    def square(self):

        self.getandreplace()
        try:

            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Ungültige Eingabe!')
        else:
            self.sqval = math.pow(self.value, 2)
            self.e.delete(0, END)
            self.e.insert(0, self.sqval)

    def chf_to_dollar(self):

        self.getandreplace()
        try:

            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Ungültige Eingabe!')
        else:
            dollar = self.value * 1.08
            self.e.delete(0, END)
            self.e.insert(0, dollar)

    def dollar_to_chf(self):

        self.getandreplace()
        try:

            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Ungültige Eingabe!')
        else:
            chf = self.value * 0.92
            self.e.delete(0, END)
            self.e.insert(0, chf)

    def chf_to_bolivar(self):

        self.getandreplace()
        try:

            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Ungültige Eingabe!')
        else:
            bolivar = self.value * 4.4929
            self.e.delete(0, END)
            self.e.insert(0, bolivar)

    def bolivar_to_chf(self):

        self.getandreplace()
        try:

            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Ungültige Eingabe!')
        else:
            chf = self.value * 0.22
            self.e.delete(0, END)
            self.e.insert(0, chf)

    def bolivar_to_dollar(self):

        self.getandreplace()
        try:

            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Ungültige Eingabe!')
        else:
            dollar = self.value * 0.24
            self.e.delete(0, END)
            self.e.insert(0, dollar)

    def dollar_to_bolivar(self):

        self.getandreplace()
        try:

            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Ungültige Eingabe!')
        else:
            bolivar = self.value * 4.13
            self.e.delete(0, END)
            self.e.insert(0, bolivar)

    def clearall(self):

        self.e.delete(0, END)

    def clear1(self):
        self.txt = self.e.get()[:-1]
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def action(self, argi):

        self.e.insert(END, argi)

    def __init__(self, master):

        master.title('Taschenrechner')
        master.geometry()
        self.e = Entry(master)
        self.e.grid(row=0, column=0, columnspan=6, pady=3)
        self.e.focus_set()

        Button(master, text="=", width=13, height=3, fg="black",
               bg="grey", command=lambda: self.equals()).grid(
            row=4, column=4, columnspan=2)

        Button(master, text=".", width=5, height=3,
               fg="black", bg="white",
               command=lambda: self.action('.')).grid(row=4, column=1)

        Button(master, text="(", width=6, height=3,
               fg="black", bg="grey",
               command=lambda: self.action('(')).grid(row=2, column=4)

        Button(master, text=")", width=6, height=3,
               fg="black", bg="grey",
               command=lambda: self.action(')')).grid(row=2, column=5)

        Button(master, text="√", width=6, height=3,
               fg="black", bg="grey",
               command=lambda: self.squareroot()).grid(row=3, column=4)

        Button(master, text="x²", width=6, height=3,
               fg="black", bg="grey",
               command=lambda: self.square()).grid(row=3, column=5)

        Button(master, text='AC', width=6, height=3,
               fg="black", bg="grey",
               command=lambda: self.clearall()).grid(row=1, column=4)

        Button(master, text='C', width=6, height=3,
               fg="black", bg="grey",
               command=lambda: self.clear1()).grid(row=1, column=5)

        Button(master, text="+", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action('+')).grid(row=4, column=3)

        Button(master, text="x", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action('x')).grid(row=2, column=3)

        Button(master, text="-", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action('-')).grid(row=3, column=3)

        Button(master, text="÷", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action('/')).grid(row=1, column=3)

        Button(master, text="%", width=5, height=3,
               fg="black", bg="white",
               command=lambda: self.action('%')).grid(row=4, column=2)

        Button(master, text="0", width=5, height=3,
               fg="black", bg="white",
               command=lambda: self.action(0)).grid(row=4, column=0)

        Button(master, text="1", width=5, height=3,
               fg="black", bg="white",
               command=lambda: self.action(1)).grid(row=3, column=0)

        Button(master, text="2", width=5, height=3,
               fg="black", bg="white",
               command=lambda: self.action(2)).grid(row=3, column=1)

        Button(master, text="3", width=5, height=3,
               fg="black", bg="white",
               command=lambda: self.action(3)).grid(row=3, column=2)

        Button(master, text="4", width=5, height=3,
               fg="black", bg="white",
               command=lambda: self.action(4)).grid(row=2, column=0)

        Button(master, text="5", width=5, height=3,
               fg="black", bg="white",
               command=lambda: self.action(5)).grid(row=2, column=1)

        Button(master, text="6", width=5, height=3,
               fg="black", bg="white",
               command=lambda: self.action(6)).grid(row=2, column=2)

        Button(master, text="7", width=5, height=3,
               fg="black", bg="white",
               command=lambda: self.action('7')).grid(row=1, column=0)

        Button(master, text="8", width=5, height=3,
               fg="black", bg="white",
               command=lambda: self.action(8)).grid(row=1, column=1)

        Button(master, text="9", width=5, height=3,
               fg="black", bg="white",
               command=lambda: self.action(9)).grid(row=1, column=2)

        Button(master, text="$ > chf", width=10, height=3,
               fg="black", bg="grey",
               command=lambda: self.dollar_to_chf()).grid(row=2, column=6)

        Button(master, text="chf > $", width=10, height=3,
               fg="black", bg="grey",
               command=lambda: self.chf_to_dollar()).grid(row=1, column=6)

        Button(master, text="chf > bolivar", width=10, height=3,
               fg="black", bg="grey",
               command=lambda: self.chf_to_bolivar()).grid(row=3, column=6)

        Button(master, text="bolivar > chf", width=10, height=3,
               fg="black", bg="grey",
               command=lambda: self.bolivar_to_chf()).grid(row=4, column=6)

        Button(master, text="bolivar > dollar", width=12, height=3,
               fg="black", bg="grey",
               command=lambda: self.bolivar_to_dollar()).grid(row=1, column=7)

        Button(master, text="dollar > bolivar", width=12, height=3,
               fg="black", bg="grey",
               command=lambda: self.dollar_to_bolivar()).grid(row=2, column=7)

root = Tk()

obj = calc(root)

root.mainloop()

