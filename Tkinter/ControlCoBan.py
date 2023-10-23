from tkinter import *

root = Tk()
root.title("Control cơ bản")
root.resizable(height=True, width=True)
root.minsize(width=300, height=300)

e = StringVar()
e.set("https://google.com")
Entry(root, textvariable=e, width=30).pack()

Label(root,
      text="Google Chrome",
      fg="red", justify=CENTER).pack()

Button(root, text="Exit", command=root.quit).pack()

photo = PhotoImage(file="images/chrome.png")
Label(root, image=photo, relief=SUNKEN).pack(side=LEFT, padx=5)

root.mainloop()