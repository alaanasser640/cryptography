from tkinter import *
from tkinter import ttk

def main():
    monoalpha_cipher = {

        'a': 'm',
        'b': 'n',
        'c': 'b',
        'd': 'v',
        'e': 'c',
        'f': 'x',
        'g': 'z',
        'h': 'a',
        'i': 's',
        'j': 'd',
        'k': 'f',
        'l': 'g',
        'm': 'h',
        'n': 'j',
        'o': 'k',
        'p': 'l',
        'q': 'p',
        'r': 'o',
        's': 'i',
        't': 'u',
        'u': 'y',
        'v': 't',
        'w': 'r',
        'x': 'e',
        'y': 'w',
        'z': 'q',
        ' ': ' ',
        
    }
    txt.delete(0.0,'end')
    crypto = var_chk.get()
    inverse_monoalpha_cipher = {}
    for key, value in monoalpha_cipher.items():
        inverse_monoalpha_cipher[value] = key
   # print(inverse_monoalpha_cipher)
    message = ent1.get()
    if crypto == 1:
        encrypted_message = []
        for letter in message:
            encrypted_message.append(monoalpha_cipher.get(letter, letter))
        txt.insert(0.0,encrypted_message)
    #print(''.join(encrypted_message)) 
    else:  
        encrypted_message = ent1.get()

        decrypted_message = []
        for letter in encrypted_message:
            decrypted_message.append( inverse_monoalpha_cipher.get(letter, letter))
            
       
        txt.insert(0.0,decrypted_message )


root = Tk()
root.geometry("700x600")
root.configure(bg='aquamarine')

#Creating Widgts
cryptography = Label(root , text = "Monoalphapytic Cipher",font=('Arial 14'),bg='aquamarine')
message = Label(root , text = "Message:",font=('Arial 14'),bg='aquamarine')


ent1 = Entry(root, width = 47,font=('Arial 14'))


var_chk = IntVar()



rb1 = Radiobutton(root , text = "encrypt" , variable = var_chk , value = 1,font=('Arial 14'),bg='aquamarine')
rb2 = Radiobutton(root , text = "decrypt" , variable = var_chk , value = 2,font=('Arial 14'),bg='aquamarine')

bt = Button(root , text = "Submit" , bg = "gray" , fg= "white" ,  command = main,font=('Arial 14'))

txt = Text(root , width = 37 , height = 12 , wrap = WORD,font=('Arial 14'))


#Placing them on screen
cryptography.place(x=280, y=30)
message.place(x=10, y=100)

ent1.place(x=120, y=100)

rb1.place(x=150, y=200)
rb2.place(x=450, y=200)

bt.place(x=290, y=250)

txt.place(x=130, y=300)

root.mainloop()    