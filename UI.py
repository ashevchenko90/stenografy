from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from stegano import exifHeader
import os

window = Tk()
window.title("Password Keeper")
window.geometry('560x300')
window.config(padx=20, pady=20)

image_to_use = None
font = ("Courier", 24)


def hide_password():
    try:
        message = message_input.get()
        image_in = image_to_use

        image_out = f'{os.path.dirname(image_in)}/{output_file_name.get()}.jpeg'
        exifHeader.hide(image_in, image_out, message)
        message_input.delete(0, END)
        output_file_name.delete(0, END)
        messagebox.showinfo(title='Important', message='Password Saved')
        # image_label.config(text='DONE!')
        # generate_btn['state'] = DISABLED
    except TypeError:
        return

def show_password():
    secret_message_show = ''
    try:
        secret_message_show = exifHeader.reveal(image_to_use).decode()
    except KeyError:
        secret_message_show = "No secrets in this image."
    except AttributeError:
        return
    show_msg.config(text=secret_message_show)


def select_files():
    global image_to_use
    filetypes = (
        ('image', '*.JPG *.jpg *.JPEG *.jpeg'),
    )
    filename = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    if type(filename) == tuple:
        filename = filename[0]
    image_to_use = filename
    image_label.config(text=image_to_use)


open_button = Button(
    window,
    text='Open Files',
    command=select_files
)
open_button.grid(column=0, row=0)

image_label = Label()
image_label.grid(column=1, row=0)


logo = Label(text="- Hide Password -")
logo.grid(column=0, row=1, columnspan=2)
logo.config(font=font)

message_label = Label(text='Password:')
message_label.grid(column=0, row=2)

message_input = Entry(width=40)
message_input.grid(column=1, row=2)

output_file_name_label = Label(text='Output Image Name:')
output_file_name_label.grid(column=0, row=3)

output_file_name = Entry(width=40)
output_file_name.grid(column=1, row=3)

generate_btn = Button(text='Hide Password', command=hide_password)
generate_btn.grid(column=0, row=4, pady=10, columnspan=2)

logo2 = Label(text="- Show Password -")
logo2.grid(column=0, row=5, columnspan=2)
logo2.config(font=font)

read_btn = Button(text='Show Password', command=show_password)
read_btn.grid(column=0, row=6, pady=10, columnspan=2)

show_msg_label = Label(text="Hidden Password:")
show_msg_label.grid(column=0, row=7)

show_msg = Label()
show_msg.grid(column=1, row=7)


window.mainloop()