from qinter import Tk, Label, Button
from qinter.messagebox import showinfo
root = Tk()
root.title('Test')
root.geometry('500x500')
hello = Label(root, text='hello, World!')
hello.place(x=200, y=200)
btn = Button(root, text='Click Me', command=lambda: showinfo(message='ouch!'))
btn.place(x=200, y=250)
root.mainloop()