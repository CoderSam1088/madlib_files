import tkinter as tk
from tkinter import ttk

# Create the application window
window = tk.Tk()

my_label = ttk.Label(window, text="From my hotel room window, I see an oversized billboard"
      "\nwith his face on it: Jason, the Great Magician.")
my_label.grid(row=1, column=1)
my_label2 = ttk.Label(window, text="I absent-mindedly turn the pages of the phone book and"
      "\ncome across a city map. Sipping my iced latté,"
      "\nI run my fingers along the streets from the hotel to the opera hall. Not more than a half-hour walk.")
my_label2.grid(row=2, column=1)
my_label3 = ttk.Label(window, text="I glance at the clock. The show starts in one hour. "
      "\nPlenty of time! I gulp the last three sips of my latté and hop in the shower."
      "\nSoon I’m on my way to the show, carrying a fancy black handbag and a genuine smile.")
my_label3.grid(row=3, column=1)
my_label4 = ttk.Label(window, text="The billboard looks even more impressive from outside. The Great Jason's eyes seem to be"
      "\nglancing through me. I shiver and walk faster. I feel like a child about to open her birthday presents.")
my_label4.grid(row=4, column=1)
my_label5 = ttk.Label(window, text="The hall is dark when I come in; the show is about to begin. "
      "\nI make my way backstage just as the great magician puts on his top hat.")
my_label5.grid(row=5, column=1)

my_label6 = ttk.Label(window, text='"Daddy, Im so glad to see you," I say in a half-whisper. '
      '\n"Im in town for the writers '
      '\nworkshop, but I just couldnt miss your show.'
      "\nI give him a quick hug and go back into the seating area,"
      "\nleaving him with a startled smile. I settle down in"
      "\nthe darkness, and the curtains open.")
my_label6.grid(row=6, column=1)

my_label7 = ttk.Label(window, text="Magically, that show remains the Great Jason's best performance to this day.")

my_label7.grid(row=7, column=1)

window.mainloop()


