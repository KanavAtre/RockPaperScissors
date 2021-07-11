from tkinter import *
import tkinter.messagebox
import tkinter.font as tkfont
from PIL import Image, ImageTk
from tkinter import messagebox
import imageio
import tkinter as threading
from mysql.connector.connection import MySQLConnection
import tkvideo
import random
from threading import Timer
import time
from playsound import playsound
from getpass import getpass
from mysql.connector import connect, Error
import mysql.connector as con 


Rock_Paper_scissors = Tk()

label_block= Label(Rock_Paper_scissors)

list_of_optn=['Rock', 'Paper', 'Scissors']

label_video =Label(Rock_Paper_scissors)

rand_choice=random.choice(list_of_optn)

fontsize5=tkfont.Font(family="Georgia", size=18)

final_choice=''

choice=''

answer=''

choice_label=Label(Rock_Paper_scissors, text='The bot chose '+ str(rand_choice), font=fontsize5)

def user_choice(option):
    choice=''
    choice=choice+str(option)
    result=messagebox.askquestion("Alert","You have chosen "+choice+", Confirm? ")

    if result == "yes":
        fontsize6=tkfont.Font(size='16')
        alert_label= Label(Rock_Paper_scissors, text='The bot is choosing...', fg='grey', font=fontsize6)
        alert_label.place(x=400, y=550)
        label_video =Label(Rock_Paper_scissors)
        label_video.place(x=400, y=250)
        player = tkvideo.tkvideo("/Users/thispc/Documents/College core work/projects /Imagesnvideo/RPReplay_Final1621845129.mov", label_video, loop = 1, size = (180,250))
        player.play()


        def bot_choice2():
            fontsize5=tkfont.Font(family="Georgia", size=18)
            # bot_choice=random.choice(list_of_optn)
            choice_label=Label(Rock_Paper_scissors, text='The bot chose '+ str(rand_choice), font=fontsize5)
            choice_label.configure(text='The bot chose '+ str(rand_choice))
            choice_label.place(x=400, y=580)
            alert_label.place(x=5000, y=8000)

        
        t=Timer(4,bot_choice2)
        t.start()

        def video_block():

            if choice!='':
                label_video.place(x=10000, y=10000)

        def final_output():

            if rand_choice==choice:

                output_value="tie!"

                messagebox.showinfo("Answer1",output_value)


            elif rand_choice=='Rock' and choice=='Paper':


                output_value='You Win!'

                messagebox.showinfo("Answer2",output_value)

        
            elif rand_choice=='Rock' and choice=='Scissors':


                output_value='You Lose'

                messagebox.showinfo("Answer3",output_value)

            elif rand_choice=='Paper' and choice=='Scissors': 



                output_value='You Win!'

                messagebox.showinfo("Answer4",output_value)

            elif rand_choice=='Paper' and choice=='Rock':

                output_value='You Lose!'

                messagebox.showinfo("Answer5",output_value)

            elif rand_choice=='Rock' and choice=='Scissors':


                output_value='You Lose!'

                messagebox.showinfo("Answer6",output_value)
    
            elif rand_choice=='Paper' and choice=='Scissors':


                output_value='You Win !'

                messagebox.showinfo("Answer7",output_value)
        
        t5=Timer(3, final_output)
        t5.start

        def icon_appear():


            if str(rand_choice)=='Paper':
                
                bard5=Image.open('/Users/thispc/Documents/College core work/projects /Imagesnvideo/Paper_450x450.jpg')
                bard5=bard5.resize((180,250), Image.ANTIALIAS)
                bardejov5 = ImageTk.PhotoImage(bard5)
                label_block_paper = Label(Rock_Paper_scissors, image=bardejov5)
                label_block_paper.image = bardejov5
                label_block_paper.place(x=400, y=250)
                

            elif str(rand_choice)=='Rock':
                
                bard5=Image.open('/Users/thispc/Documents/College core work/projects /Imagesnvideo/Rock.jpg')
                bard5=bard5.resize((180,250), Image.ANTIALIAS)
                bardejov5 = ImageTk.PhotoImage(bard5)
                label_block_rock = Label(Rock_Paper_scissors, image=bardejov5)
                label_block_rock.image = bardejov5
                label_block_rock.place(x=400, y=250)
                
            elif str(rand_choice)=='Scissors':
                
                bard5=Image.open('/Users/thispc/Documents/College core work/projects /Imagesnvideo/fabric-cutting-scissor-500x500.jpg')   
                bard5=bard5.resize((180,250), Image.ANTIALIAS)
                bardejov5 = ImageTk.PhotoImage(bard5)
                label_block_scissors = Label(Rock_Paper_scissors, image=bardejov5)
                label_block_scissors.image = bardejov5
                label_block_scissors.place(x=400, y=250)
        
            
        t3=Timer(4, icon_appear)
        t3.start()         
            
        t2=Timer(4,video_block)
        t2.start()    

       # t5=Timer(7,final_output)
        #t5.start        
     
      
       

    else:

        messagebox.showerror("Wrong error", "Please choose again", icon="warning")    

    

Rock_Paper_scissors.geometry('686x700')

fontsize=tkfont.Font(family="Garamond", size=18)

Title= Label(Rock_Paper_scissors, text='Rock Paper Scissors Game', bg='light green', font=fontsize)
Title.grid(padx=250, pady=20)


fontsize2=tkfont.Font(family="Georgia", size=16)
Choose=Label(Rock_Paper_scissors, text='choose either of the following', bg='light blue', font=fontsize2)
Choose.place(x=100, y=100)

bard=Image.open('/Users/thispc/Documents/College core work/projects /Imagesnvideo/Rock.jpg')
bard=bard.resize((150, 120), Image.ANTIALIAS)
bardejov = ImageTk.PhotoImage(bard)
label_rock = Label(Rock_Paper_scissors, image=bardejov)
label_rock.image = bardejov


label_rock.place(x=120, y=150)

fontsize3=tkfont.Font(family='Herculanum',size='16')
Button_rock=Button(Rock_Paper_scissors, text='Rock', font=fontsize3, bg='green', command=lambda:user_choice(mytext))
mytext= Button_rock.cget('text')
Button_rock.place(x=170, y=270)


bard2=bard=Image.open('/Users/thispc/Documents/College core work/projects /Imagesnvideo/Paper_450x450.jpg')
bard2=bard2.resize((150, 120), Image.ANTIALIAS)
bardejov2=ImageTk.PhotoImage(bard2)
label_paper = Label(Rock_Paper_scissors, image=bardejov2)
label_paper.image = bardejov2
label_paper.place(x=130, y=310)

fontsize3=tkfont.Font(family='Athelas',size='16')
Button_paper=Button(Rock_Paper_scissors, text='Paper', font=fontsize3, command=lambda:user_choice(mytext2))
mytext2=Button_paper.cget('text')
Button_paper.place(x=170, y=450)

bard3=Image.open('/Users/thispc/Documents/College core work/projects /Imagesnvideo/fabric-cutting-scissor-500x500.jpg')
bard3=bard3.resize((150, 120), Image.ANTIALIAS)
bardejov3=ImageTk.PhotoImage(bard3)
label_paper = Label(Rock_Paper_scissors, image=bardejov3)
label_paper.image = bardejov3
label_paper.place(x=130, y=500)

fontsize4=tkfont.Font(family='Calibri',size='16')
Button_scissors=Button(Rock_Paper_scissors, text='Scissors', font=fontsize4, command=lambda:user_choice(mytext3))
mytext3=Button_scissors.cget('text')
Button_scissors.place(x=170, y=650)

Rock_Paper_scissors.mainloop()
