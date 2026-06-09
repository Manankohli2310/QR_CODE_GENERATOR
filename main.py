# importing modules
import qrcode
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


# define function
def createQR(*args):
    data = text_entry.get()

    if data:
        img = qrcode.make(data) # QR CODE MAKING
        resized_img= img.resize((270, 240))
        tkimage= ImageTk.PhotoImage(resized_img)
        qr_canvas.delete("all")
        qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage
    else:
        messagebox.showwarning("Error", "URL Not Found")

def saveQR (*args):
    data = text_entry.get()

    if data:
        img = qrcode.make(data)  # QR CODE MAKING
        resized_img = img.resize((270, 240))

        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            resized_img.save(path)
            messagebox.showinfo("Sucess", "QR Code Saved")
    else:
        messagebox.showwarning("Error", "URL Not Found")



# GUI CODE
root= tk.Tk()
root.title("OR Code Generator")
root.geometry("300x400") # w x h
root.config(bg="#404040")
root.resizable(0,0)
root.iconbitmap("frame.ico")


# creating frame
frame1 = tk.Frame(root)
frame1.place(x=14,y=15, width=270, height=240)

frame2 = tk.Frame(root, bg="white")
frame2.place(x=23,y=263, width=250, height=100)

# logo
cover_img= tk.PhotoImage(file="QR Code Generator.png")
qr_canvas= tk.Canvas(frame1)
qr_canvas.create_image(0,0, anchor=tk.NW, image=cover_img)
qr_canvas.image=cover_img
qr_canvas.bind("<Double-1>",saveQR)
qr_canvas.pack(fill=tk.BOTH)

# text entry
text_entry= ttk.Entry(frame2, width = 21, font=("Sitka 11"), justify=tk.CENTER)
text_entry.bind("<Return>", createQR)
text_entry.place(x=55, y=13)


# label

url = tk.Label(frame2, text="URL", bg="white", font="Bold 13")
url.place(x=13, y=13)


# buttton
btn_1 = ttk.Button(frame2, text="Create", width=10, command=createQR)
btn_1.place(x=10, y=53)

btn_2 = ttk.Button(frame2, text="Save", width=10, command=saveQR)
btn_2.place(x=89.5, y=53)

btn_3 = ttk.Button(frame2, text="Exit", width=10, command=root.quit)
btn_3.place(x=169, y=53)



root.mainloop()


