import tkinter as tk
from tkinter import PhotoImage
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Flashcard Logic

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_bg,image=card_front_img)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_bg,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

# UI setup
window = tk.Tk()
window.title("FlashCards")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)


canvas = tk.Canvas(width=800,height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400,263,image=card_front_img)

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263, text="word", font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = tk.Button(image=cross_image,highlightthickness=0,command = next_card)
unknown_button.grid(row=1,column=0)

right_img = PhotoImage(file="images/right.png")
known_button = tk.Button(image=right_img,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

window.mainloop()