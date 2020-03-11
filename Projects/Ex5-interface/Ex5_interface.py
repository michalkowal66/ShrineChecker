import tkinter as tk

window = tk.Tk()
window.title("Logowanie")
window.minsize(500, 200)
window.maxsize(500, 200)

welcome = tk.Label(window, text = "Hi! Log in to your account using 'login' button or create new account with 'register' button.")
welcome.pack()

idlabel = tk.Label(window, text = "Login:")
idlabel.pack()
id = tk.Entry(window)
id.pack()
pwlabel = tk.Label(window, text = "Password:")
pwlabel.pack()
pw = tk.Entry(window, show="*")
pw.pack()

login = tk.Button(window, text = "Login")
login.pack()
login.place(height = 30, width = 80, x = 150, y = 120)

register = tk.Button(window, text = "Register")
register.place(height = 30, width = 80, x = 270, y = 120)

close = tk.Button(window, text = "Close", command = window.destroy)
close.place(height = 30, width = 80, x = 210, y = 160)

tk.mainloop()