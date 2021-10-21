import random
from tkinter import *
from tkinter import messagebox

global chars
chars = []


def copy():
    messagebox.showinfo(title="Info", message="You copied the password to clipboard!")
    root.clipboard_clear()
    root.clipboard_append(entry_generated.get())


def restart():
    if r.get() == 1:
        messagebox.showinfo(title="Info", message="You reseted the parameters!")
        check_lower.deselect()
        check_lower.configure(state=NORMAL)
        check_upper.deselect()
        check_upper.configure(state=NORMAL)
        check_number.deselect()
        check_number.configure(state=NORMAL)
        check_symbol.deselect()
        check_symbol.configure(state=NORMAL)
        check_restart.deselect()
        entry_len.delete(0, END)
        entry_generated.delete(0, END)
        entry_generated.configure(state=DISABLED)
        chars.clear()


def generate():
    if not entry_len.get():
        messagebox.showerror(
            title="Error!", message="Insert a length to your password!"
        )
    elif not l.get() or not n.get():
        messagebox.showerror(
            title="Error!",
            message="Select at least the lower case and numbers parameters!",
        )
    else:
        password = ""
        for i in range(0, int(entry_len.get())):
            password_char = random.choice(chars)
            password = password + password_char
            entry_generated.configure(state=NORMAL)
            entry_generated.delete(0, END)
            entry_generated.insert(0, password)


def symbol():
    symbol_chars = ["!", "@", "$", "%", "&", "*", "#"]
    if s.get() == 1:
        chars.extend(symbol_chars)
        check_symbol.configure(state=DISABLED)


def number():
    if n.get() == 1:
        chars.extend(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        check_number.configure(state=DISABLED)


def upper():
    if u.get() == 1:
        chars.extend(
            [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "J",
                "K",
                "L",
                "M",
                "N",
                "O",
                "P",
                "Q",
                "R",
                "S",
                "T",
                "U",
                "V",
                "W",
                "X",
                "Y",
                "Z",
            ]
        )
        check_upper.configure(state=DISABLED)


def lower():
    if l.get() == 1:
        chars.extend(
            [
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
                "g",
                "h",
                "i",
                "j",
                "k",
                "l",
                "m",
                "n",
                "o",
                "p",
                "q",
                "r",
                "s",
                "t",
                "u",
                "v",
                "w",
                "x",
                "y",
                "z",
            ]
        )
        check_lower.configure(state=DISABLED)


def buttons():
    button_generate = Button(
        root,
        text="Generate",
        width=10,
        bg="white",
        font=("Fira Code", 18),
        fg="black",
        activebackground="white",
        activeforeground="black",
        command=generate,
    )
    button_generate.place(x=63, y=305)

    button_copy = Button(
        root,
        text="Copy",
        width=10,
        bg="white",
        font=("Fira Code", 18),
        fg="black",
        activebackground="white",
        activeforeground="black",
        command=copy,
    )
    button_copy.place(x=240, y=305)


def labels():
    global entry_len
    global entry_generated
    global check_lower
    global check_upper
    global check_number
    global check_symbol
    global check_restart
    global l
    global u
    global n
    global s
    global r

    l = IntVar()
    u = IntVar()
    n = IntVar()
    s = IntVar()
    r = IntVar()

    label_emp = Label(bg="white")
    label_emp.pack()

    label_len = Label(
        root,
        font=("Fira Code", 16),
        text="Type the length of the password: ",
        bg="white",
    )
    label_len.pack()

    label_emp1 = Label(bg="white")
    label_emp1.pack()

    entry_len = Entry(root, width=6, font=("Fira Code", 20))
    entry_len.pack()

    label_emp2 = Label(bg="white")
    label_emp2.pack()

    label_emp4 = Label(bg="white")
    label_emp4.pack()

    label_emp5 = Label(bg="white")
    label_emp5.pack()

    check_lower = Checkbutton(
        root,
        variable=l,
        text="Lower Case",
        onvalue=1,
        offvalue=0,
        font=("Fira Code", 10),
        fg="black",
        bg="white",
        activeforeground="black",
        activebackground="white",
        command=lower,
    )

    check_lower.place(x=30, y=142)

    check_upper = Checkbutton(
        root,
        variable=u,
        text="Upper Case",
        onvalue=1,
        offvalue=0,
        font=("Fira Code", 10),
        fg="black",
        bg="white",
        activeforeground="black",
        activebackground="white",
        command=upper,
    )

    check_upper.place(x=142, y=142)

    check_number = Checkbutton(
        root,
        variable=n,
        text="Numbers",
        onvalue=1,
        offvalue=0,
        font=("Fira Code", 10),
        fg="black",
        bg="white",
        activeforeground="black",
        activebackground="white",
        command=number,
    )

    check_number.place(x=255, y=142)

    check_symbol = Checkbutton(
        root,
        variable=s,
        text="Symbols",
        onvalue=1,
        offvalue=0,
        font=("Fira Code", 10),
        fg="black",
        bg="white",
        activeforeground="black",
        activebackground="white",
        command=symbol,
    )

    check_symbol.place(x=345, y=142)

    check_restart = Checkbutton(
        root,
        variable=r,
        text="Restart",
        onvalue=1,
        offvalue=0,
        font=("Fira Code", 12),
        fg="black",
        bg="white",
        activeforeground="black",
        activebackground="white",
        command=restart,
    )

    check_restart.place(x=30, y=80)

    label_emp6 = Label(bg="white")
    label_emp6.pack()

    label_generated = Label(
        root,
        font=("Fira Code", 18),
        text="Generated password: ",
        bg="white",
    )
    label_generated.pack()

    label_emp3 = Label(bg="white")
    label_emp3.pack()

    entry_generated = Entry(root, width=24, font=("Fira Code", 20), state=DISABLED)
    entry_generated.pack()

    buttons()


def main():
    global root
    root = Tk()
    root.title("Password Generator")
    root.geometry("460x380")
    root.config(bg="white")
    root.resizable(0, 0)
    labels()
    root.mainloop()


main()
