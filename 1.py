from tkinter import *

#### Key down function
def click():
    entered_text=textentry.get() #this will collect the text from the textbox
#### main
window = Tk()
window.title("MY TKINTER")
window.configure(bg="black")
print('Hello')
#### my photo
photo1 = PhotoImage(file="C:\\Users\\ADMIN\\Desktop\\project\\Label.gif")
Label(window, image=photo1, bg="black") .grid(row=0, column=0, sticky=W)

#### create label
Label (window, text="Enter Your Name:", bg="white", fg="black", font="none 12 bold") .grid(row=1, column=0, sticky=W)

#### Create a text entry box
textentry = Entry(window, width=15, bg="white")
textentry.grid(row=1, column=1, sticky=W)

#### add a submit button
Button(window, text="SUBMIT", width=6, command=click) .grid(row=2, column=0, sticky=W)

                    
#### run main loop
window.mainloop()
