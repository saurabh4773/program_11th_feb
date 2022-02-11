# GUI calculator using tkinter

from cProfile import label
from tkinter import*

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
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
	cal = Tk()
	cal.configure(background="light grey")
	cal.title("Calculator")
	cal.geometry("300x250+100+100")
	equation = StringVar()

	lbl1 = Label(cal,bd=3,relief=RIDGE,fg="BLACK",bg="light grey")
	lbl1.place(x=0,y=0,width=300,height=70)
    
	expression_field = Entry(lbl1, textvariable=equation)
	expression_field.grid(columnspan=4,ipadx=80, ipady=19, padx=5, pady=3)

	lbl2 = Label(cal,bd=3,relief=RIDGE,fg="BLACK",bg="light grey")
	lbl2.place(x=0,y=70,width=300,height=140)

	button1 = Button(lbl2, text=' 1 ', fg='black', bg='grey',command=lambda: press(1), height=1, width=8)
	button1.grid(row=2, column=0, padx=4,pady=4)

	button2 = Button(lbl2, text=' 2 ', fg='black',bg='grey',command=lambda: press(2), height=1, width=8)
	button2.grid(row=2, column=1, padx=4,pady=4)

	button3 = Button(lbl2, text=' 3 ', fg='black',bg='grey',command=lambda: press(3), height=1, width=8)
	button3.grid(row=2, column=2, padx=4,pady=4)

	button4 = Button(lbl2, text=' 4 ', fg='black',bg='grey',command=lambda: press(4), height=1, width=8)
	button4.grid(row=1, column=0, padx=4,pady=4)

	button5 = Button(lbl2, text=' 5 ', fg='black',bg='grey',command=lambda: press(5), height=1, width=8)
	button5.grid(row=1, column=1, padx=4,pady=4)

	button6 = Button(lbl2, text=' 6 ', fg='black',bg='grey',command=lambda: press(6), height=1, width=8)
	button6.grid(row=1, column=2, padx=4,pady=4)

	button7 = Button(lbl2, text=' 7 ', fg='black',bg='grey',command=lambda: press(7), height=1, width=8)
	button7.grid(row=0, column=0, padx=4,pady=4)

	button8 = Button(lbl2, text=' 8 ', fg='black',bg='grey',command=lambda: press(8), height=1, width=8)
	button8.grid(row=0, column=1, padx=4,pady=4)

	button9 = Button(lbl2, text=' 9 ', fg='black',bg='grey',command=lambda: press(9), height=1, width=8)
	button9.grid(row=0, column=2, padx=4,pady=4)

	button0 = Button(lbl2, text=' 0 ', fg='black',bg='grey',command=lambda: press(0), height=1, width=8)
	button0.grid(row=3, column=1, padx=4,pady=4)

	plus = Button(lbl2, text=' + ', fg='black',bg='grey',command=lambda: press("+"), height=1, width=8)
	plus.grid(row=0, column=3, padx=4,pady=4)

	minus = Button(lbl2, text=' - ', fg='black',bg='grey',command=lambda: press("-"), height=1, width=8)
	minus.grid(row=1, column=3, padx=4,pady=4)

	multiply = Button(lbl2, text=' * ', fg='black',bg='grey',command=lambda: press("*"), height=1, width=8)
	multiply.grid(row=2, column=3, padx=4,pady=4)

	divide = Button(lbl2, text=' / ', fg='black',bg='grey',command=lambda: press("/"), height=1, width=8)
	divide.grid(row=3, column=3, padx=4,pady=4)

	equal = Button(lbl2, text=' = ', fg='black',bg='grey',command=equalpress, height=1, width=8)
	equal.grid(row=3, column=2, padx=4,pady=4)

	lbl3 = Label(cal,bd=3,relief=RIDGE,fg="BLACK",bg="light grey")
	lbl3.place(x=0,y=210,width=300,height=40)

	clear = Button(lbl3, text='Clear', fg='black',bg='grey',command=clear, height=1, width=40)
	clear.grid(row=0, column=0, padx=4,pady=4)

	Decimal= Button(lbl2, text='.', fg='black',bg='grey',command=lambda: press('.'), height=1, width=8)
	Decimal.grid(row=3, column=0, padx=4,pady=4)
	
	cal.mainloop()