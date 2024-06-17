from tkinter import *


def button_clicked():
    new_text = float(miles_input.get()) * 1.6
    calc_label.config(text=round(new_text, 2))


window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

# Calculate Button
button = Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=2)

# Miles input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Miles text
miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

# equal text
equal_label = Label(text='is equal to')
equal_label.grid(column=0, row=1)

# Km text
km_label = Label(text='Km')
km_label.grid(column=2, row=1)

# calc label
calc_label = Label(text=0)
calc_label.grid(column=1, row=1)



window.mainloop()
