from tkinter import Frame, Label, Tk

root = Tk()

root.title('AstreaA')
# root.iconbitmap('')
root.geometry("540x960")
root.wm_attributes('-transparentcolor', root['bg'])

my_frame = Frame(root, width=200, height=200)
my_frame.pack(pady=20, ipady=20, ipadx=20)

word = "TODAY'S REPORT"
Label(my_frame, text=word, fg="cyan", font=("Arial",50)).pack()
Label(my_frame, text=word, fg="cyan", font=("Arial",50)).pack()
Label(my_frame, text=word, fg="cyan", font=("Arial",50)).pack()
Label(my_frame, text=word, fg="cyan", font=("Arial",50)).pack()

root.mainloop()