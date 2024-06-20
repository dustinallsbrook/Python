from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✓"
rep = 0
CHECK_COUNTER = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global rep
    global CHECK_COUNTER
    window.after_cancel(TIMER)
    # Timer Text
    canvas.itemconfig(timer_text, text=f"00:00")
    # Timer Label to Timer
    timer_label.config(text='Timer', fg=GREEN)
    # Rep to 0
    rep = 0
    # Check Counter to 0
    CHECK_COUNTER = 0
    check_label.config(text=CHECK_MARK * CHECK_COUNTER)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global rep
    rep += 1
    timer_running = True
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if rep % 8 == 0:
        timer_label.config(text='Break', fg=RED)
        count_down(long_break_sec)
    elif rep % 2 == 0:
        timer_label.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text='Work', fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        if rep % 2 != 0:
            global CHECK_COUNTER
            CHECK_COUNTER += 1
            check_label.config(text=CHECK_MARK * CHECK_COUNTER)
            if CHECK_COUNTER == 4:
                CHECK_COUNTER = 0
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 143, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start Button Mechanism
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button Mechanism
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Timer Label
timer_label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 40), bg=YELLOW)
timer_label.grid(column=1, row=0)

# Checkmark label
check_label = Label(fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
check_label.grid(column=1, row=3)


window.mainloop()




