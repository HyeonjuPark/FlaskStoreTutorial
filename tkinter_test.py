from tkinter import *
class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=RIGHT)

    def say_hi(self):
        # self.hi_there.
        print("hi there, everyone!")

root = Tk()

app = App(root)

root.mainloop()
# root = Tk()
# w = Label(root, text="Hello, world!")
# w.pack()
# root.mainloop()
