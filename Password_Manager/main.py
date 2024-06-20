from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for letter in range(randint(8, 10))]
    password_list += [choice(symbols) for symbol in range(randint(2, 4))]
    password_list += [choice(numbers) for number in range(randint(2, 4))]

    shuffle(password_list)

    password = ''.join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please don\'t leave any fields empty')
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}\n'
        #                                               f'Password: {password} \nIs it ok to save?')
        # if is_ok:
        try:
            with open('data.json', 'r') as file:
                # json.dump(new_data, file, indent=4)
                # Reading old data
                data = json.load(file)
                # Updating old data
                data.update(new_data)

            with open('data.json', 'w') as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            with open('data.json', 'w') as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)

            # print(data)
            # file.write(f"{website} | {email} | {password}\n")
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- Find Password ------------------------------- #
def search_passwords():
    website = website_input.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='File Does Not Exist')
        website_input.delete(0, END)
        password_input.delete(0, END)
    except KeyError:
        messagebox.showinfo(title=f'{website}', message=f'No Entry for {website}')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=35, pady=35)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_png)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Website Input field
website_input = Entry(width=24)
website_input.grid(column=1, row=1)
website_input.focus()

# Email/Username Label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# Email/Username Input Field
email_input = Entry(width=43)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'dustin@google.com')

# Password Label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# Password field
password_input = Entry(width=24)
password_input.grid(column=1, row=3)


# Generate Button
generate_button = Button(text="Generate Password", width=16, command=generate_password)
generate_button.grid(column=2, row=3)
# Search Button
search_button = Button(text="Search", width=16, command=search_passwords)
search_button.grid(column=2, row=1)
# Add button
add_button = Button(text="Add", width=41, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
