import tkinter as tk
from tkinter import ttk

# Create the application window
master = tk.Tk()

def newWindow():
    building = text1.get()
    adj_1 = text2.get()
    name = text3.get()
    occupation = text4.get()
    verb_1 = text5.get()
    noun_1 = text6.get()
    drink = text7.get()
    name_of_place = text8.get()
    number_1 = float(text9.get())
    obj_1 = text10.get()
    number_2 = float(text11.get())
    number_3 = float(text12.get())
    name_of_place_1 = text13.get()
    adj_2 = text14.get()
    obj_2 = text15.get()
    adj_3 = text16.get()
    verb_2 = text17.get()
    verb_3 = text18.get()
    type_of_person = text19.get()
    open_obj = text20.get()
    adj_4 = text21.get()
    place = text22.get()
    emotion = text23.get()
    event = text24.get()
    adj_6 = text25.get()
    noun_2 = text26.get()

    
    window = tk.Toplevel(master)
    window.title("My Story")
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
    

#first entry
tk.Label(master, text="Building: ").grid(row=0, column=1, sticky=tk.E) #label for text
text1 = tk.Entry(master)
text1.grid(row=0, column=2, sticky=tk.W) #entry box

#second entry
tk.Label(master, text="Adjective that starts with a vowel: ").grid(row=1, column=1, sticky=tk.E) #label for text
text2 = tk.Entry(master)
text2.grid(row=1, column=2, sticky=tk.W)

#third entry
tk.Label(master, text="Name of a person: ").grid(row=2, column=1, sticky=tk.E) #label for text
text3 = tk.Entry(master)
text3.grid(row=2, column=2, sticky=tk.W)

#fourth entry
tk.Label(master, text="Occupation: ").grid(row=3, column=1, sticky=tk.E) #label for text
text4 = tk.Entry(master)
text4.grid(row=3, column=2, sticky=tk.W)

#fifth entry
tk.Label(master, text="Verb (present tense): ").grid(row=4, column=1, sticky=tk.E) #label for text
text5 = tk.Entry(master)
text5.grid(row=4, column=2, sticky=tk.W)

#sixth entry
tk.Label(master, text="Noun: ").grid(row=5, column=1, sticky=tk.E) #label for text
text6 = tk.Entry(master)
text6.grid(row=5, column=2, sticky=tk.W)

#seventh entry
tk.Label(master, text="Drink: ").grid(row=6, column=1, sticky=tk.E) #label for text
text7 = tk.Entry(master)
text7.grid(row=6, column=2, sticky=tk.W)

#eigth entry
tk.Label(master, text="Name of a place: ").grid(row=7, column=1, sticky=tk.E) #label for text
text8 = tk.Entry(master)
text8.grid(row=7, column=2, sticky=tk.W)

#ninth entry
tk.Label(master, text="Number: ").grid(row=8, column=1, sticky=tk.E) #label for text
text9 = tk.Entry(master)
text9.grid(row=8, column=2, sticky=tk.W)

#tenth entry
tk.Label(master, text="Object: ").grid(row=9, column=1, sticky=tk.E) #label for text
text10 = tk.Entry(master)
text10.grid(row=9, column=2, sticky=tk.W)

#11th entry
tk.Label(master, text="Number: ").grid(row=10, column=1, sticky=tk.E) #label for text
text11 = tk.Entry(master)
text11.grid(row=10, column=2, sticky=tk.W)

#12th entry
tk.Label(master, text="Number: ").grid(row=11, column=1, sticky=tk.E) #label for text
text12 = tk.Entry(master)
text12.grid(row=11, column=2, sticky=tk.W)

#13th entry
tk.Label(master, text="Name of a place: ").grid(row=12, column=1, sticky=tk.E) #label for text
text13 = tk.Entry(master)
text13.grid(row=12, column=2, sticky=tk.W)

#14th entry
tk.Label(master, text="Adjective: ").grid(row=13, column=1, sticky=tk.E) #label for text
text14 = tk.Entry(master)
text14.grid(row=13, column=2, sticky=tk.W)

#15th entry
tk.Label(master, text="Object: ").grid(row=14, column=1, sticky=tk.E) #label for text
text15 = tk.Entry(master)
text15.grid(row=14, column=2, sticky=tk.W)

#16th entry
tk.Label(master, text="Adjective: ").grid(row=15, column=1, sticky=tk.E) #label for text
text16 = tk.Entry(master)
text16.grid(row=15, column=2, sticky=tk.W)

#17th entry
tk.Label(master, text="Verb: ").grid(row=16, column=1, sticky=tk.E) #label for text
text17 = tk.Entry(master)
text17.grid(row=16, column=2, sticky=tk.W)

#18th entry
tk.Label(master, text="Verb: ").grid(row=17, column=1, sticky=tk.E) #label for text
text18 = tk.Entry(master)
text18.grid(row=17, column=2, sticky=tk.W)

#19th entry
tk.Label(master, text="Type of person: ").grid(row=18, column=1, sticky=tk.E) #label for text
text19 = tk.Entry(master)
text19.grid(row=18, column=2, sticky=tk.W)

#20th entry
tk.Label(master, text="Object you can open: ").grid(row=19, column=1, sticky=tk.E) #label for text
text20 = tk.Entry(master)
text20.grid(row=19, column=2, sticky=tk.W)

#21st entry
tk.Label(master, text="Adjective: ").grid(row=20, column=1, sticky=tk.E) #label for text
text21 = tk.Entry(master)
text21.grid(row=20, column=2, sticky=tk.W)

#22nd entry
tk.Label(master, text="Name of place: ").grid(row=21, column=1, sticky=tk.E) #label for text
text22 = tk.Entry(master)
text22.grid(row=21, column=2, sticky=tk.W)

#23rd entry
tk.Label(master, text="Adjective: ").grid(row=22, column=1, sticky=tk.E) #label for text
text23 = tk.Entry(master)
text23.grid(row=22, column=2, sticky=tk.W)

#24th entry
tk.Label(master, text="Name of event: ").grid(row=23, column=1, sticky=tk.E) #label for text
text24 = tk.Entry(master)
text24.grid(row=23, column=2, sticky=tk.W)

#25th entry
tk.Label(master, text="Adjective: ").grid(row=24, column=1, sticky=tk.E) #label for text
text25 = tk.Entry(master)
text25.grid(row=24, column=2, sticky=tk.W)

#26th entry
tk.Label(master, text="Noun: ").grid(row=25, column=1, sticky=tk.E) #label for text
text26 = tk.Entry(master)
text26.grid(row=25, column=2, sticky=tk.W)

tk.Button(master, text="Submit", command=newWindow).grid(row=27, column=2, sticky=tk.W, pady=4)



master.mainloop()


