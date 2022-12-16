from tkinter import *
from tkinter import ttk
def main():
    txt.delete(0.0,'end')
    crypto = var_chk.get()
    string = ent1.get()
    key = ent2.get()
   
    
    def generateKey(string, key): 
        key = list(key) 
        if len(string) == len(key): 
            return(key) 
        else: 
            for i in range(len(string) -len(key)): 
                key.append(key[i % len(key)]) 
        return("" . join(key)) 
    
    def encryption(string, key): 
        encrypt_text = [] 
        for i in range(len(string)): 
            x = (ord(string[i]) +ord(key[i])) % 26
            x += ord('A') 
            encrypt_text.append(chr(x)) 
        return("" . join(encrypt_text)) 
    def decryption(encrypt_text, key): 
        orig_text = [] 
        for i in range(len(encrypt_text)): 
            x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
            x += ord('A') 
            orig_text.append(chr(x)) 
        return("" . join(orig_text)) 
        
    key = generateKey(string, key) 

    if crypto == 1:
        encrypt_text = encryption(string.upper(),key.upper()) 
        txt.insert(0.0,encrypt_text)
    else:    
        encrypt_text = decryption(string.upper(),key.upper()) 
        txt.insert(0.0,encrypt_text)
   

root = Tk()
root.geometry("700x600")
root.configure(bg='aquamarine')

#Creating Widgts
cryptography = Label(root , text = "Polyalphapytic Cipher",font=('Arial 14'),bg='aquamarine')
message = Label(root , text = "Message:",font=('Arial 14'),bg='aquamarine')
keyBtn = Label(root , text = "key:",font=('Arial 14'),bg='aquamarine')

ent1 = Entry(root, width = 47,font=('Arial 14'))
ent2 = Entry(root, width = 47,font=('Arial 14'))

var_chk = IntVar()



rb1 = Radiobutton(root , text = "encrypt" , variable = var_chk , value = 1,font=('Arial 14'),bg='aquamarine')
rb2 = Radiobutton(root , text = "decrypt" , variable = var_chk , value = 2,font=('Arial 14'),bg='aquamarine')

bt = Button(root , text = "Submit" , bg = "gray" , fg= "white" ,  command = main,font=('Arial 14'))

txt = Text(root , width = 37 , height = 12 , wrap = WORD,font=('Arial 14'))


#Placing them on screen
cryptography.place(x=280, y=30)
message.place(x=10, y=100)
keyBtn.place(x=10, y=150)

ent1.place(x=120, y=100)
ent2.place(x=120, y=150)

rb1.place(x=150, y=200)
rb2.place(x=450, y=200)

bt.place(x=290, y=250)

txt.place(x=130, y=300)

root.mainloop()



