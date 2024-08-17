# Program to work as a calculator with GUI
# Fulufhelo Mulaudzi
# Version 1

from tkinter import *


def calculation():
    try:
        calc = str(eval(response.get()))
        clear()
        response.insert(END, calc)
    except:
        clear()
        response.insert(END, "MATH ERROR")


def clear():
    response.delete(0, END)


window = Tk()

window.geometry("265x200")
window.title("Calculator")
window.config(bg="#3e3e42")
window.resizable(0,0)

response = Entry(window, width=16, font=("Times New Roman", 24))
response.grid(columnspan=5)


btClear = Button(window, text="C", width=5, command=clear, bg="#808080")
btClear.grid(row=2, column=1)
btBrc1 = Button(window, text="(", width=5,command=lambda: response.insert("end", btBrc1.cget("text")), bg="#808080")
btBrc1.grid(row=2, column=2)
btBrc2 = Button(window, text=")", width=5,command=lambda: response.insert("end", btBrc2.cget("text")), bg="#808080")
btBrc2.grid(row=2, column=3)


bt7 = Button(window, text="7", width=5,command=lambda: response.insert("end", bt7.cget("text")), bg="#808080")
bt7.grid(row=3, column=1)
bt8 = Button(window, text="8", width=5,command=lambda: response.insert("end", bt8.cget("text")), bg="#808080")
bt8.grid(row=3, column=2)
bt9 = Button(window, text="9", width=5,command=lambda: response.insert("end", bt9.cget("text")), bg="#808080")
bt9.grid(row=3, column=3)
bt4 = Button(window, text="4", width=5,command=lambda: response.insert("end", bt4.cget("text")), bg="#808080")
bt4.grid(row=4, column=1)
bt5 = Button(window, text="5", width=5,command=lambda: response.insert("end", bt5.cget("text")), bg="#808080")
bt5.grid(row=4, column=2)
bt6 = Button(window, text="6", width=5,command=lambda: response.insert("end", bt6.cget("text")), bg="#808080")
bt6.grid(row=4, column=3)
bt1 = Button(window, text="1", width=5,command=lambda: response.insert("end", bt1.cget("text")), bg="#808080")
bt1.grid(row=5, column=1)
bt2 = Button(window, text="2", width=5,command=lambda: response.insert("end", bt2.cget("text")), bg="#808080")
bt2.grid(row=5, column=2)
bt3 = Button(window, text="3", width=5,command=lambda: response.insert("end", bt3.cget("text")), bg="#808080")
bt3.grid(row=5, column=3)
bt0 = Button(window, text="0", width=5,command=lambda: response.insert("end", bt0.cget("text")), bg="#808080")
bt0.grid(row=6, column=2)
btComma = Button(window, text=".", width=5,command=lambda: response.insert("end", btComma.cget("text")), bg="#808080")
btComma.grid(row=6, column=1)
btEq = Button(window, text="=", width=14, command=calculation, bg="#808080")
btEq.grid(row=6, column=3, columnspan=2)

btPlus = Button(window, text="+", width=5,command=lambda: response.insert("end", btPlus.cget("text")), bg="#808080")
btPlus.grid(row=2, column=4)
btMinus = Button(window, text="-", width=5,command=lambda: response.insert("end", btMinus.cget("text")), bg="#808080")
btMinus.grid(row=3, column=4)
btMult = Button(window, text="*", width=5,command=lambda: response.insert("end", btMult.cget("text")), bg="#808080")
btMult.grid(row=4, column=4)
btDiv = Button(window, text="/", width=5,command=lambda: response.insert("end", btDiv.cget("text")), bg="#808080")
btDiv.grid(row=5, column=4)



window.mainloop()