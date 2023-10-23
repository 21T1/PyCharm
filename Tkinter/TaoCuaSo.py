from tkinter import *
from CenterLib import makeCenter

root = Tk()
root.title("https://google.com")
root.resizable(height=True, width=True)
root.minsize(height=200, width=400)
makeCenter(root)

root.mainloop()