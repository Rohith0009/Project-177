from tkinter import *

root = Tk()
root.title("Thing")
root.geometry("700x700")
root.configure(bg="pale green")

name = ""
password = ""
captcha = ""

LabName = Label(root, text="Name: ", font=("Arial", 20), bg="pale green")
entryName = Entry(root, font=("Arial", 20))

LabName.place(anchor=CENTER, relx=0.315, rely=0.05)
entryName.place(anchor=CENTER, relx=0.6, rely=0.05)


LabPassword = Label(root, text="Password: ", font=("Arial", 20), bg="pale green")
entryPassword = Entry(root, font=("Arial", 20))

LabPassword.place(anchor=CENTER, relx=0.285, rely=0.15)
entryPassword.place(anchor=CENTER, relx=0.6, rely=0.15)


LabCaptcha = Label(root, text="Captcha: ", font=("Arial", 20), bg="pale green")
entryCaptcha = Entry(root, font=("Arial", 20))

LabCaptcha.place(anchor=CENTER, relx=0.295, rely=0.25)
entryCaptcha.place(anchor=CENTER, relx=0.6, rely=0.25)


LabelName = Label(root, text="", font=("Arial", 20), bg="pale green")
LabelPassword = Label(root, text="", font=("Arial", 20), bg="pale green")
LabCaptcha = Label(root, text="", font=("Arial", 20), bg="pale green")

LabelName.place(anchor=CENTER, relx=0.5, rely=0.55)
LabelPassword.place(anchor=CENTER, relx=0.5, rely=0.65)
LabCaptcha.place(anchor=CENTER, relx=0.5, rely=0.75)


def update():
    global name, password, captcha

    name = entryName.get()
    password = entryPassword.get()
    captcha = entryCaptcha.get()


def showProfile():
    LabelName["text"] = f"Name: {name}"
    LabelPassword["text"] = f"Password: {password}"
    LabCaptcha["text"] = f"Captcha: {captcha}"


BtnUpdate = Button(
    root,
    text="Update Login Details",
    font=("Arial", 20),
    bg="pale turquoise",
    command=update,
)
BtnUpdate.place(anchor=CENTER, relx=0.3, rely=0.45)

BtnShow = Button(
    root,
    text="Show Profile",
    font=("Arial", 20),
    bg="pale turquoise",
    command=showProfile,
)
BtnShow.place(anchor=CENTER, relx=0.75, rely=0.45)

root.mainloop()
