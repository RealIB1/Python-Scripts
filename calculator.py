from tkinter import *

expression = ""


def btn_click(num):
    global expression

    expression = expression + str(num)

    equation.set(expression)


def equal_btn_click():
    try:
        global expression
        total = str(eval(expression))
        equation.set(str(total))

        expression = ""
    except:
        equation.set("ERROR!")
        expression = ""


def clear_btn():
    global expression
    expression = ""
    equation.set("")


window = Tk()
window.title('Calculator')
window.geometry("500x500")
# window.config(bg="blue")
# frame = Frame(window)
# frame.place(x=100, y=0, width=600, height=600)

equation = StringVar()

display_ent = Entry(window, width=15,
                    font=("Verdana", 20), bd=0,
                    textvariable=equation,
                    justify="right",
                    highlightbackground="black",
                    highlightcolor="black",
                    highlightthickness=2,
                    bg="#d1cfcf")
display_ent.insert(END, "0")
display_ent.place(x=50, y=10)

btn_ac = Button(window,
                text="AC",
                width=5, font=("Helvetica", 15),
                fg="white",
                activeforeground="white",
                activebackground="purple",
                bg="purple",
                command=clear_btn)
btn_ac.place(x=50, y=60)

btn_bracket = Button(window,
                     text="(",
                     width=3, font=("Helvetica", 15),
                     fg="white",
                     activeforeground="white",
                     activebackground="purple",
                     bg="purple",
                     command=lambda: btn_click("("))
btn_bracket.place(x=115, y=60)

btn_brackets = Button(window,
                      text=")",
                      width=3, font=("Helvetica", 15),
                      fg="white",
                      activeforeground="white",
                      activebackground="purple",
                      bg="purple",
                      command=lambda: btn_click(")"))
btn_brackets.place(x=148, y=60)

btn_modulo = Button(window,
                    text="%",
                    width=5, font=("Helvetica", 15),
                    fg="white",
                    activeforeground="white",
                    activebackground="purple",
                    bg="purple",
                    command=lambda: btn_click("%"))
btn_modulo.place(x=180, y=60)

btn_divide = Button(window,
                    text="/",
                    width=5, font=("Helvetica", 15),
                    fg="white",
                    activeforeground="white",
                    activebackground="purple",
                    bg="purple",
                    command=lambda: btn_click("/"))
btn_divide.place(x=245, y=60)

btn_seven = Button(window,
                   text="7",
                   width=5,
                   font=("Helvetica", 15),
                   fg="white",
                   activeforeground="white",
                   activebackground="purple",
                   bg="purple",
                   command=lambda: btn_click("7"))
btn_seven.place(x=50, y=100)

btn_eight = Button(window,
                   text="8",
                   width=5,
                   font=("Helvetica", 15),
                   fg="white",
                   activeforeground="white",
                   activebackground="purple",
                   bg="purple",
                   command=lambda: btn_click("8"))
btn_eight.place(x=115, y=100)

btn_nine = Button(window,
                  text="9",
                  width=5,
                  font=("Helvetica", 15),
                  fg="white",
                  activeforeground="white",
                  activebackground="purple",
                  bg="purple",
                  command=lambda: btn_click("9"))
btn_nine.place(x=180, y=100)

btn_multiplly = Button(window,
                       text="x",
                       width=5,
                       font=("Helvetica", 15),
                       fg="white",
                       activeforeground="white",
                       activebackground="purple",
                       bg="purple",
                       command=lambda: btn_click("*"))
btn_multiplly.place(x=245, y=100)

btn_four = Button(window,
                  text="4",
                  width=5,
                  font=("Helvetica", 15),
                  fg="white",
                  activeforeground="white",
                  activebackground="purple",
                  bg="purple",
                  command=lambda: btn_click("4"))
btn_four.place(x=50, y=140)

btn_five = Button(window,
                  text="5",
                  width=5,
                  font=("Helvetica", 15),
                  fg="white",
                  activeforeground="white",
                  activebackground="purple",
                  bg="purple",
                  command=lambda: btn_click("5"))
btn_five.place(x=115, y=140)

btn_six = Button(window,
                 text="6",
                 width=5,
                 font=("Helvetica", 15),
                 fg="white",
                 bg="purple",
                 activeforeground="white",
                 activebackground="purple",
                 command=lambda: btn_click("6"))
btn_six.place(x=180, y=140)

btn_minus = Button(window,
                   text="-",
                   width=5,
                   font=("Helvetica", 15),
                   fg="white",
                   activeforeground="white",
                   activebackground="purple",
                   bg="purple",
                   command=lambda: btn_click("-"))
btn_minus.place(x=245, y=140)

btn_one = Button(window,
                 text="1",
                 width=5,
                 font=("Helvetica", 15),
                 fg="white",
                 activeforeground="white",
                 activebackground="purple",
                 bg="purple",
                 command=lambda: btn_click("1"))
btn_one.place(x=50, y=180)

btn_two = Button(window,
                 text="2",
                 width=5,
                 font=("Helvetica", 15),
                 fg="white",
                 activeforeground="white",
                 activebackground="purple",
                 bg="purple",
                 command=lambda: btn_click("2"))
btn_two.place(x=115, y=180)

btn_three = Button(window,
                   text="3",
                   width=5,
                   font=("Helvetica", 15),
                   fg="white",
                   activeforeground="white",
                   activebackground="purple",
                   bg="purple",
                   command=lambda: btn_click("3"))
btn_three.place(x=180, y=180)

btn_plus = Button(window,
                  text="+",
                  width=5,
                  font=("Helvetica", 15),
                  fg="white",
                  activeforeground="white",
                  activebackground="purple",
                  bg="purple",
                  command=lambda: btn_click("+"))
btn_plus.place(x=245, y=180)

btn_zero = Button(window,
                  text="0",
                  width=11,
                  font=("Helvetica", 15),
                  fg="white",
                  activeforeground="white",
                  activebackground="purple",
                  bg="purple",
                  command=lambda: btn_click("0"))
btn_zero.place(x=50, y=220)

btn_float = Button(window,
                   text=".",
                   width=5,
                   font=("Helvetica", 15),
                   fg="white",
                   activeforeground="white",
                   activebackground="purple",
                   bg="purple",
                   command=lambda: btn_click("."))
btn_float.place(x=180, y=220)

btn_equal = Button(window,
                   text="=",
                   width=5,
                   font=("Helvetica", 15),
                   fg="white",
                   activeforeground="white",
                   activebackground="purple",
                   bg="purple",
                   command=equal_btn_click)
btn_equal.place(x=245, y=220)

window.mainloop()
