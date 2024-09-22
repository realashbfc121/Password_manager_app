from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(8)]
    [password_list.append(random.choice(symbols)) for _ in range(2)]
    [password_list.append(random.choice(numbers)) for _ in range(4)]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showerror(title="Missing Fields", message="Please fill all entries")
    else:
        entry_password.delete(0, END)
        entry_website.delete(0, END)

        with open(file="all_credentials_log", mode="r") as read_file:
            log_list = read_file.readlines()
            saved_text = f"{website} || {username} \n"
            if saved_text in log_list:
                # overwrite
                index = log_list.index(saved_text)
                log_list[index+1] = f" {password}\n "
                messagebox.showinfo(title="Personal Log",
                                    message="Password updated")
                with open(file="all_credentials_log", mode="w") as over_write:
                    over_write.writelines(log_list)

            else:
                with open(file="all_credentials_log", mode="a") as file:
                    file.write(f"\n{website} || {username} \n {password}\n ")
                    messagebox.showinfo(title="Personal Log",
                                        message="New password added to your book")


# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Password Manager")
lock_image = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200, highlightthickness=0)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)
win.config(padx=20, pady=20)

lable_website = Label(text="Website", font=("Courier", 8, "normal"))
lable_website.focus()
lable_website.grid(row=1, column=0)
entry_website = Entry(width=35, justify="center")
entry_website.grid(row=1, column=1, columnspan=2, sticky="ew")

lable_username = Label(text="Username/Email", font=("Courier", 8, "normal"))
lable_username.grid(row=2, column=0)
entry_username = Entry(width=35)
entry_username.insert(1, "ashwinyogam@gmail.com")
entry_username.grid(row=2, column=1, columnspan=2, sticky="ew")

lable_password = Label(text="Password", font=("Courier", 8, "normal"))
lable_password.grid(row=3, column=0)
entry_password = Entry(width=21)
entry_password.grid(row=3, column=1, sticky="ew")
button_password = Button(text="Generate Password", command=generate_password)
button_password.grid(row=3, column=2)

button_add = Button(text="Add", width=36, command=save_data)
button_add.grid(row=4, column=1, columnspan=2)

empty_buffer = Label(text="", pady=5)
empty_buffer.grid(row=5, column=1)

win.mainloop()
