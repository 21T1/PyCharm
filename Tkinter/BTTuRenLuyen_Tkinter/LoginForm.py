from tkinter import *


def clrAction():
    strOldP.set("")
    strNewP.set("")
    strNewP2.set("")


root = Tk()

strOldP = StringVar()
strNewP = StringVar()
strNewP2 = StringVar()

root.title("Enter New Password")
root.minsize(width=250, height=150)

Label(root, text="Old Password").grid(row=0, column=0, sticky="w")
Entry(root, width=20, show="*", textvariable=strOldP).grid(row=0, column=1)

Label(root, text="New Password").grid(row=1, column=0, sticky="w")
Entry(root, width=20, show="*", textvariable=strNewP).grid(row=1, column=1)

Label(root, text="Enter New Password Again").grid(row=2, column=0)
Entry(root, width=20, show="*", textvariable=strNewP2).grid(row=2, column=1)

SubmitBtn = Frame(root)
Button(SubmitBtn, width=5, text="OK", command=root.quit).pack(side=LEFT, pady=5, padx=1)
Button(SubmitBtn, width=5, text="Cancel", command=clrAction).pack(side=LEFT, pady=5, padx=1)
SubmitBtn.grid(row=3, columnspan=2)

root.mainloop()