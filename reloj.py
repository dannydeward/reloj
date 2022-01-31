from tkinter import Label, Tk
import time


app_window= Tk()
app_window.title("My Reloj Digital")
app_window.geometry("450x300")
app_window.resizable(0,0)

text_font=("Boulder", 50, "bold")
background="#222222"
foreground="#e7d40A"
border_width=100

label=Label(app_window, font=text_font, bg= background, fg=foreground, bd=border_width)

label.grid(row=0,column=1)


def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,digital_clock)



digital_clock()
app_window.mainloop()

