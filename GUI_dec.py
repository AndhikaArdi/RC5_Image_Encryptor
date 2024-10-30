import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk 
import numpy
import convertor

class Window():
    def __init__(self) -> None: 
    # ========================================================================================================================   
        self.Decryptor_tittle = Label(root,text="IMAGE DECRYPTOR",font=('Times New Roman',20))

        # Label & Field
        self.label_File = Label(root,text="Encrypted File :")
        self.field_File = Entry(root,bd=3)
        self.label_Image = Label(root,text="Decrypted Image :")

        # Button & Log
        self.btn_File = Button(root,text="Open File",command=lambda:self.set_text(self.field_File,self.open_file()))
        self.btn_Decrypt = Button(root,text="Decrypt", command=lambda: self.decrypt_img())
        
        # PLACING THE WIDGET -------------------------------------------------------------------------------------------------
        self.Decryptor_tittle.place(x=5, y=15)

        self.label_File.place(x=5, y=65)
        self.field_File.place(x=10, y=90, width=355)
        self.label_Image.place(x=5, y=130)

        self.btn_File.place(x=380, y=87, width = 90, height = 25)
        self.btn_Decrypt.place(x=380, y=123, width = 90, height = 25)
        
    # ========================================================================================================================

    def set_text(self,field,text):
        field.delete(0,'end')
        field.insert(0,text)

    def open_file(self):
        file = filedialog.askopenfilename(title="Select an Image",filetypes=[("text files","*.txt")]).replace("/", "\\")
        return file

    def decrypt_img(self):
        file_path = self.field_File.get()
        mode = 'ECB'

        if file_path != '' :
            with open(file_path, 'r') as f:
                first_line = f.readline().strip()
                img_Width, img_Height, rounds = map(int,first_line.split(','))

                second_line = f.readline().strip()
                key = second_line
                print(key)

                enc_string = f.read()
                enc_list = enc_string.split()


            windowsize_r = img_Height - (img_Height % 2)
            windowsize_c = img_Width - (img_Width % 6)

            res = convertor.decrypt(enc_list, windowsize_r, windowsize_c, key, rounds, mode)

            de_pix = numpy.block(res)
            de_pix = ImageTk.PhotoImage(image=Image.fromarray(de_pix))
            
            panel2 = Label(root, image = de_pix) 
            panel2.image = de_pix 

            panel2.place(x=10, y=160, width = 460, height = 320)

        else :
            pass



root = tk.Tk()
app = Window()
root.wm_title("Image Encryptor")
root.geometry("485x500")
root.resizable(width = False , height = False) 
root.mainloop()