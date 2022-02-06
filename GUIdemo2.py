from tkinter import *
from tkinter import filedialog

#file_path = " "
#branch = " "
root = Tk()
root.geometry("500x200")


def ellhniko():
    global branch
    branch = "ellhniko"
    global file_path
    file_path = filedialog.askopenfilename()
    buttonE.config(state=DISABLED)#DISABLED

buttonE = Button(root, text='Ελληνικό', command = ellhniko)
buttonE.config(font=('Ink Free', 20, 'bold'))
buttonE.config(bg='#bf9000')
buttonE.config(state=ACTIVE)#DISABLED
buttonE.pack()


root.mainloop()
print("text", file_path, branch)
