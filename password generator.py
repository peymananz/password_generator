# by Peyman_Anz 2023
import string
from tkinter import Tk, Button, Entry, LabelFrame, IntVar, Label, Checkbutton, END, X, messagebox
import random
import webbrowser

root = Tk()
root.title("Generate Password")
root.iconbitmap("icon/icon.ico")
root.geometry("600x230")
root.configure(bg="#BB2649")
root.resizable(False, False)
a_z = string.ascii_lowercase
A_Z = string.ascii_uppercase
number = string.digits
smbl = string.punctuation

def create_pass(char):
    pass_generate = "".join(random.choices(char, k=int(entry_length.get())))
    text_box.insert(END, pass_generate)


def answer():
    try:
        text_box.delete(0, END)
        if var_check_button_all.get() == 1:
            create_pass(A_Z + a_z + number + smbl)
        elif var_check_button_A_Z.get() == 1 and var_check_button_a_z.get() == 1 and var_check_button_0_9.get() == 1:
            create_pass(A_Z + a_z + number)
        elif var_check_button_A_Z.get() == 1 and var_check_button_a_z.get() == 1 and var_check_button_Symbol.get() == 1:
            create_pass(A_Z + a_z + smbl)
        elif var_check_button_a_z.get() == 1 and var_check_button_0_9.get() == 1 and var_check_button_Symbol.get() == 1:
            create_pass(a_z + number + smbl)
        elif var_check_button_A_Z.get() == 1 and var_check_button_0_9.get() == 1 and var_check_button_Symbol.get() == 1:
            create_pass(A_Z + number + smbl)
        elif var_check_button_A_Z.get() == 1 and var_check_button_a_z.get() ==1:
            create_pass(A_Z + a_z)
        elif var_check_button_A_Z.get() == 1 and var_check_button_0_9.get() == 1:
            create_pass(A_Z + number)
        elif var_check_button_A_Z.get() == 1 and var_check_button_Symbol.get() == 1:
            create_pass(A_Z + smbl)
        elif var_check_button_a_z.get() == 1 and var_check_button_0_9.get() == 1:
            create_pass(a_z + number)
        elif var_check_button_a_z.get() == 1 and var_check_button_Symbol.get() == 1:
            create_pass(a_z + smbl)
        elif var_check_button_0_9.get() == 1 and var_check_button_Symbol.get() == 1:
            create_pass(number + smbl)
        elif var_check_button_A_Z.get() == 1:
            create_pass(A_Z)
        elif var_check_button_a_z.get() == 1:
            create_pass(a_z)
        elif var_check_button_0_9.get() == 1:
            create_pass(number)
        elif var_check_button_Symbol.get() == 1:
            create_pass(smbl)
        elif var_check_button_A_Z.get() == 0 and var_check_button_all.get() == 0 and var_check_button_a_z.get() == 0 and \
        var_check_button_0_9.get() == 0 and var_check_button_Symbol.get() == 0:
            select_length_character()
    except:
        select_length_character()


def select_length_character():
    messagebox.showerror("Error", "Please choice length or character select")


def copy_pass():
    text_box.clipboard_clear()
    pass_copy = text_box.get()
    text_box.clipboard_append(pass_copy)


######################################### Entry ##############################
text_box = Entry(root,  font=("arial", 16), bd=2, bg="#D8BFD8")
text_box.pack(fill=X)

######################################### Button ##############################
btn_generate = Button(root, text="Generate", bd=2, padx=50, command=answer, bg="#D8BFD8", fg="black")
btn_generate.place(x=20, y=40)

btn_copy = Button(root, text="Copy", bd=2, padx=60, command=copy_pass, bg="#D8BFD8", fg="black")
btn_copy.place(x=223, y=40)

btn_exit = Button(root, text="Exit", bd=2, padx=64, command=exit, bg="#D8BFD8", fg="black")
btn_exit.place(x=425, y=40)

######################################### Label Frame ##############################
lable_frm = LabelFrame(root, text="Option", padx=73, bd=2, bg="#BB2649")
#lable_frm.pack(fill=X, pady=70)
lable_frm.place(x=5, y=80)

######################################### Check Button ##############################
var_check_button_all = IntVar()
var_check_button_A_Z = IntVar()
var_check_button_a_z = IntVar()
var_check_button_0_9 = IntVar()
var_check_button_Symbol = IntVar()


def check_deactive_all():
    if var_check_button_Symbol.get() == 0 or var_check_button_0_9.get() == 0 or var_check_button_a_z.get() == 0 or\
        var_check_button_A_Z.get() == 0:
        check_button_all.deselect()
    else:
        check_button_all.select()


def check_btn_all():
    if var_check_button_all.get() == 1:
        check_button_A_Z.select()
        check_button_a_z.select()
        check_button_0_9.select()
        check_button_Symbol.select()
    else:
        check_button_A_Z.deselect()
        check_button_a_z.deselect()
        check_button_0_9.deselect()
        check_button_Symbol.deselect()


check_button_all = Checkbutton(lable_frm, text="All", variable=var_check_button_all, command=check_btn_all, bg="#BB2649",
                               activebackground="#BB2649")
check_button_all.grid(row=0, column=0, padx=30, pady=10)

check_button_A_Z = Checkbutton(lable_frm, text="A-Z", variable=var_check_button_A_Z, command=check_deactive_all, bg="#BB2649",
                               activebackground="#BB2649")
check_button_A_Z.grid(row=0, column=1, padx=10, pady=10)
check_button_A_Z.select()

check_button_a_z = Checkbutton(lable_frm, text="a-z", variable=var_check_button_a_z, command=check_deactive_all, bg="#BB2649",
                               activebackground="#BB2649")
check_button_a_z.grid(row=0, column=2, padx=10, pady=10)

check_button_0_9 = Checkbutton(lable_frm, text="0-9", variable=var_check_button_0_9, command=check_deactive_all, bg="#BB2649",
                               activebackground="#BB2649")
check_button_0_9.grid(row=0, column=3, padx=10, pady=10)

check_button_Symbol = Checkbutton(lable_frm, text="Symbol(@!#$%...)", variable=var_check_button_Symbol, command=check_deactive_all, bg="#BB2649",
                               activebackground="#BB2649")
check_button_Symbol.grid(row=0, column=4, padx=10, pady=10)

#########################################


def open_link(url):
    webbrowser.open_new_tab(url)


about_lbl = Label(root, text="Create By : Peyman Anz Copyright 2023", fg="yellow", bg="#BB2649")
about_lbl.place(x=5, y=200)

git_lbl = Label(root, text="https://github.com/peymananz", fg="yellow", cursor="hand2", bg="#BB2649")
git_lbl.place(x=400, y=200)
git_lbl.bind("<Button-1>", lambda x: open_link("https://github.com/peymananz"))

label_length = Label(lable_frm, text="Length", bg="#BB2649")
label_length.grid(row=1, column=0, pady=15)

var_entry_length = IntVar()
entry_length = Entry(lable_frm, width=3, font=("arial", 12), bd=2, textvariable=var_entry_length)
entry_length.grid(row=1, column=1)
entry_length.delete(0, END)
entry_length.insert(END, str(10))
root.mainloop()
