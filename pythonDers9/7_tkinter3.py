from tkinter import *
window=Tk()
window.title("merhaba")
lbl=Label(window, text="Merhaba")
lbl2=Label(window, text="Merhaba", font=("arial bold", 50))
lbl.grid(column=0, row=0)
lbl2.grid(column=1, row=0)
window.geometry('500x400')
btn=Button(window, text="tıkla")
btn.grid(column=1, row=1)
def tiklandi():
    lbl.configure(text="butona tıklandı")

btn2=Button(window, text="tıkla renkli",
              bg="orange", fg="red",
              width=10, height=10,
              command=tiklandi
              )
btn2.grid(column=1, row=3)
window.mainloop()