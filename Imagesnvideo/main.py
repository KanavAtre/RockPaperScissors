from tkinter import *
import tkinter.messagebox
import tkinter.font as tkfont
from PIL import Image, ImageTk
from tkinter import messagebox
import imageio
import tkinter as threading
import tkvideo
import random
import time

Rock_Paper_scissors = Tk()

list_of_optn=['Rock', 'Paper', 'Scissors']


def user_choice(option):
    choice=''
    choice=choice+str(option)
    result=messagebox.askquestion("Alert","You have chosen "+choice+", Confirm? ")
    return result

if user_choice == "yes":
    label_video =Label(Rock_Paper_scissors)
    label_video.place(x=400, y=250)
    player = tkvideo.tkvideo("/Users/thispc/Desktop/Imagesnvideo/RPReplay_Final1621845129.mov", label_video, loop = 1, size = (180,250))
    player.play()
    alert_label= Label(Rock_Paper_scissors, text='The bot is choosing...', fg='grey')
    alert_label.place(x=400, y=550)
    time.sleep(4)
    alert_label.place(x=5000, y=89329)
    bot_choice=random.choice(list_of_optn)
    #choice_label=Label(Rock_Paper_scissors, text='The bot choose'+ bot_choice)
    choice_label=Label(Rock_Paper_scissors, text='The bot choose'+ bot_choice)
    choice_label.after(2000)
    choice_label.place(x=400, y=580)
    #choice_label.configure(text='The bot chose...'+ bot_choice)
    
else:

    messagebox.showerror("Wrong error", "Please choose again", icon="warning")    

Rock_Paper_scissors.geometry('686x700')

fontsize=tkfont.Font(family="Garamond", size=18)

Title= Label(Rock_Paper_scissors, text='Rock Paper Scissors Game', bg='light green', font=fontsize)
Title.grid(padx=250, pady=20)

'''
#Rock= Button(Rock_Paper_scissors, text="Rock", bg='brown')

#Rock.grid(row=2, column=1) 
'''
fontsize2=tkfont.Font(family="Georgia", size=16)
Choose=Label(Rock_Paper_scissors, text='choose either of the following', bg='light blue', font=fontsize2)
Choose.place(x=100, y=100)

bard=Image.open('/Users/thispc/Desktop/Imagesnvideo/Rock.jpg')
bard=bard.resize((150, 120), Image.ANTIALIAS)
bardejov = ImageTk.PhotoImage(bard)
label_rock = Label(Rock_Paper_scissors, image=bardejov)
label_rock.image = bardejov

'''
#image = image.resize
'''
label_rock.place(x=120, y=150)

fontsize3=tkfont.Font(family='Herculanum',size='16')
Button_rock=Button(Rock_Paper_scissors, text='Rock', font=fontsize3, bg='green', command=lambda:user_choice(mytext))
mytext= Button_rock.cget('text')
#Button_rock.bind("<Button-1>", rock)
Button_rock.place(x=170, y=270)


bard2=bard=Image.open('/Users/thispc/Desktop/Imagesnvideo/Paper_450x450.jpg')
bard2=bard2.resize((150, 120), Image.ANTIALIAS)
bardejov2=ImageTk.PhotoImage(bard2)
label_paper = Label(Rock_Paper_scissors, image=bardejov2)
label_paper.image = bardejov2
label_paper.place(x=130, y=310)

fontsize3=tkfont.Font(family='Athelas',size='16')
Button_paper=Button(Rock_Paper_scissors, text='Paper', font=fontsize3, command=lambda:user_choice(mytext2))
mytext2=Button_paper.cget('text')
#Button_paper.bind("<Button-2>", rock)
Button_paper.place(x=170, y=450)

bard3=Image.open('/Users/thispc/Desktop/Imagesnvideo/fabric-cutting-scissor-500x500.jpg')
bard3=bard3.resize((150, 120), Image.ANTIALIAS)
bardejov3=ImageTk.PhotoImage(bard3)
label_paper = Label(Rock_Paper_scissors, image=bardejov3)
label_paper.image = bardejov3
label_paper.place(x=130, y=500)

fontsize4=tkfont.Font(family='Calibri',size='16')
Button_scissors=Button(Rock_Paper_scissors, text='Scissors', font=fontsize4, command=lambda:user_choice(mytext3))
mytext3=Button_scissors.cget('text')
Button_scissors.place(x=170, y=650)

video_name = "/Users/thispc/Desktop/Imagesnvideo/RPReplay_Final1621845129.mov" #This is your video file path
video = imageio.get_reader(video_name)

'''

#def stream(label):

 #   for image in video.iter_data():
  #      frame_image = ImageTk.PhotoImage(Image.fromarray(image))
   #     label.config(image=frame_image)
    #    label.image = frame_image

#if __name__ == "__main__":

 #   my_label = Label(Rock_Paper_scissors)
  #  my_label.place(x=330, y=300)
   # thread = threading.Thread(target=stream, args=(my_label,))
    #thread.daemon = 1
    #thread.start()  

'''
Rock_Paper_scissors.mainloop()
