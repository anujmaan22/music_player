#setup screen=-
#tkinder is used for gui
from tkinter import *
from PIL import Image,ImageTk
#pygame and mixer used for import music and use functions
from pygame import mixer
mixer.init()
class musicplayer:
    def __init__(self, Tk, x=None):
        self.root=Tk
        self.root.title('music_player')
        self.root.geometry('400x400')
        self.root.configure(background='sky blue')
        #add lable---
        self.label=Label(text='Listen ad free music with Amaan premium for free ').place(x=50,y=30)
        self.label1=Label(self.root,text='special for PARU RAJ SIR.',bg='black',fg='white',font=15)
        self.label1.pack(side=BOTTOM,fill=x)
        #adding image
        self.photo=ImageTk.PhotoImage(file='spotify.jpeg')
        photo = Label(self.root, image =self.photo).place(x=50,y=50)

        #functions for work for buttons
        def playmusic():
            mixer.music.load('Goli.mp3')
            mixer.music.play()
            self.label1['text']='goli song playing for sir..'

        #creating buttons--
        #play button--
        self.photo_B1=ImageTk.PhotoImage(file='play_new.jpeg')
        photo_b1=Button(self.root,image=self.photo_B1,bd=0,bg='blue',command=playmusic).place(x=50,y=250)

        #function for pause
        def stopmusic():
            mixer.music.stop()
            self.label1['text']='aapne bnd kr diya sir..'

        # pause button--
        self.photo_B2 = ImageTk.PhotoImage(file='pause_2.jpeg')
        photo_b2 = Button(self.root, image=self.photo_B2, bd=0, bg='blue',command=stopmusic ).place(x=150, y=250)

       #function for next
        def nextmusic():
            mixer.music.load('Past-Future-Miel.mp3')
            mixer.music.play()
            self.label1['text']='past future playing..'
        #next music

        self.photo_B3 = ImageTk.PhotoImage(file='next.jpeg')
        photo_b3 = Button(self.root, image=self.photo_B3, bd=0, bg='blue', command=nextmusic).place(x=250, y=250)
root=Tk()    #for close this
obj=musicplayer(root)
root.mainloop() #for close this window