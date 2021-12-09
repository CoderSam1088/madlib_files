import tkinter as tk
from tkinter import ttk

# Create the application window
window = tk.Tk()

building = 1
adj_1 = 2
name = 3
occupation = 4
verb_1 = 5
noun_1 = 6
drink = 7
name_of_place = 8
number_1 = 9
obj_1 = 10
number_2 = 11
number_3 = 12
name_of_place_1 = 13
adj_2 = 14
obj_2 = 15
adj_3 = 16
verb_2 = 17
verb_3 = 18
type_of_person = 19
open_obj = 20
adj_4 = 21
place = 22
emotion = 23
event = 24
adj_6 = 25
noun_2 = 26

my_label = ttk.Label(window, text="From my _1_ window, I see an oversized _2_ billboard"
      "\nwith his face on it: _3_, the Great _4_.")
my_label.grid(row=1, column=1)
my_label2 = ttk.Label(window, text="I absent-mindedly _5_ the pages of the phone book and"
      "\ncome across a _6_ map. Sipping my _7_,"
      "\nI run my fingers along the streets from the _8_ to the opera hall. Not more than a _9_ walk.")
my_label2.grid(row=2, column=1)
my_label3 = ttk.Label(window, text="I glance at the _10_. The show starts in _11_ hour. "
      "\nPlenty of time! I gulp the last _12_ sips of my _7_ and hop in the shower."
      "\nSoon I’m on my way to the _13_, carrying a _14_ _15_ handbag and a _16_ smile.")
my_label3.grid(row=3, column=1)
my_label4 = ttk.Label(window, text="The billboard looks even more impressive from outside. The Great _3_'s eyes seem to be"
      "\nglancing through me. I _17_ and _18_ faster. I feel like a _19_ about to open her _20_.")
my_label4.grid(row=4, column=1)
my_label5 = ttk.Label(window, text="The hall is _21_ when I come in; the show is about to begin. "
      "\nI make my way to _22_ just as the great _4_ puts on his top hat.")
my_label5.grid(row=5, column=1)

my_label6 = ttk.Label(window, text='"Daddy, Im so _23_ to see you," I say in a half-whisper. '
      '\n"Im in town for the _24_, '
      '\nbut I just couldnt miss your show.'
      "\nI give him a quick hug and go back into the seating area,"
      "\nleaving him with a _25_ smile. I settle down in"
      "\nthe darkness, and the curtains open.")
my_label6.grid(row=6, column=1)

my_label7 = ttk.Label(window, text="Magically, that _26_ remains the Great _3_'s best performance to this day.")

my_label7.grid(row=7, column=1)

window.mainloop()


