'''
Author: Celine Podgornik
Date: 21 June 2022
Description: This program turns an Excel spreadsheet 
of books I want to read into a SQL database created 
and maintained with Python.
'''

#import sqlite3
#import pandas as pd
import tkinter as tk
from tkinter import *
#from bookDatabaseSQL import *

def loadImageHelper(filename):
    
    return PhotoImage(file='Images/'+filename)

def loadMiscImages():

    books_img = loadImageHelper('Books.png')
    
    return [books_img]

def loadCatAvatars():

    pierre_btn = loadImageHelper('Pierre1.png')
    rory_btn = loadImageHelper('Rory1.png')
    inky_btn = loadImageHelper('Inky1.png')
    madison_btn = loadImageHelper('Madison1.png')
    binky_btn = loadImageHelper('Binky1.png')
    booboo_btn = loadImageHelper('Booboo1.png')

    return [pierre_btn, rory_btn, inky_btn, madison_btn, binky_btn, booboo_btn]
    
def loadDialogueImages():

    pierre_bubble = loadImageHelper('PierreDialogue.png')
    rory_bubble = loadImageHelper('RoryDialogue.png')
    inky_bubble = loadImageHelper('InkyDialogue.png')
    madison_bubble = loadImageHelper('MadisonDialogue.png')
    binky_bubble = loadImageHelper('BinkyDialogue.png')
    booboo_bubble = loadImageHelper('BoobooDialogue.png')
    
    return [pierre_bubble, rory_bubble, inky_bubble, madison_bubble, binky_bubble, booboo_bubble]

def assistantHelper(name):
    
    choices = ["Pierre", "Rory", "Inky", "Madison", "Binky", "Booboo"]
    for i in range(len(choices)):
        if choices[i] == name:
            return i        

def setAssistant(frame, name):
    
    assistant = assistantHelper(name)
    loadFrame(frame, helpPage(assistant))

def chooseCat():

    chooseCatFrame = Frame(root)
    chooseCatFrame["bg"] = "skyblue"

    chooseCatFrame.rowconfigure(0, weight=1)
    chooseCatFrame.rowconfigure(1, weight=1)
    chooseCatFrame.rowconfigure(2, weight=1)
    chooseCatFrame.rowconfigure(3, weight=1)
    chooseCatFrame.rowconfigure(4, weight=1)
    chooseCatFrame.columnconfigure(0, weight=1)
    chooseCatFrame.columnconfigure(1, weight=1)
    chooseCatFrame.columnconfigure(2, weight=1)
    
    # welcome message
    Label(chooseCatFrame, 
          bg= 'skyblue', 
          text= "Welcome to", 
          font= ('Comic Sans MS', 25, 'bold italic')).grid(row=0, column=0, columnspan=3, sticky="S")
    Label(chooseCatFrame, 
          bg= 'skyblue', 
          text= "The Library of Celine!", 
          font= ('Comic Sans MS', 35, 'bold italic')).grid(row=1, column=0, columnspan=3, sticky="N")
    
    # buttons to choose which cat will be the assistant
    # upon choosing the assistant, the user will be taken to the search page
    Button(chooseCatFrame, 
           image= catAvatars[0], 
           height= 125, 
           width= 125, 
           command= lambda: setAssistant(chooseCatFrame, "Pierre")).grid(row=2, column=0, sticky="E")
    Button(chooseCatFrame, 
           image= catAvatars[1], 
           height= 125, 
           width= 125, 
           command= lambda: setAssistant(chooseCatFrame, "Rory")).grid(row=2, column=1)
    Button(chooseCatFrame, 
           image= catAvatars[2], 
           height= 125, 
           width= 125, 
           command= lambda: setAssistant(chooseCatFrame, "Inky")).grid(row=2, column=2, sticky="W")
    Button(chooseCatFrame, 
           image= catAvatars[3], 
           height= 125, 
           width= 125, 
           command= lambda: setAssistant(chooseCatFrame, "Madison")).grid(row=3, column=0, sticky="E")
    Button(chooseCatFrame, 
           image= catAvatars[4], 
           height= 125, 
           width= 125, 
           command= lambda: setAssistant(chooseCatFrame, "Binky")).grid(row=3, column=1)
    Button(chooseCatFrame, 
           image= catAvatars[5], 
           height= 125, 
           width= 125, 
           command= lambda: setAssistant(chooseCatFrame, "Booboo")).grid(row=3, column=2, sticky="W")      
    Label(chooseCatFrame, 
          bg= 'skyblue', 
          text= "Choose your assistant", 
          font= ('Comic Sans MS', 15, 'bold italic')).grid(row=4, column=0, columnspan=3, sticky="N")
          
    return chooseCatFrame

def helpPage(assistant):
    
    helpFrame = Frame(root)
    helpFrame["bg"] = "skyblue"
    
    helpFrame.rowconfigure(0, weight=1)
    helpFrame.rowconfigure(1, weight=1)
    helpFrame.rowconfigure(2, weight=1)
    helpFrame.rowconfigure(3, weight=1)
    helpFrame.rowconfigure(4, weight=1)
    helpFrame.rowconfigure(5, weight=1)
    helpFrame.columnconfigure(0, weight=1)
    helpFrame.columnconfigure(1, weight=1)
    helpFrame.columnconfigure(2, weight=1)
    
    # images of books at top of interface
    for i in range(3):
        Label(helpFrame, 
              bg= 'skyblue', 
              image = miscImages[0]).grid(row=0, column=i)#, columnspan=3) 
    
    # help, add recommendation, and home buttons
    Button(helpFrame,
           text = "Search for a Book",
           font= ('Comic Sans MS', 10, 'bold italic'),
           command= lambda: searchButton(helpFrame, assistant)).grid(row=1, column=0)
    Button(helpFrame,
           text = "Make a Recommendation",
           font= ('Comic Sans MS', 10, 'bold italic')).grid(row=2, column=0)
    Button(helpFrame,
           text = "Home",
           command = lambda: loadFrame(helpFrame, chooseCat()),
           font= ('Comic Sans MS', 10, 'bold italic')).grid(row=3, column=0)

    # cat assistant info
    Label(helpFrame,
          bg = "skyblue",
          image = dialogueImages[assistant]).grid(row=1, column = 1, sticky="SE", rowspan=2)  
    Label(helpFrame,
          image = catAvatars[assistant]).grid(row=3, column = 1, sticky="NE")    
    
    return helpFrame

def searchButton(frame, assistant):
 
    loadFrame(frame, searchPage(assistant))

def searchPage(assistant):

    searchFrame = Frame(root)
    searchFrame["bg"] = "skyblue"
    
    options = ["TBR", "Read"]
    variable = StringVar(root)
    variable.set("Choose an option")
    
    w = OptionMenu(root, variable, *options)
    w.pack()
    
    Button(searchFrame,
           text = "Home",
           command = lambda: loadFrame(searchFrame, chooseCat()),
           font= ('Comic Sans MS', 10, 'bold italic')).grid(row=3, column=0)
    
    Label(searchFrame, 
          bg= 'skyblue', 
          text= "Your assistant is:", 
          font= ('Comic Sans MS', 25, 'bold italic')).grid(row=0, column=0, columnspan=3, sticky="S")
          
    Label(searchFrame,
          image = catAvatars[assistant]).grid(row=3, column = 1, sticky="NE")       
    
    return searchFrame

def loadFrame(oldFrame, newFrame):
    
    if oldFrame != "none":
        oldFrame.destroy()
    newFrame.pack(fill="both", expand=True)
 
# initializes the interface
root = Tk()
root.title("The Library of Celine")
root.geometry("1000x700")
root['bg']='skyblue'

# loads the pictures
catAvatars = loadCatAvatars()
dialogueImages = loadDialogueImages()
miscImages = loadMiscImages()

# starts the interface  
loadFrame("none", chooseCat()) 

# keeps the interface open until manually closed   
root.mainloop()

