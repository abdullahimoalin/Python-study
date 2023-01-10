from tkinter import*

root = Tk()


root.title("Go Calculator")
root.iconbitmap(r"IconCalculator.ico")
root.configure(bg="black")

e = Entry(root, bg="lightgreen", fg="black", width=37, borderwidth=5)

e.grid(row=0, column=0, columnspan=4, padx=11 , pady=11)

##e.insert(0, "") -input will be done through buttons (input validation)



#Function

def button_click(number):
        
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current)+ str(number))
def button_clear():
        e.delete(0, END)
def button_add():
        first_num = e.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_num)
        e.delete(0, END)
        
def button_equal():
        second_num = e.get()
        e.delete(0, END)

        if math == "addition":
                e.insert(0, f_num + int(second_num))
        if math == "subtraction":
                e.insert(0, f_num - int(second_num))
        if math == "division":
                e.insert(0, f_num // int(second_num))
        if math == "multiplication":
                e.insert(0, f_num * int(second_num))
        
        
def button_subtract():
        first_num = e.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_num)
        e.delete(0, END)
        

def button_divide():
        first_num = e.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_num)
        e.delete(0, END)
        

def button_multiply():
        first_num = e.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_num)
        e.delete(0, END)
        return
        
#Defining class for default button text:

font="Calibri 11 bold"
                           
button_1 = Button(root, text="1",font=("Calibri 11 bold"),fg="white", bg="navy",borderwidth=5, padx=35.5, pady=15, command=lambda: button_click(1))
button_2 = Button(root, text="2",font=("Calibri 11 bold"),fg="white", bg="navy",borderwidth=5, padx=35, pady=15, command=lambda: button_click(2))
button_3 = Button(root, text="3",font=("Calibri 11 bold"),fg="white", bg="navy",borderwidth=5, padx=35, pady=15, command=lambda: button_click(3))
button_4 = Button(root, text="4",font=("Calibri 11 bold"),fg="white", bg="navy",borderwidth=5, padx=35.5, pady=15, command=lambda: button_click(4))
button_5 = Button(root, text="5",font=("Calibri 11 bold"),fg="white", bg="navy",borderwidth=5, padx=35, pady=15, command=lambda: button_click(5))
button_6 = Button(root, text="6",font=("Calibri 11 bold"),fg="white", bg="navy",borderwidth=5, padx=35, pady=15, command=lambda: button_click(6))
button_7 = Button(root, text="7",font=("Calibri 11 bold"),fg="white", bg="navy",borderwidth=5, padx=35.5, pady=15, command=lambda: button_click(7))
button_8 = Button(root, text="8",font=("Calibri 11 bold"),fg="white", bg="navy",borderwidth=5, padx=35, pady=15, command=lambda: button_click(8))
button_9 = Button(root, text="9",font=("Calibri 11 bold"),fg="white", bg="navy",borderwidth=5, padx=35, pady=15, command=lambda: button_click(9))
button_0 = Button(root, text="0",font=("Calibri 11 bold"),fg="white", bg="navy",borderwidth=5, padx=35, pady=15, command=lambda: button_click(0))

button_add = Button(root, text="+", font=("Calibri 11 bold"),bg="orange",borderwidth=5, padx=34, pady=15, command=button_add)
button_subtract = Button(root, text="-",font=("Calibri 11 bold"), bg="orange",borderwidth=5, padx=35, pady=15, command=button_subtract)
button_divide = Button(root, text="/",font=("Calibri 11 bold"), bg="orange",borderwidth=5, padx=35, pady=15, command=button_divide)
button_multiply = Button(root, text="X",font=("Calibri 11 bold"), bg="orange",borderwidth=5, padx=34, pady=15, command=button_multiply)
button_equal = Button(root, text="=",font=("Calibri 11 bold"), bg="orange",borderwidth=5, padx=35, pady=15, command=button_equal)
button_clear = Button(root, text="clear",font=("Calibri 11 bold"), bg="red",borderwidth=5, padx=25.47, pady=15, command=button_clear)

#Defining buttons

button_9.grid(row=1, column=2)
button_8.grid(row=1, column=1)
button_7.grid(row=1, column=0)

button_6.grid(row=2, column=2)
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=0)

button_3.grid(row=3, column=2)
button_2.grid(row=3, column=1)
button_1.grid(row=3, column=0)

button_0.grid(row=4, column=1)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2)

root.mainloop()
