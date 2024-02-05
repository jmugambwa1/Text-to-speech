import tkinter as tk
from tkinter import *
import pyttsx3

engine=pyttsx3.init()

def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()
    

root = Tk()  # Initialize the Tk instance

textv = StringVar()

obj = LabelFrame(root, text="Text to Speech", font=20, bd=1)
obj.pack(fill="both", expand=True, padx=10, pady=10)

lb1 = Label(obj, text='Text', font=('ariel', 30))
lb1.pack(side=tk.LEFT, padx=5)

text = Entry(obj, textvariable=textv, width=25, font=30, bd=5)
text.pack(side=tk.LEFT, padx=10)

btn = Button(obj, text="Speak", font=20, bg="black", fg="white", command=speaknow)
btn.pack(side=tk.RIGHT, padx=10)

root.title("Text To Speech")
root.geometry("500x300")
root.resizable(False, False)
root.mainloop()
