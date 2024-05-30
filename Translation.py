#PythonGeeks GUIDE TO TRANSLATE LANGUAGES USING Google Translate API
import googletrans
from googletrans import Translator
from tkinter import *
from tkinter import messagebox

#Since default options are allowed, we check for 
#explicitly given source and destination languages
def translate_function():
  #check if the source and target languages are empty  
  if (len(src_entry.get("1.0","end-1c"))>1):
    src_v = src_entry.get("1.0","end-1c").lower()
    src_v =src_v.replace(" ","")
  else:
    src_v = None
    
  if (len(dest_entry.get("1.0","end-1c"))>1):
    dest_v = dest_entry.get("1.0","end-1c").lower()
    dest_v =dest_v.replace(" ","")
  else:
    dest_v = None
  #Check if the text is empty. If so, prompt user to key it
  if (len(text_entry.get("1.0","end-1c"))<=1):
    messagebox.showerror(message="Enter valid text")
  else:
  #Send the parameters based on user input provided  
    text_v = text_entry.get("1.0","end-1c")  
    if (not src_v) & (not dest_v):
      translated_text = translator_object.translate(text_v)
    elif (not src_v):
      translated_text = translator_object.translate(text_v,dest=dest_v)
    elif (not dest_v):
      translated_text = translator_object.translate(text_v,src=src_v)
    else:
      translated_text = translator_object.translate(text_v,src=src_v,dest=dest_v)
    #Display translated text on a prompt
    messagebox.showinfo(message = "TRANSLATED TEXT: "+translated_text.text)

#Function to clear the text boxes
def clear():
  dest_entry.delete("1.0","end-1c")
  src_entry.delete("1.0","end-1c")
  text_entry.delete("1.0","end-1c")


#Invoke call to class to view a window
window = Tk()
#Set dimensions of window and title
window.geometry("500x300")
window.title("Language Translator")

#Import the Translator class which will read the input and translate
#Default translation is done by detection of input and to english
translator_object = Translator()
#Title of the app
title_label = Label(window, text="Language Translator",font=("Gayathri", 12)).pack()
#Read inputs
#Text input
text_label = Label(window, text="Text to translate:").place(x=10,y=20)
text_entry = Text(window, width=40, height=5,font=("Ubuntu Mono",12))
text_entry.place(x=130,y=20)
#Source language input
src_label = Label(window, text="Source language (empty: auto-detect):").place(x=10,y=120)
src_entry = Text(window, width=20,height=1,font=("Ubuntu Mono",12))
src_entry.place(x=275,y=120)
#Destination input
dest_label = Label(window, text="Target language (empty: english-default):").place(x=10,y=150)
dest_entry = Text(window, width=20,height=1,font=("Ubuntu Mono",12))
dest_entry.place(x=300,y=150)
#Translate function and clear function activated through buttons
button1 = Button(window,text='Translate', bg = 'Turquoise',command=translate_function).place(x=160,y=190)
button2 = Button(window,text='Clear', bg = 'Turquoise',command=clear).place(x=270,y=190)
#close the app
window.mainloop()



