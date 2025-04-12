import tkinter as tk
from tkinter import image_types

#CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#TIMER RESET

#TIMER MECHANISM

#COUNTDOWN MECHANISM

#UI SETUP
window = tk.Tk()
window.title("Pomodoro")
title_label = tk.Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'bold'))
title_label.grid(column=1, row=0)

window.config(padx=100, pady=50, bg=YELLOW)
canvas = tk.Canvas(width=225, height=225, bg=YELLOW, highlightthickness=1)
tomato_img = tk.PhotoImage(file='tomato1.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(103, 120, text="00:00", fill="white", font=(FONT_NAME, 20, 'bold'))
canvas.grid(column=1, row=1)

start_btn = tk.Button(text="START")
start_btn.grid(column=0, row=2)

reset_btn= tk.Button(text="RESET")
reset_btn.grid(column=2, row=2)
window.mainloop()

