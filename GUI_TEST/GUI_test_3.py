from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hintLabel = Label(self,text='Please input your name:')
        self.hintLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.helloButton = Button(self, text='Hello', command=self.hello)
        self.helloButton.pack()
        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello , %s !'% name)

app=Application()
app.master.title('Hello,world')
app.mainloop()
