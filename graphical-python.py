from tkinter import *

 

expression = ""

 

def press(num):

                global expression

                expression = expression + str(num)

                equation.set(expression)

 

def equalpress():

                try:

 

                                global expression

                                total = str(eval(expression))

                                equation.set(total)

                                expression = ""

 

                except:

 

                                equation.set("SYNTAX ERROR")

                                expression = ""

 

def clear():

                global expression

                expression = ""

                equation.set("")

 

if __name__ == "__main__":

   

                wn = Tk()

                wn.configure(background="light grey")

                wn.title("Calculator")

                wn.geometry("810x450")

                equation = StringVar()

                expression_field = Entry(wn, textvariable=equation)

                expression_field.grid(columnspan=4, ipadx=250)

 

                button1 = Button(wn, text=' 1 ', fg='black', bg='blue',

                                                                                command=lambda: press(1), height=3, width=21)

                button1.grid(row=2, column=0)

 

                button2 = Button(wn, text=' 2 ', fg='black', bg='blue',

                                                                                command=lambda: press(2), height=3, width=21)

                button2.grid(row=2, column=1)

 

                button3 = Button(wn, text=' 3 ', fg='black', bg='blue',

                                                                                command=lambda: press(3), height=3, width=21)

                button3.grid(row=2, column=2)

 

                button4 = Button(wn, text=' 4 ', fg='black', bg='blue',

                                                                                command=lambda: press(4), height=3, width=21)

                button4.grid(row=3, column=0)

 

                button5 = Button(wn, text=' 5 ', fg='black', bg='blue',

                                                                                command=lambda: press(5), height=3, width=21)

                button5.grid(row=3, column=1)

 

                button6 = Button(wn, text=' 6 ', fg='black', bg='blue',

                                                                                command=lambda: press(6), height=3, width=21)

                button6.grid(row=3, column=2)

 

                button7 = Button(wn, text=' 7 ', fg='black', bg='blue',

                                                                                command=lambda: press(7), height=3, width=21)

                button7.grid(row=4, column=0)

 

                button8 = Button(wn, text=' 8 ', fg='black', bg='blue',

                                                                                command=lambda: press(8), height=3, width=21)

                button8.grid(row=4, column=1)

 

                button9 = Button(wn, text=' 9 ', fg='black', bg='blue',

                                                                                command=lambda: press(9), height=3, width=21)

                button9.grid(row=4, column=2)

 

                button0 = Button(wn, text=' 0 ', fg='black', bg='blue',

                                                                                command=lambda: press(0), height=3, width=21)

                button0.grid(row=5, column=0)

 

                plus = Button(wn, text=' + ', fg='black', bg='blue',

                                                                command=lambda: press("+"), height=3, width=21)

                plus.grid(row=2, column=3)

 

                minus = Button(wn, text=' - ', fg='black', bg='blue',

                                                                command=lambda: press("-"), height=3, width=21)

                minus.grid(row=3, column=3)

 

                multiply = Button(wn, text=' × ', fg='black', bg='blue',

                                                                                command=lambda: press("*"), height=3, width=21)

                multiply.grid(row=4, column=3)

 

                divide = Button(wn, text=' ÷ ', fg='black', bg='blue',

                                                                                command=lambda: press("/"), height=3, width=21)

                divide.grid(row=5, column=3)

 

                equal = Button(wn, text=' = ', fg='black', bg='blue',

                                                                command=equalpress, height=3, width=21)

                equal.grid(row=5, column=2)

 

                clear = Button(wn, text='Clear', fg='black', bg='blue',

                                                                command=clear, height=3, width=21)

                clear.grid(row=5, column='1')

 

                Decimal= Button(wn, text='.', fg='black', bg='blue',

                                                                                command=lambda: press('.'), height=3, width=21)

                Decimal.grid(row=6, column=0)

   

                wn.mainloop()
