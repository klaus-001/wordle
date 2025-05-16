import random
from tkinter import *
from tkinter import messagebox

ROWS = 6
COLUMNS = 5

row = 0
streak = 0
highscore = 0

WORDS = ['APPLE', 'BRAVE', 'CHAIR', 'DANCE', 'EAGLE', 'FLAME', 'GRAPE', 'HOUSE', 'IVORY', 'JOLLY', 'KNIFE',
         'LEMON', 'MANGO', 'NOBLE', 'OCEAN', 'PEARL', 'QUILT', 'RIVER', 'STONE', 'TIGER', 'UNITY', 'VIVID',
         'WALTZ', 'XENON', 'YACHT', 'ZEBRA']
WORD = random.choice(WORDS)

buttons = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]

def display_word():
    global row

    guess = word_entry.get().upper()

    if guess == "" or len(guess) > 5:
        messagebox.showwarning('Warning', 'Invalid guess!')
        return

    WORD_COUNT = {}

    for char in WORD:
        if char in WORD_COUNT:
            WORD_COUNT[char] += 1
        else:
            WORD_COUNT[char] = 1

    for j in range(COLUMNS):
        buttons[row][j].config(text=guess[j])

        if guess[j] == WORD[j]:

            buttons[row][j].config(bg='light green')

            if WORD_COUNT[guess[j]] == 1:
                WORD_COUNT.pop(guess[j])

            elif WORD_COUNT[guess[j]] > 1:
                WORD_COUNT[guess[j]] -= 1

    for j in range(COLUMNS):      
        if guess[j] != WORD[j] and guess[j] in WORD_COUNT:

            buttons[row][j].config(bg='light yellow')

            if WORD_COUNT[guess[j]] == 1:
                WORD_COUNT.pop(guess[j])

            elif WORD_COUNT[guess[j]] > 1:
                WORD_COUNT[guess[j]] -= 1

    row += 1

    word_entry.delete(0, END)

    if guess == WORD:
        submit_button.after(2000, next_level)

    if row >= ROWS and guess != WORD:
        submit_button.after(2000, game_over)
        messagebox.showinfo('Result', 'Game Over!')

def next_level():
    global row, WORD, streak

    word_entry.delete(0, END)

    for i in range(ROWS):
        for j in range(COLUMNS):
            buttons[i][j].config(text='', bg='SystemButtonFace')

    row = 0
    streak += 1
    WORD = random.choice(WORDS)

    streak_label.config(text=f'streak: {streak}')

def game_over():
    global row, WORD, streak, highscore

    highscore = streak

    word_entry.delete(0, END)

    for i in range(ROWS):
        for j in range(COLUMNS):
            buttons[i][j].config(text='', bg='SystemButtonFace')

    row = 0
    streak = 0
    WORD = random.choice(WORDS)

    streak_label.config(text=f'streak: {streak}')
    highscore_label.config(text=f'highscore: {highscore}')

window = Tk()

window.state('zoomed')
window.resizable(width=False, height=False)

# width = window.winfo_screenwidth()
# height = window.winfo_screenheight()
# window.geometry(f"{width}x{height}")

window.title("Wordle")
window.config(bg='light grey', cursor='circle')

wordle_label = Label(window, text='WORDLE', font=('Courier New', 60), bg='light grey')
wordle_label.pack(padx=30)

highscore_frame = Frame(window, bg='light grey')
highscore_frame.pack()

streak_label = Label(highscore_frame, text=f'streak: {streak}', font=('Courier New', 16), bg='light grey', fg='red')
streak_label.grid(row=0, column=0, padx=50)

highscore_label = Label(highscore_frame, text=f'highscore: {highscore}', font=('Courier New', 16), bg='light grey', fg='green')
highscore_label.grid(row=0, column=1, padx=50)

frame = Frame(window, bg='light grey')
frame.pack(padx=30)

for i in range(ROWS):
    for j in range(COLUMNS):
        buttons[i][j] = Button(frame, width=10, height=4, state='disabled')

        buttons[i][j].grid(row=i, column=j, padx= 4, pady=4)

word_entry = Entry(window, font=('Courier New', 16))
word_entry.pack(pady=10)

submit_button = Button(window, text='Submit', borderwidth=0, relief='flat', highlightthickness=0,
                       bg='light grey', activebackground='light grey', font=('Courier New', 18), command=display_word)
submit_button.pack()

window.mainloop()