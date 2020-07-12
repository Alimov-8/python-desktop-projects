from tkinter import *
from PIL import ImageTk, Image

# Main Window
window = Tk()
window.title("Image Viewer")
window.iconbitmap('D:/Abdulloh/Inha University/Python Language/Auto School '
                  'Tkinter/icons/Wwalczyszyn-Android-Style-Honeycomb-Calculator.ico')


# Functions
def forward(img_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()

    my_label = Label(image=img_list[img_num-1])
    button_forward = Button(window, text=">>", command=lambda: forward(img_num+1),
                            font=("times new roman", 15), bg="black", fg="white")
    button_back = Button(window, text="<<",
                         font=("times new roman", 15), bg="black", fg="white",
                         command=lambda: back(img_num-1))

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(img_num):
    global my_label
    global button_forward
    global button_back
    global status
    my_label.grid_forget()

    my_label = Label(image=img_list[img_num-1])
    button_forward = Button(window, text=">>", command=lambda: forward(img_num+1),
                            font=("times new roman", 15), bg="black", fg="white")
    button_back = Button(window, text="<<",
                         font=("times new roman", 15), bg="black", fg="white",
                         command=lambda: back(img_num-1))

    status = Label(window, text="Image "+str(img_num) + " of " + str(len(img_list)), relief=SUNKEN, anchor=E,
                   font=("times new roman", 10))
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


# Image
img1 = ImageTk.PhotoImage(Image.open("D:/Abdulloh/Inha University/Python "
                                     "Language/Auto School Tkinter/images/bg1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("D:/Abdulloh/Inha University/Python "
                                     "Language/Auto School Tkinter/images/bg2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("D:/Abdulloh/Inha University/Python "
                                     "Language/Auto School Tkinter/images/bg3.jpg"))
img_list = [img1, img2, img3]


# Labels
my_label = Label(image=img1)
status = Label(window, text="Image 1 of " + str(len(img_list)), relief=SUNKEN, anchor=E,
               font=("times new roman", 10))

# Button
button_quit = Button(window, text='Exit Program',
                     font=("times new roman", 15), command=window.quit, bg="black", fg="white")
button_back = Button(window, text="<<",
                     font=("times new roman", 15), bg="black", fg="white", command=back)
button_forward = Button(window, text=">>",
                        font=("times new roman", 15), bg="black", fg="white", command=lambda: forward(2))


# Showing on Window
my_label.grid(row=0, column=0, columnspan=3)
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


window.mainloop()