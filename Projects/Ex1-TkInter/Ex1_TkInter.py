import tkinter as tk

r = tk.Tk()

r.title("Aplikacja")
r.minsize(1000,400)
r.maxsize(1000,400)
button = tk.Button(text = "Wyłącznik", width = 25, command = r.destroy)
button.pack()

r.mainloop()