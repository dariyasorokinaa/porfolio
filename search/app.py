import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser

app = tk.Tk()
app.title("Searching")

app.configure(background="yellow")

app_name = ttk.Label(app, text="Поисковое приложение", font="Roboto 18 bold", foreground="red")
app_name.grid(row=0, column=0)

search_label = ttk.Label(app, text="Search")
search_label.grid(row=1, column=0)

text_field = ttk.Entry(app, width=50)
text_field.grid(row=1, column=1)

search_engine = StringVar()
search_engine.set("yandex")

def search():
    if text_field.get().strip() != "":
        if search_engine.get() == "google":
            webbrowser.open('https://www.google.com/search?q=' + text_field.get())
        elif search_engine.get() == "yandex":
            webbrowser.open('https://yandex.ru/search/?lr=10716&text=' + text_field.get())

def searchBtn():
    search()

def enter_button(event):
    search()


btn_search = ttk.Button(app, text="Find", width=10, command=search)
btn_search.grid(row=1, column=3)

text_field.bind('<Return>', enter_button)

radio_google = ttk.Radiobutton(app, text="Google", value="google", variable=search_engine)
radio_yandex = ttk.Radiobutton(app, text="Yandex", value="yandex", variable=search_engine)

radio_google.grid(row=3, column=1, sticky=W)
radio_yandex.grid(row=3, column=1, sticky=E)

app.wm_attributes('-topmost', True)

text_field.focus()

app.mainloop()
