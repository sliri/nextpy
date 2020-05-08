# 6.1.3
################

import tkinter as tk


def open_image(image_label):
    img = tk.PhotoImage(file='capture.png')
    image_label.image = img
    image_label.configure(image=img)


window = tk.Tk()
label = tk.Label(text="This is window label", fg="red", font=20)
label.pack()

image_label = tk.Label(text='this is image label')
image_label.pack(side="bottom", fill="both", expand='yes')

button = tk.Button(text ="click to find out",command=lambda:open_image(image_label))
button.pack()
window.mainloop()