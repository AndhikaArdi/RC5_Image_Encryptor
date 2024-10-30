import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk 
import numpy
import convertor

class Window():
    def __init__(self) -> None: 
    # ========================================================================================================================   
        self.Encryptor_tittle = Label(root,text="IMAGE ENCRYPTOR",font=('Times New Roman',20))

        # Label & Field
        self.label_Key = Label(root,text="Key :")
        self.field_Key = Entry(root,bd=3)
        self.label_Rounds = Label(root,text="Rounds :")
        self.field_Rounds = Entry(root,bd=3)
        self.label_Image = Label(root,text="Image :")
        self.field_Image = Entry(root,bd=3)
        self.label_File = Label(root,text="Save File as :")
        self.field_File = Entry(root,bd=3)
        self.label_Log = Label(root,text="Encrypted Image (part of) :")

        # Button & Log
        self.btn_Image = Button(root,text="Open Image",command=lambda:self.set_text(self.field_Image,self.open_file()))
        self.btn_Encrypt = Button(root,text="Encrypt & Save", command=lambda: self.encrypt_img())

        self.log = Text(root, wrap='none')
        self.log.config(state="disabled")
        
        # PLACING THE WIDGET -------------------------------------------------------------------------------------------------
        self.Encryptor_tittle.place(x=5, y=15)

        self.label_Key.place(x=5,y=65)
        self.field_Key.place(x=10, y=90, width=245)
        self.label_Rounds.place(x=260,y=65)
        self.field_Rounds.place(x=265, y=90, width=100)
        self.label_Image.place(x=5,y=115)
        self.field_Image.place(x=10, y=140, width=355)
        self.label_File.place(x=5,y=165)
        self.field_File.place(x=10, y=190, width=355)
        self.label_Log.place(x=5,y=220)

        self.btn_Image.place(x=380, y=137, width = 90, height = 25)
        self.btn_Encrypt.place(x=380, y=187, width = 90, height = 25)

        self.log.place(x=10, y=245, width = 460, height = 200)
        
    # ========================================================================================================================

    def set_text(self,field,text):
        field.delete(0,'end')
        field.insert(0,text)

    def open_file(self):
        file = filedialog.askopenfilename(title="Select an Image",filetypes=[("Image files","*.jpg")]).replace("/", "\\")
        return file
    
    def encrypt_img(self):
        key = self.field_Key.get()
        rounds = self.field_Rounds.get()
        image_path = self.field_Image.get()
        enc_filename = self.field_File.get()
        mode = 'ECB'

        if key != '' and rounds != '' and image_path != '' and enc_filename != '':
            try:
                rounds = int(rounds)
                
                img = Image.open(image_path) 
                img_Width , img_Height = img.size
                pix = numpy.array(img)
                window , windowsize_r , windowsize_c = convertor.original(pix,img_Width,img_Height)
                enc = convertor.encrypt(window,windowsize_r,windowsize_c,key,rounds,mode)

                self.set_log(enc)

                with open(f'{enc_filename}.txt', 'w') as f:
                    f.write(f"{img_Width},{img_Height},{rounds}\n")
                    f.write(f"{key}\n")

                    enc_string = ' '.join(map(str, enc))
                    f.write(enc_string)
            except ValueError:
                pass

        else :
            pass

    def set_log(self,enc):
        self.log.config(state='normal')
        self.log.delete('1.0','end')

        for i in range(0,25):
            if i % 2 != 0 :
                self.log.insert('end',f"{enc[i-1]} {enc[i]}\n")
            else:
                pass

        self.log.config(state='disabled')



root = tk.Tk()
app = Window()
root.wm_title("Image Encryptor")
root.geometry("485x500")
root.resizable(width = False , height = False) 
root.mainloop()