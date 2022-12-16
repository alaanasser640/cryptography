

from tkinter import *
from tkinter import ttk
def main():
    txt.delete(0.0,'end')
    key=ent2.get()
    key=key.replace(" ", "")
    key=key.upper()
    crypto = var_chk.get()
    text = ent1.get()
    def create_matrix(key):
        key = key.upper()
        matrix = [[0 for i in range (5)] for j in range(5)]
        letters_added = []
        row = 0
        col = 0
        # add the key to the matrix
        for letter in key:
            if letter not in letters_added:
                matrix[row][col] = letter
                letters_added.append(letter)
            else:
                continue
            if (col==4):
                col = 0
                row += 1
            else:
                col += 1
        #Add the rest of the alphabet to the matrix
        # A=65 ... Z=90
        for letter in range(65,91):
            if letter==74: # I/J are in the same position
                    continue
            if chr(letter) not in letters_added: # Do not add repeated letters
                letters_added.append(chr(letter))
                
        #print (len(letters_added), letters_added)
        index = 0
        for i in range(5):
            for j in range(5):
                matrix[i][j] = letters_added[index]
                index+=1
        return matrix

    def separate_same_letters(message):
        index = 0
        while (index<len(message)):
            l1 = message[index]
            if index == len(message)-1:
                message = message + 'X'
                index += 2
                continue
            l2 = message[index+1]
            if l1==l2:
                message = message[:index+1] + "X" + message[index+1:]
            index +=2   
        return message

    def indexOf(letter,matrix):
        for i in range (5):
            try:
                index = matrix[i].index(letter)
                return (i,index)
            except:
                continue

    def indexOf(letter,matrix):
        for i in range (5):
            try:
                index = matrix[i].index(letter)
                return (i,index)
            except:
                continue
    #Implementation of the playfair cipher
    #If encrypt=True the method will encrypt the message
    # otherwise the method will decrypt
    def playfair(key, message, encrypt=True):
        inc = 1
        if encrypt==False:
            inc = -1
        matrix = create_matrix(key)
        message = message.upper()
        message = message.replace(' ','')    
        message = separate_same_letters(message)
        cipher_text=''
        for (l1, l2) in zip(message[0::2], message[1::2]):
            row1,col1 = indexOf(l1,matrix)
            row2,col2 = indexOf(l2,matrix)
            if row1==row2: #Rule 2, the letters are in the same row
                cipher_text += matrix[row1][(col1+inc)%5] + matrix[row2][(col2+inc)%5]
            elif col1==col2:# Rule 3, the letters are in the same column
                cipher_text += matrix[(row1+inc)%5][col1] + matrix[(row2+inc)%5][col2]
            else: #Rule 4, the letters are in a different row and column
                cipher_text += matrix[row1][col2] + matrix[row2][col1]
        
        return cipher_text
    
    if crypto == 1:
        cipher = playfair(key, text)
        txt.insert(0.0,cipher.upper())
    else:
        cipher = playfair(key, text,False)
        cipher = cipher.upper()
        txt.insert(0.0,cipher.replace('X', ''))
    

root = Tk()
root.geometry("700x600")
root.configure(bg='aquamarine')

#Creating Widgts


cryptography = Label(root , text = "PlayFair Cipher",font=('Arial 18'),bg='aquamarine', foreground = 'gray')
message = Label(root , text = "Message:",font=('Arial 14'),bg='aquamarine',foreground = 'gray')
keyBtn = Label(root , text = "key:",font=('Arial 14'),bg='aquamarine',foreground = 'gray')

ent1 = Entry(root, width = 40,font=('Arial 18'))
ent2 = Entry(root, width = 40,font=('Arial 18'))

var_chk = IntVar()



rb1 = Radiobutton(root , text = "encrypt" , variable = var_chk , value = 1,font=('Arial 14'),bg='aquamarine',foreground = 'gray')
rb2 = Radiobutton(root , text = "decrypt" , variable = var_chk , value = 2,font=('Arial 14'),bg='aquamarine',foreground = 'gray')

bt = Button(root , text = "Submit" , bg = "gray" , fg= "white" ,  command = main,font=('Arial 14'),border=0,activeforeground = 'black',activebackground ='aquamarine')

txt = Text(root , width = 37 , height = 8 , wrap = WORD,font=('Arial 14'))


#Placing them on screen
cryptography.place(x=280, y=30)
message.place(x=10, y=100)
keyBtn.place(x=10, y=150)

ent1.place(x=120, y=100)
ent2.place(x=120, y=150)

rb1.place(x=150, y=200)
rb2.place(x=450, y=200)

bt.place(x=290, y=250)

txt.place(x=140, y=330)

root.mainloop()        