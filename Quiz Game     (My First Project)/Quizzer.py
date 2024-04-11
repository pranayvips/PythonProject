from tkinter import *
import tkinter.messagebox
from pygame import mixer
import time

mixer.init()
mixer.music.load('open.mp3')
mixer.music.play(1)
score=['0','10','20','30','40','50','60','70','80','90','100']
of=['1 of 10','2 of 10','3 of 10','4 of 10','5 of 10','6 of 10','7 of 10','8 of 10','9 of 10','10 of 10','']
questions = ['How many volts are there in 12 volt battery ?','If 55 is (fifty five) and 49 is (forty nine) then 11 is ?','If life is unfair to everyone does that make it fair ?','How to store milk safely and for long lasting freshness ?','When was the war of 1812 ?','What is the colour of Red','Where did Neil Armstrong went on the moon.','What is the thing that is always coming but never comes.','Which of the following is not an browser.','Who died in squid game.','THANK YOU FOR PLAYING THIS GAME']

first_option = ['0 volts'         ,'onety one'             ,'elon musk' ,'drink it all '            ,'Akbar-Hitler War of 2022'  ,'green'      ,'Sulabh Shauchalaya'     ,'tommorow'                 ,'instagram'         ,'HoYeon Jung'      ,'']
second_option = ['12 volts'       ,'eleven'                ,'nonsense'  ,'put cow in fridge'        ,'stone age'                 ,"don't know" ,'never stepped on moon'  ,'when you become rich'     ,'opera'             ,'Lee jung-jae'     ,'']
third_option = ['infinite volts'  ,'eleventy one'          ,'rubbish'   ,'no scope'                 ,'2021'                      ,'light red'  ,'rajendra nagar-patna'   ,'your brain'               ,'internet explorer' ,'The Front Man'    ,'']
fourth_option = ['no scope'       ,'number does not exist' ,'True'      ,'make the cow drink that'  ,'1812'                      ,'bluish'     ,'no scope'               ,'non-sense'                ,'facebook'          ,'Hwang Jun-ho'     ,'']

correct_answers = ['12 volts'     ,'eleven'                ,'True'      ,'put cow in fridge'        ,'1812'                      ,'light red'  ,'no scope'               ,'tommorow'                 ,'opera'              ,'HoYeon Jung'     ,'']

def conti():
    root2.destroy()
root2 = Tk()
root2.geometry('571x280')
root2.resizable(0, 0)
root2.title("pranay's Quiz")
root2.config(bg='black')
asghImage=PhotoImage(file='wellc.png')
layoutlabel = Label(root2, image=asghImage, bd=0)
layoutlabel.place(x=0,y=0)
nButton = Button(root2, text='Continue-)', font=('arial', 19, 'bold'), bg='purple', fg='yellow',bd=0,activebackground='black', cursor='hand2', activeforeground='white',command=conti)
nButton.place(x=410,y=220)
root2.mainloop()

def con():
    root3.destroy()
def exet():
    exit()
mixer.music.load('hera.mp3')
mixer.music.play(1)
root3 = Tk()
root3.geometry('840x664')
root3.resizable(0, 0)
root3.title("pranay's Quiz")
root3.config(bg='black')
asghImage=PhotoImage(file='eula.png')
asghImage1=PhotoImage(file='agreewala.png')
asghImage2=PhotoImage(file='disagreewala.png')
layoutlabel = Label(root3, image=asghImage, bd=0)
layoutlabel.place(x=0,y=0)
nButton = Button(root3, image=asghImage1, font=('arial', 12, 'bold'), bg='white', fg='black',bd=0,command=con)
nButton.place(x=441,y=525)
nButton = Button(root3, image=asghImage2, font=('arial', 12, 'bold'), bg='white', fg='black',bd=0,command=exet)
nButton.place(x=333,y=525)

root3.mainloop()

def asd():
    root4.destroy()
root4 = Tk()
root4.geometry('600x661')
root4.resizable(0, 0)
root4.title("pranay's Quiz")
root4.config(bg='black')
as_dfgImage=PhotoImage(file='disclamer.png')
as_dgImage=PhotoImage(file='Accept.png')
layoutlabel = Label(root4, image=as_dfgImage, bd=0)
layoutlabel.place(x=0,y=0)
nButton = Button(root4, image=as_dgImage,  bg='white', bd=0,command=asd)
nButton.place(x=250,y=455)

root4.mainloop()



def select(event):
    #mixer.music.set_volume(1)
    b = event.widget
    value = b['text']
    for i in range(10):
        if value == correct_answers[i]:
            mixer.music.load('adbhut.mp3')
            mixer.music.play(1)
            optionButton1.config(text=first_option[i + 1])
            optionButton2.config(text=second_option[i + 1])
            optionButton3.config(text=third_option[i + 1])
            optionButton4.config(text=fourth_option[i + 1])
            optionButton5.config(text=questions[i + 1])
            optionButton6.config(text=of[i + 1])
            optionButton7.config(text='Your Score is = '+score[i + 1])
            
        
        if value not in correct_answers:
            def tryagain():
                mixer.music.load('toba.mp3')
                mixer.music.play(-1)
                
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                optionButton5.config(text=questions[0])
                optionButton6.config(text=of[0])
                optionButton7.config(text='your score is '+score[0])
                
                root1.destroy()
                
            def on_closing():
                root1.destroy()
                root.destroy()
            mixer.music.stop()
            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.grab_set()
            root1.config(bg='black')
            root1.geometry('1100x770')
            root1.title('You Lose')
            img = PhotoImage(file='inco.png')
            imgLabel = Label(root1, image=img, bd=0)
            imgLabel.pack(pady=30)
            tryagainButton = Button(root1, text='Try Again', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                    , activebackground='black', cursor='hand2', activeforeground='white',
                                    command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                 , activebackground='black', cursor='hand2', activeforeground='white',
                                 command=on_closing)
            closeButton.pack()

            root1.protocol('WM_DELETE_WINDOW', on_closing)

            root1.mainloop()
            break
            
root = Tk()
root.geometry('1107x624')
root.resizable(0, 0)
root.title('1Q==0')
root.config(bg='black')

leftFrame = Frame(root, bg='black', padx=90)
leftFrame.grid(row=0, column=0)

rightFrame = Frame(root, bg='black', padx=50, pady=25)
rightFrame.grid(row=0, column=1)

topFrame = Frame(leftFrame, bg='black', pady=15)
topFrame.grid(row=0, column=0)

middleFrame = Frame(leftFrame, bg='black', pady=15)
middleFrame.grid(row=1, column=0)

bottomFrame = Frame(leftFrame, bg='black')
bottomFrame.grid(row=2, column=0)

imcgImage=PhotoImage(file='1.png')
layoutlabel = Label(root, image=imcgImage, bd=0)
layoutlabel.grid(row=0, column=0)

optionButton1 = Button(root,text=first_option[0], font=('arial', 18, 'bold'), bg='red', fg='white',cursor='hand2',bd=0,activebackground='red',activeforeground='white')
optionButton1.place(x=170,y=425)

optionButton2 = Button(root, text=second_option[0], font=('arial', 18, 'bold'), bg='blue', fg='white', cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton2.place(x=740,y=420)

optionButton3 = Button(root, text=third_option[0], font=('arial', 18, 'bold'), bg='yellow', fg='red',cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton3.place(x=180,y=540)

optionButton4 = Button(root, text=fourth_option[0], font=('arial', 18, 'bold'), bg='green', fg='white',cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton4.place(x=710,y=546)

optionButton5 = Button(root, text=questions[0], font=('arial', 27, 'bold'), bg='white', fg='black',cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton5.place(x=80,y=295)

optionButton6 = Button(root, text=of[0], font=('arial', 31, 'bold'), bg='dark blue', fg='white',bd=0,activebackground='purple',activeforeground='black')
optionButton6.place(x=1,y=1)

optionButton7 = Button(root, text='Your Score is = '+score[0], font=('arial', 12, 'bold'), bg='dark blue', fg='white',bd=0,activebackground='purple',activeforeground='white')
optionButton7.place(x=950,y=250)

def setting():
    root987 = Toplevel()
    root987.geometry('650x468')
    root987.overrideredirect(True)
    root987.title('Quiz settings')
    root987.config(bg='black')
    dafghImage=PhotoImage(file='setting.png')
    ghayoutlabel = Label(root987, image=dafghImage, bd=0)
    ghayoutlabel.place(x=0,y=0)
    closeImage=PhotoImage(file='close.png')
    allsetImage=PhotoImage(file='allisset.png')
    audioImage=PhotoImage(file='audio.png')
    aboutusImage=PhotoImage(file='aboutus.png')
    
    def closebutt():
        root987.destroy()
    closeButton8 = Button(root987, image=closeImage,bd=0,bg='dark blue',activebackground='black',activeforeground='black',cursor='hand2',command=closebutt)
    closeButton8.place(x=21,y=414)
    
    allsetButton8 = Button(root987, image=allsetImage,bd=0,bg='dark blue',activebackground='black',activeforeground='black',cursor='hand2')
    allsetButton8.place(x=278,y=53)
    
    audioButton8 = Button(root987, image=audioImage,bd=0,bg='dark blue',activebackground='black',activeforeground='black',cursor='hand2',command=setting)
    audioButton8.place(x=33,y=106)
    
    def aboutus():
        root789=Tk()
        root789.geometry('634x570')
        root789.overrideredirect(True)
        root789.title('About us')
        root789.config(bg='black')
        
        f=open('review.txt','r')
        ff=f.read()
        ff=str(ff)
        outusButton8 = Button(root789, text=ff,bd=0,bg='white',font=('arial',18,'bold'),activebackground='black',activeforeground='black')
        outusButton8.place(x=364,y=101)

        ggmmImage=PhotoImage(file='reviews.png')
        cakeislabel =Button(root789, image=ggmmImage, bd=0)
        cakeislabel.place(x=0,y=0)
        root789.mainloop()

    aboutusButton8 = Button(root987, image=aboutusImage,bd=0,bg='dark blue',activebackground='black',activeforeground='black',cursor='hand2',command=aboutus)
    aboutusButton8.place(x=518,y=367)

    root987.mainloop()
setImage=PhotoImage(file='set.png')
optionButton8 = Button(root, image=setImage,bd=0,bg='dark blue',activebackground='purple',activeforeground='white',cursor='hand2',command=setting)
optionButton8.place(x=1050,y=1)



optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)
root.mainloop()



def onClick():
    tkinter.messagebox.showinfo('ABOUT HIM',text)
def closer():
    root1.destroy()
root1 = tkinter.Tk()
root1.title("Information")
root1.geometry("350x200")
root1.overrideredirect(True)
root1.config(bg='red')
atabutton = Button(root1, text='Made and developed by \nSir.Pranay Prasad ',bg='red', fg='white',bd=0,activebackground='red',activeforeground='blue',height=3,width=21,font=('arial',21,'bold'))
atabutton.place(x=0,y=0)
atabutton.pack()

text='Sir.Pranay Prasad is an entrepreneur and business magnate. He is the founder, CEO and Chief Engineer at Mars; early-stage investor, CEO and Product Architect of vimal-zuba kesari, Inc.; and co-founder of universe. With an estimated net worth of around US$2555 trillion as of December 2021,Prasad is one of the richest person in the Mars.More about him is not known as of now'
atabutton2 = Button(root1,text='Want to read more about Sir. Pranay Prasad      (CLICK HERE)',bd=0,bg='red',fg='blue', activebackground='red',activeforeground='black',font=('arial',9,'bold'),command=onClick)
atabutton2.place(x=15,y=16)
atabutton2.pack()

atabutton1 = Button(root1,text='OKAY',bg='red',fg='white', bd=0,activebackground='red',activeforeground='black',height=1,width=5,font=('arial',21,'bold'),command=closer)
atabutton1.place(x=15,y=16)
atabutton1.pack()


root1.mainloop()
'''
import time
from plyer import notification

if __name__ == "__main__" :
    notification.notify(
        title = "Hehehe",
        
        message = "ThankYou for wasting your time\ncredits goes to Sir.Pranay Prasad\nPlease give us a 5 star review.",
        app_icon = "abcl.ico",
        timeout=20
    )'''

def buttone():
    root7.destroy()
    root8 = Tk()
    root8.geometry('504x312')
    root8.resizable(0, 0)
    root8.title("Please review us")
    root8.config(bg='black')
    def search():
        frame = Tk()
        frame.title("G-SEARCH")
        frame.geometry('200x70')
        def printInput():
            root8.destroy()
            inp = inputtxt.get(1.0, "end-1c")
            a=inp
            a1=str(a)
            f=open('review.txt','w')
            f.write(a1)
            f.close()
            frame.destroy()
            root9 = Toplevel()
            root9.geometry('622x448')
            root9.resizable(0, 0)
            root9.title("Thank you")
            root9.config(bg='black')
            thankImage=PhotoImage(file='thank.png')
            layoutlabel = Label(root9, image=thankImage, bd=0)
            layoutlabel.place(x=0,y=0)
            def abcdefg():
                root9.destroy()
            thankButton = Button(root9, text='Welcome',  bg='light blue',cursor='hand2',fg='white',font=('arial',18,'bold') ,bd=0,command=abcdefg)
            thankButton.place(x=460,y=403)
            root9.mainloop()
        inputtxt = Text(frame,height = 2,width = 50)
        inputtxt.pack()
        a=printInput
        a1=str(a)
        f=open('review.txt','w')
        f.write(a1)
        f.close()
        searchButton = Button(frame, text = "send=)",cursor='hand2', command = printInput)
        searchButton.pack()
    asmhImage=PhotoImage(file='review1star.png')
    writeImage=PhotoImage(file='writereview.png')
    layoutlabel = Label(root8, image=asmhImage, bd=0)
    layoutlabel.place(x=0,y=0)
    oeneButton = Button(root8, image=writeImage,  bg='white',cursor='hand2', bd=0,command=search)
    oeneButton.place(x=20,y=225)
    root8.mainloop()

def butttwo():
    root7.destroy()
    root8 = Tk()
    root8.geometry('504x312')
    root8.resizable(0, 0)
    root8.title("Please review us")
    root8.config(bg='black')
    def search():
        frame = Tk()
        frame.title("G-SEARCH")
        frame.geometry('200x70')
        def printInput():
            root8.destroy()
            inp = inputtxt.get(1.0, "end-1c")
            a=inp
            a1=str(a)
            f=open('review.txt','w')
            f.write(a1)
            f.close()
            frame.destroy()
            root9 = Tk()
            root9.geometry('622x448')
            root9.resizable(0, 0)
            root9.title("Thank you")
            root9.config(bg='black')
            thankImage=PhotoImage(file='thank.png')
            layoutlabel = Label(root9, image=thankImage, bd=0)
            layoutlabel.place(x=0,y=0)
            def abcdefg():
                root9.destroy()
            thankButton = Button(root9, text='Welcome',  bg='light blue',cursor='hand2',fg='white',font=('arial',18,'bold') ,bd=0,command=abcdefg)
            thankButton.place(x=460,y=403)
            root9.mainloop()
        inputtxt = Text(frame,height = 2,width = 50)
        inputtxt.pack()
        a=printInput
        a1=str(a)
        f=open('review.txt','w')
        f.write(a1)
        f.close()
        searchButton = Button(frame, text = "send=)",cursor='hand2', command = printInput)
        searchButton.pack()
    asmhImage=PhotoImage(file='review2star.png')
    writeImage=PhotoImage(file='writereview.png')
    layoutlabel = Label(root8, image=asmhImage, bd=0)
    layoutlabel.place(x=0,y=0)
    oeneButton = Button(root8, image=writeImage,  bg='white',cursor='hand2', bd=0,command=search)
    oeneButton.place(x=20,y=225)
    root8.mainloop()
def buttthree():
    root7.destroy()
    root8 = Tk()
    root8.geometry('504x312')
    root8.resizable(0, 0)
    root8.title("Please review us")
    root8.config(bg='black')
    def search():
        frame = Tk()
        frame.title("G-SEARCH")
        frame.geometry('200x70')
        def printInput():
            root8.destroy()
            inp = inputtxt.get(1.0, "end-1c")
            a=inp
            a1=str(a)
            f=open('review.txt','w')
            f.write(a1)
            f.close()
            frame.destroy()
            root9 = Tk()
            root9.geometry('622x448')
            root9.resizable(0, 0)
            root9.title("Thank you")
            root9.config(bg='black')
            thankImage=PhotoImage(file='thank.png')
            layoutlabel = Label(root9, image=thankImage, bd=0)
            layoutlabel.place(x=0,y=0)
            def abcdefg():
                root9.destroy()
            thankButton = Button(root9, text='Welcome',  bg='light blue',cursor='hand2',fg='white',font=('arial',18,'bold') ,bd=0,command=abcdefg)
            thankButton.place(x=460,y=403)
            root9.mainloop()
        inputtxt = Text(frame,height = 2,width = 50)
        inputtxt.pack()
        a=printInput
        a1=str(a)
        f=open('review.txt','w')
        f.write(a1)
        f.close()
        searchButton = Button(frame, text = "send=)",cursor='hand2', command = printInput)
        searchButton.pack()
    asmhImage=PhotoImage(file='review3star.png')
    writeImage=PhotoImage(file='writereview.png')
    layoutlabel = Label(root8, image=asmhImage, bd=0)
    layoutlabel.place(x=0,y=0)
    oeneButton = Button(root8, image=writeImage,  bg='white',cursor='hand2', bd=0,command=search)
    oeneButton.place(x=20,y=225)
    root8.mainloop()
def buttfour():
    root7.destroy()
    root8 = Tk()
    root8.geometry('504x312')
    root8.resizable(0, 0)
    root8.title("Please review us")
    root8.config(bg='black')
    def search():
        frame = Tk()
        frame.title("G-SEARCH")
        frame.geometry('200x70')
        def printInput():
            root8.destroy()
            inp = inputtxt.get(1.0, "end-1c")
            a=inp
            a1=str(a)
            f=open('review.txt','w')
            f.write(a1)
            f.close()
            frame.destroy()
            root9 = Tk()
            root9.geometry('622x448')
            root9.resizable(0, 0)
            root9.title("Thank you")
            root9.config(bg='black')
            thankImage=PhotoImage(file='thank.png')
            layoutlabel = Label(root9, image=thankImage, bd=0)
            layoutlabel.place(x=0,y=0)
            def abcdefg():
                root9.destroy()
            thankButton = Button(root9, text='Welcome',  bg='light blue',cursor='hand2',fg='white',font=('arial',18,'bold') ,bd=0,command=abcdefg)
            thankButton.place(x=460,y=403)
            root9.mainloop()
        inputtxt = Text(frame,height = 2,width = 50)
        inputtxt.pack()
        a=printInput
        a1=str(a)
        f=open('review.txt','w')
        f.write(a1)
        f.close()
        searchButton = Button(frame, text = "send=)",cursor='hand2', command = printInput)
        searchButton.pack()
    asmhImage=PhotoImage(file='review4star.png')
    writeImage=PhotoImage(file='writereview.png')
    layoutlabel = Label(root8, image=asmhImage, bd=0)
    layoutlabel.place(x=0,y=0)
    oeneButton = Button(root8, image=writeImage,  bg='white',cursor='hand2', bd=0,command=search)
    oeneButton.place(x=20,y=225)
    root8.mainloop()
def buttfive():
    root7.destroy()
    root8 = Tk()
    root8.geometry('504x312')
    root8.resizable(0, 0)
    root8.title("Please review us")
    root8.config(bg='black')
    def search():
        frame = Tk()
        frame.title("G-SEARCH")
        frame.geometry('200x70')
        def printInput():
            root8.destroy()
            inp = inputtxt.get(1.0, "end-1c")
            a=inp
            a1=str(a)
            f=open('review.txt','w')
            f.write(a1)
            f.close()
            frame.destroy()
            root9 = Tk()
            root9.geometry('622x448')
            root9.resizable(0, 0)
            root9.title("Thank you")
            root9.config(bg='black')
            thankImage=PhotoImage(file='thank.png')
            layoutlabel = Label(root9, image=thankImage, bd=0)
            layoutlabel.place(x=0,y=0)
            def abcdefg():
                root9.destroy()
            thankButton = Button(root9, text='Welcome',  bg='light blue',cursor='hand2',fg='white',font=('arial',18,'bold') ,bd=0,command=abcdefg)
            thankButton.place(x=460,y=403)
            root9.mainloop()
        inputtxt = Text(frame,height = 2,width = 50)
        inputtxt.pack()
        a=printInput
        a1=str(a)
        f=open('review.txt','w')
        f.write(a1)
        f.close()
        searchButton = Button(frame, text = "send=)",cursor='hand2', command = printInput)
        searchButton.pack()
    asmhImage=PhotoImage(file='review5star.png')
    writeImage=PhotoImage(file='writereview.png')
    layoutlabel = Label(root8, image=asmhImage, bd=0)
    layoutlabel.place(x=0,y=0)
    oeneButton = Button(root8, image=writeImage,  bg='white',cursor='hand2', bd=0,command=search)
    oeneButton.place(x=20,y=225)
    root8.mainloop()
root7 = Tk()
root7.geometry('504x312')
root7.resizable(0, 0)
root7.title("Please review-Your feedback")
root7.config(bg='black')
as_dmhgImage=PhotoImage(file='review.png')
layoutlabel = Label(root7, image=as_dmhgImage, bd=0)
layoutlabel.place(x=0,y=0)

star1Image=PhotoImage(file='1star.png')
star2Image=PhotoImage(file='2star.png')
star3Image=PhotoImage(file='3star.png')
star4Image=PhotoImage(file='4star.png')
star5Image=PhotoImage(file='5star.png')

oneButton = Button(root7, image=star1Image,cursor='hand2',  bg='white', bd=0,command=buttone)
oneButton.place(x=2,y=175)


twoButton = Button(root7, image=star2Image, cursor='hand2', bg='white', bd=0,command=butttwo)
twoButton.place(x=93,y=175)


threeButton = Button(root7, image=star3Image,cursor='hand2',  bg='white', bd=0,command=buttthree)
threeButton.place(x=189,y=175)


fourButton = Button(root7, image=star4Image,cursor='hand2',  bg='white', bd=0,command=buttfour)
fourButton.place(x=288,y=170)


fiveButton = Button(root7, image=star5Image,cursor='hand2',  bg='white', bd=0,command=buttfive)
fiveButton.place(x=390,y=170)


root7.mainloop()

exit()
         