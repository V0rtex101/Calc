# A simple GUI calculator
# Made by Fulufhelo Mulaudzi
# Version 2

from tkinter import *

LARGE_FONT = ("Arial", 40, "bold")
SMALL_FONT = ("Arial", 14)
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOUR = "#25265e"
WHITE = "#FFFFFF"
DIGIT_FONT = ("Arial", 24, "bold")

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.output_frame = self.output_frame()
        self.buttons_frame = self.buttons_frame()

        self.total_eq = ""
        self.current_eq = "0"
        self.total_label, self.cur_label = self.display_labels()

        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            ".":(4,1), 0:(4,2)
        }

        self.operations = {"/":"\u00F7", "*":"\u00D7", "-":"-", "+":"+"}

        for x in range(5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.display_digits(self.digits)
        self.display_op(self.operations)
        self.special_buttons()
        self.bind_keys()


    def output_frame(self):
        frame = Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def buttons_frame(self):
        frame = Frame(self.window)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def display_labels(self):
        total_label = Label(self.output_frame, text=self.total_eq, anchor=E,
                            bg=LIGHT_GRAY,fg=LABEL_COLOUR, font=SMALL_FONT)
        total_label.pack(fill=BOTH, expand=True)

        cur_label = Label(self.output_frame, text=self.current_eq, anchor=E,
                          bg=LIGHT_GRAY, fg=LABEL_COLOUR, font=LARGE_FONT)
        cur_label.pack(fill=BOTH, expand=True)

        return total_label, cur_label

    def display_digits(self, digits):
        for num,pos in digits.items():
            button = Button(self.buttons_frame, text=str(num),
                            bg=WHITE, fg=LABEL_COLOUR, font=DIGIT_FONT, borderwidth=0,
                            command=lambda x=num:self.button_press(x))
            button.grid(row=pos[0],column=pos[1], sticky=NSEW)

    def display_op(self, operations):
        count = 0
        for op,symbol in operations.items():
            button = Button(self.buttons_frame, text=symbol,
                            bg=OFF_WHITE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                            command=lambda x=op:self.op_press(x))
            button.grid(row=count,column=4, sticky=NSEW)
            count += 1

    def del_button(self):
        button = Button(self.buttons_frame, text="Del",
                        bg=OFF_WHITE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.del_press)
        button.grid(row=0,column=0, sticky=NSEW)

    def square_button(self):
        button = Button(self.buttons_frame, text="\u02E3\u00b2",
                        bg=OFF_WHITE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0,
                        command=self.squared_press)
        button.grid(row=1, column=0, sticky=NSEW)

    def sqrt_button(self):
        button = Button(self.buttons_frame, text="\u221A\u02E3",
                        bg=OFF_WHITE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.sqrt_press)
        button.grid(row=2, column=0, sticky=NSEW)

    def power_button(self):
        button = Button(self.buttons_frame, text="\u02E3\u207F",
                        bg=OFF_WHITE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.power_press)
        button.grid(row=3, column=0, sticky=NSEW)

    def perc_button(self):
        button = Button(self.buttons_frame, text="%",
                        bg=OFF_WHITE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.perc_press)
        button.grid(row=4, column=0, sticky=NSEW)

    def display_equal(self):
        button = Button(self.buttons_frame, text="=",bg=LIGHT_BLUE, fg=LABEL_COLOUR, font=DEFAULT_FONT_STYLE,
                        borderwidth=0, command=self.calculation)
        button.grid(row=4, column=3, columnspan=2, sticky=NSEW)

    def display_Cbutton(self):
        button = Button(self.buttons_frame, text="C", bg=WHITE, fg=LABEL_COLOUR, font=DIGIT_FONT, borderwidth=0,
                        command=self.clear_press)
        button.grid(row=0, column=1, sticky=NSEW)

    def display_parenthesis(self):
        button = Button(self.buttons_frame, text="(",
                        bg=WHITE, fg=LABEL_COLOUR, font=DIGIT_FONT, borderwidth=0,
                        command=lambda : self.button_press("("))
        button.grid(row=0, column=2, sticky=NSEW)

        button = Button(self.buttons_frame, text=")",
                        bg=WHITE, fg=LABEL_COLOUR, font=DIGIT_FONT, borderwidth=0,
                        command=lambda : self.button_press(")"))
        button.grid(row=0, column=3, sticky=NSEW)

    def update_total_label(self):
        exp = self.total_eq
        for op, symbol in self.operations.items():
            exp = exp.replace(op,symbol)

        self.total_label.config(text=exp)

    def update_cur_label(self):
        self.cur_label.config(text=self.current_eq)

    def button_press(self, text):
        if self.current_eq == "0" and text != ".":
            self.current_eq = ""
        self.current_eq += str(text)
        self.update_cur_label()

    def op_press(self, op):
        if self.total_eq and self.total_eq[-1] == "=":
            self.total_eq = ""
        self.total_eq += self.current_eq + " "
        self.total_eq += str(op) + " "
        self.update_total_label()
        self.current_eq = ""
        self.update_cur_label()

    def clear_press(self):
        self.total_eq = ""
        self.update_total_label()
        self.current_eq = ""
        self.update_cur_label()

    def del_press(self):
        self.current_eq = self.current_eq[:-1]
        self.update_cur_label()

    def squared_press(self):
        ans = eval(self.current_eq)**2
        self.current_eq = str(ans)
        self.update_cur_label()

    def sqrt_press(self):
        ans = str(eval(self.current_eq)**0.5)
        if ans[::-1][:2][::-1] == ".0":
            ans = ans[:-2]

        if len(ans) > 13 and "." in ans:
            ans = round(float(ans), 11)
            ans = str(ans)

        self.current_eq = ans
        self.update_cur_label()

    def power_press(self):
        if self.total_eq and self.total_eq[-1] == "=":
            self.total_eq = ""
        self.total_eq += self.current_eq + " ^ "
        self.current_eq = ""
        self.update_cur_label()
        self.update_total_label()

    def perc_press(self):
        num = eval(self.current_eq)
        ans = str(num / 100)
        if ans[::-1][:2][::-1] == ".0":
            ans = ans[:-2]

        self.current_eq = ans
        self.update_cur_label()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event:self.calculation())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.button_press(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, op=key: self.op_press(op))

        self.window.bind("(", lambda event: self.button_press("("))
        self.window.bind(")", lambda event: self.button_press(")"))


    def calculation(self):
        try:
            self.total_eq += self.current_eq + " "

            ans = str(eval(self.total_eq.replace("^", "**")))
            if ans[::-1][:2][::-1] == ".0":
                ans = ans[:-2]

            if len(ans) > 13 and "." in ans:
                ans = round(float(ans), 11)
                ans = str(ans)

            self.current_eq = ans
            self.total_eq += "="
            self.update_cur_label()
            self.update_total_label()
        except:
            self.clear_press()
            self.current_eq = "MATH ERROR"
            self.update_cur_label()

    def special_buttons(self):
        self.display_Cbutton()
        self.display_parenthesis()
        self.display_equal()
        self.del_button()
        self.sqrt_button()
        self.square_button()
        self.power_button()
        self.perc_button()

    def start(self):
        self.window.mainloop()


if __name__ == "__main__":
    program = Calculator()
    program.start()