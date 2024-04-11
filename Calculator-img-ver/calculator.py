import pygame 
from math import sqrt
import ctypes
from ctypes import wintypes 
import webbrowser
import requests
from tkinter import *
import sys



pygame.init()
screen=pygame.display.set_mode((320,505))
pygame.display.set_caption('Calculator')
clock=pygame.time.Clock()

pygame_icon = pygame.image.load('images.ico')
pygame_icon1 = pygame.image.load('fee.ico')
pygame.display.set_icon(pygame_icon)
game_active=True

def get_feature():
    root=Tk()
    root.config(bg='white')
    root.title('Request To Add A Feature')
    root.geometry('700x500')
    root.resizable(0,0)

    Label(root,text='|ADD A FEATURE|',fg='black',bg='white',font=('georgia',20,'bold')).place(x=220,y=0)
    Label(root,text='*Name For Your Feature :',fg='dark blue',bg='white',font=('georgia',20,'bold')).place(x=0,y=100)
    Label(root,text='You can tell about your feature in brief (optional) :',fg='dark blue',bg='white',font=('georgia',19,'bold')).place(x=0,y=200)
    textbox1=Text(root,fg='orange',font=('arial',15),height=1,width=30,bd=10)
    textbox1.place(x=350,y=104)
    textbox2=Text(root,fg='green',font=('arial',15),height=8,width=50,bd=5)
    textbox2.place(x=50,y=240)
    def submit():
        abmd=textbox1.get(1.0, "end-1c")
        if len(abmd)>3:
            abmd1=textbox2.get(1.0, "end-1c")
            f=open('report','a')
            f.write('  '+abmd+':'+abmd1)
            f.close()
            root.destroy()
        else:
            Label(root,text='!!!!YOU HAVE GOT AN ERROR!!!!\nPlease write more than 5 words',fg='red',bg='white',font=('georgia',15,'bold')).place(x=40,y=145)
    lob=Button(root,text='Submit',fg='black',bg='white',bd=0,font=('georgia',20,'bold'),cursor='hand2',command=submit)
    lob.place(x=270,y=450)
    root.mainloop()


def writs():
    root=Tk()
    root.title('Write Your Review')
    root.geometry('470x350')
    root.config(bg='black')

    ab=Text(root,fg='black',width=30,height=7,bd=10,font=('arial',20,'bold'))
    ab.place(x=0,y=0)
    def getall():
        abp=ab.get(1.0, "end-1c")
        root.destroy()

    cd=Button(root,text='SUBMIT',bg='green',fg='blue',font=('arial',20,'bold'),command=getall)
    cd.place(x=180,y=270)

    root.mainloop()

def pin_to_top():
    hwnd = pygame.display.get_wm_info()['window']
    user32 = ctypes.WinDLL("user32")
    user32.SetWindowPos.restype = wintypes.HWND
    user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.UINT]
    user32.SetWindowPos(hwnd, -1, 1100, 50, 0, 0, 0x0001)
def searching_online(term):
    url = "https://www.google.com.tr/search?q={}".format(term)
    webbrowser.open_new_tab(url)

def clear_all():
    f=open(r'standard/cal','w')
    f.write('0')
    f.close()
    f=open(r'standard/cal_above','w')
    f.write('')
    f.close()
    f=open(r'standard/main','w')
    f.write('')
    f.close()
clear_all()

bg_surface=pygame.image.load('cc.png')



#REVIEW SCREEN
review_main_photo=pygame.image.load(r'rate\rate.png')
review_1_photo=pygame.image.load(r'rate\1.png')
review_2_photo=pygame.image.load(r'rate\2.png')
review_3_photo=pygame.image.load(r'rate\3.png')
review_4_photo=pygame.image.load(r'rate\4.png')
review_5_photo=pygame.image.load(r'rate\5.png')

review_welcome_photo=pygame.image.load(r'welcome.png')

back_button_photo=pygame.image.load(r'back.png')
back_button_rect=back_button_photo.get_rect(bottomright=(73,50))

review_write_photo=pygame.image.load(r'rate\write.png')
photo_thanks=pygame.image.load(r'thank.png')

review_1_rect=review_1_photo.get_rect(bottomright=(175,286))
review_2_rect=review_2_photo.get_rect(bottomright=(287,289))
review_3_rect=review_3_photo.get_rect(bottomright=(401,287))
review_4_rect=review_4_photo.get_rect(bottomright=(513,286))
review_5_rect=review_5_photo.get_rect(bottomright=(626,286))

review_welcome_rect=review_welcome_photo.get_rect(bottomright=(416,336))

review_write_rect=review_write_photo.get_rect(bottomright=(600,336))


#REVIEW SCREEN



#STANDARD SCREEN
standard_screen=True
standard_screen_typing=True
start=0
plus_active=False
cut_equal_state=False

#other image
abo=pygame.image.load(r'standard\developer.png') 
fohts=pygame.image.load(r'standard\fohts.png')
fohts_rect=fohts.get_rect(bottomright=(400,450))
#other image


Button_0_photo=pygame.image.load(r'standard\0.png')
Button_1_photo=pygame.image.load(r'standard\1.png')
Button_2_photo=pygame.image.load(r'standard\2.png')
Button_3_photo=pygame.image.load(r'standard\3.png')
Button_4_photo=pygame.image.load(r'standard\4.png')
Button_5_photo=pygame.image.load(r'standard\5.png')
Button_6_photo=pygame.image.load(r'standard\6.png')
Button_7_photo=pygame.image.load(r'standard\7.png')
Button_8_photo=pygame.image.load(r'standard\8.png')
Button_9_photo=pygame.image.load(r'standard\9.png')
Button_plus_minus_photo=pygame.image.load(r'standard\+-.png')
Button_dot_photo=pygame.image.load(r'standard\d.png')
Button_equal_photo=pygame.image.load(r'standard\=.png')
Button_plus_photo=pygame.image.load(r'standard\+.png')
Button_minus_photo=pygame.image.load(r'standard\-.png')
Button_multi_photo=pygame.image.load(r'standard\x.png')
Button_divide_photo=pygame.image.load(r'standard\di.png')
Button_C_photo=pygame.image.load(r'standard\c.png')
Button_ce_photo=pygame.image.load(r'standard\ce.png')
Button_per_photo=pygame.image.load(r'standard\per.png')
Button_cut_photo=pygame.image.load(r'standard\cut.png')
Button_sq_photo=pygame.image.load(r'standard\sq.png')
Button_ro_photo=pygame.image.load(r'standard\ro.png')
Button_upon_photo=pygame.image.load(r'standard\upon.png')
Button_no_int_photo=pygame.image.load(r'standard\no_int.png')
Button_no_int_photo1=pygame.image.load(r'standard\no_int1.png')
Button_options_photo=pygame.image.load(r'standard\options.png')
Button_report_photo=pygame.image.load(r'standard\report.png')
Button_enlarge_photo=pygame.image.load(r'standard\enlarge.png')
Button_menu_butt_photo=pygame.image.load(r'standard\menu_butt.png')

Button_report_rect=Button_report_photo.get_rect(bottomright=(200,35))
Button_enlarge_rect=Button_enlarge_photo.get_rect(bottomright=(153,33))
Button_menu_butt_rect=Button_menu_butt_photo.get_rect(bottomright=(33,37))

#options
Button_request_photo=pygame.image.load(r'standard\request.png')
Button_request_rect=Button_request_photo.get_rect(bottomright=(210,110))
Button_aboutus_photo=pygame.image.load(r'standard\aboutus.png')
Button_aboutus_rect=Button_aboutus_photo.get_rect(bottomright=(210,180))#2nd for (130)
option_rating_photo=pygame.image.load(r'standard\ratesss.png')
option_rating_rect=option_rating_photo.get_rect(bottomright=(210,240))
#options

Button_7_rect=Button_7_photo.get_rect(bottomright=(80,337))
Button_8_rect=Button_8_photo.get_rect(bottomright=(159,337))
Button_9_rect=Button_9_photo.get_rect(bottomright=(237,337))
Button_multi_rect=Button_multi_photo.get_rect(bottomright=(316,337))

Button_4_rect=Button_4_photo.get_rect(bottomright=(80,391))
Button_5_rect=Button_5_photo.get_rect(bottomright=(159,391))
Button_6_rect=Button_6_photo.get_rect(bottomright=(237,391))
Button_minus_rect=Button_minus_photo.get_rect(bottomright=(316,391))

Button_1_rect=Button_1_photo.get_rect(bottomright=(80,445))
Button_2_rect=Button_2_photo.get_rect(bottomright=(159,445))
Button_3_rect=Button_3_photo.get_rect(bottomright=(237,445))
Button_plus_rect=Button_plus_photo.get_rect(bottomright=(316,445))

Button_0_rect=Button_0_photo.get_rect(bottomright=(159,500))
Button_plus_minus_rect=Button_plus_minus_photo.get_rect(bottomright=(80,500))
Button_dot_rect=Button_dot_photo.get_rect(bottomright=(237,500))
Button_equal_rect=Button_equal_photo.get_rect(bottomright=(316,500))


Button_divide_rect=Button_divide_photo.get_rect(bottomright=(316,282))
Button_sq_rect=Button_sq_photo.get_rect(bottomright=(237,282))
Button_ro_rect=Button_ro_photo.get_rect(bottomright=(159,282))
Button_upon_rect=Button_upon_photo.get_rect(bottomright=(80,282))


Button_C_rect=Button_C_photo.get_rect(bottomright=(240,229))
Button_ce_rect=Button_ce_photo.get_rect(bottomright=(162,229))
Button_per_rect=Button_per_photo.get_rect(bottomright=(80,229))
Button_cut_rect=Button_cut_photo.get_rect(bottomright=(316,229))




#bull_rect=bull_surface.get_rect(bottomright=(1600,505))
report_failed_of_internet=False
report_failed_of_internet_count=0
report_failed_of_internet_status=0
option_screen=False
about_dev=False
option_screen_count_clicks=0

review_screen=False
review_screen_1=False
review_screen_2=False
review_screen_3=False
report_failed_of_calculation=False

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if game_active:
            if event.type==pygame.MOUSEBUTTONDOWN:
                
                if standard_screen_typing:
                    pygame.display.set_mode((320,505))
                    pygame.display.set_caption('Calculator')
                    pygame.display.set_icon(pygame_icon)
                    if start==0:
                        f=open(r'standard/cal','w')
                        f.write('')
                        f.close()
                        start=1


                    if Button_0_rect.collidepoint(event.pos):

                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('0')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('0')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('0')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False
                        else:
                            f=open(r'standard/cal','a')
                            f.write('0')
                            f.close()

                        f=open(r'standard/main','a')
                        f.write('0')
                        f.close()
                    elif Button_1_rect.collidepoint(event.pos):

                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('1')
                            f.close()
                            plus_active=False

                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('1')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('1')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('1')
                            f.close()

                        f=open(r'standard/main','a')
                        f.write('1')
                        f.close()
                    elif Button_2_rect.collidepoint(event.pos):

                        f=open(r'standard/main','a')
                        f.write('2')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('2')
                            f.close()
                            plus_active=False

                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('2')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('2')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('2')
                            f.close()
                    elif Button_3_rect.collidepoint(event.pos):

                        f=open(r'standard/main','a')
                        f.write('3')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('3')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('3')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('3')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('3')
                            f.close()
                    elif Button_4_rect.collidepoint(event.pos):

                        f=open(r'standard/main','a')
                        f.write('4')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('4')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('4')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('4')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('4')
                            f.close()
                    elif Button_5_rect.collidepoint(event.pos):

                        f=open(r'standard/main','a')
                        f.write('5')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('5')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('5')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('5')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('5')
                            f.close()
                    elif Button_6_rect.collidepoint(event.pos):

                        f=open(r'standard/main','a')
                        f.write('6')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('6')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('6')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('6')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('6')
                            f.close()
                    elif Button_7_rect.collidepoint(event.pos):

                        f=open(r'standard/main','a')
                        f.write('7')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('7')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('7')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('7')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('7')
                            f.close()
                    elif Button_8_rect.collidepoint(event.pos):

                        f=open(r'standard/main','a')
                        f.write('8')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('8')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('8')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('8')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('8')
                            f.close()
                    elif Button_9_rect.collidepoint(event.pos):

                        f=open(r'standard/main','a')
                        f.write('9')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('9')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('9')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('9')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('9')
                            f.close()

                    elif Button_C_rect.collidepoint(event.pos):
                        clear_all()
                        start=0
                        cut_equal_state=False



                    elif Button_plus_rect.collidepoint(event.pos):
                        try:
                            f=open(r'standard/cal_above','r')
                            abcd=f.read()
                            f.close()

                            

                            if cut_equal_state:
                                f=open(r'standard/main','w')
                                f.write('+')
                                f.close()
                                f=open(r'standard/cal','w')
                                abmd=f.write('')
                                f.close()
                                f=open(r'standard/cal_above','w')
                                f.write('+')
                                f.close()
                                plus_active=True
                                cut_equal_state=False
                            elif '-' in abcd or '+' in abcd or '/ ' in abcd or '*' in abcd:
                                f=open(r'standard/cal','r')
                                abmd=f.read()
                                f.close()

                                f=open(r'standard/cal_above','a')
                                f.write(str(abmd+'+'))
                                f.close()

                                f=open(r'standard/main','r')
                                mob=f.read()
                                f.close()

                                mob=eval(mob)
                                mob=str(mob)

                                f=open(r'standard/main','a')
                                f.write('+')
                                f.close()

                                f=open(r'standard/cal','w')
                                f.write(mob)
                                f.close()

                                plus_active=True
                            else:
                                f=open(r'standard/main','a')
                                f.write('+')
                                f.close()

                                f=open(r'standard/main','r')
                                hhh=f.read()
                                f.close()

                                f=open(r'standard/cal','r')
                                abmd=f.read()
                                f.close()

                                f=open(r'standard/cal_above','a')
                                f.write(str(abmd+'+'))
                                f.close()

                                plus_active=True

                        except:
                            f=open(r'standard/cal_above','a')
                            f.write(str(''))
                            f.close()

                            f=open(r'standard/main','w')
                            f.write('')
                            f.close()

                            f=open(r'standard/cal','w')
                            f.write('INVALID SYNTAX')
                            f.close()
                    elif Button_minus_rect.collidepoint(event.pos):
                        try:
                            f=open(r'standard/cal_above','r')
                            abcd=f.read()
                            f.close()

                            

                            if cut_equal_state:
                                f=open(r'standard/main','w')
                                f.write('-')
                                f.close()
                                f=open(r'standard/cal','w')
                                abmd=f.write('')
                                f.close()
                                f=open(r'standard/cal_above','w')
                                f.write('-')
                                f.close()
                                plus_active=True
                                cut_equal_state=False
                            elif '-' in abcd or '+' in abcd or '/ ' in abcd or '*' in abcd:
                                f=open(r'standard/cal','r')
                                abmd=f.read()
                                f.close()

                                f=open(r'standard/cal_above','a')
                                f.write(str(abmd+'-'))
                                f.close()

                                f=open(r'standard/main','r')
                                mob=f.read()
                                f.close()

                                mob=eval(mob)
                                mob=str(mob)

                                f=open(r'standard/main','a')
                                f.write('-')
                                f.close()

                                f=open(r'standard/cal','w')
                                f.write(mob)
                                f.close()

                                plus_active=True
                            else:
                                f=open(r'standard/main','a')
                                f.write('-')
                                f.close()
                                f=open(r'standard/cal','r')
                                abmd=f.read()
                                f.close()
                                f=open(r'standard/cal_above','a')
                                f.write(str(abmd+'-'))
                                f.close()
                                plus_active=True

                        except:
                            f=open(r'standard/cal_above','a')
                            f.write(str(''))
                            f.close()

                            f=open(r'standard/main','w')
                            f.write('')
                            f.close()

                            f=open(r'standard/cal','w')
                            f.write('INVALID SYNTAX')
                            f.close()
                    elif Button_multi_rect.collidepoint(event.pos):
                        try:
                            f=open(r'standard/cal_above','r')
                            abcd=f.read()
                            f.close()

                            

                            if cut_equal_state:
                                f=open(r'standard/main','w')
                                f.write('*')
                                f.close()
                                f=open(r'standard/cal','w')
                                abmd=f.write('')
                                f.close()
                                f=open(r'standard/cal_above','w')
                                f.write('*')
                                f.close()
                                plus_active=True
                                cut_equal_state=False
                            elif '-' in abcd or '+' in abcd or '/ ' in abcd or '*' in abcd:
                                f=open(r'standard/cal','r')
                                abmd=f.read()
                                f.close()

                                f=open(r'standard/cal_above','a')
                                f.write(str(abmd+'*'))
                                f.close()

                                f=open(r'standard/main','r')
                                mob=f.read()
                                f.close()

                                mob=eval(mob)
                                mob=str(mob)

                                f=open(r'standard/main','a')
                                f.write('*')
                                f.close()

                                f=open(r'standard/cal','w')
                                f.write(mob)
                                f.close()

                                plus_active=True
                            else:

                                f=open(r'standard/main','a')
                                f.write('*')
                                f.close()

                                f=open(r'standard/cal','r')
                                abmd=f.read()
                                f.close()
                                f=open(r'standard/cal_above','a')
                                f.write(str(abmd+'*'))
                                f.close()
                                plus_active=True

                        except:
                            f=open(r'standard/cal_above','a')
                            f.write(str(''))
                            f.close()

                            f=open(r'standard/main','w')
                            f.write('')
                            f.close()

                            f=open(r'standard/cal','w')
                            f.write('INVALID SYNTAX')
                            f.close()
                    elif Button_divide_rect.collidepoint(event.pos):
                        try:
                            f=open(r'standard/cal_above','r')
                            abcd=f.read()
                            f.close()

                            

                            if cut_equal_state:
                                f=open(r'standard/main','w')
                                f.write('/')
                                f.close()
                                f=open(r'standard/cal','w')
                                abmd=f.write('')
                                f.close()
                                f=open(r'standard/cal_above','w')
                                f.write('/')
                                f.close()
                                plus_active=True
                                cut_equal_state=False
                            elif '-' in abcd or '+' in abcd or '/ ' in abcd or '*' in abcd:
                                f=open(r'standard/cal','r')
                                abmd=f.read()
                                f.close()

                                f=open(r'standard/cal_above','a')
                                f.write(str(abmd+'/'))
                                f.close()

                                f=open(r'standard/main','r')
                                mob=f.read()
                                f.close()

                                mob=eval(mob)
                                mob=str(mob)

                                f=open(r'standard/main','a')
                                f.write('/')
                                f.close()

                                f=open(r'standard/cal','w')
                                f.write(mob)
                                f.close()

                                plus_active=True
                            else:
                                f=open(r'standard/main','a')
                                f.write('/')
                                f.close()
                                f=open(r'standard/cal','r')
                                abmd=f.read()
                                f.close()
                                f=open(r'standard/cal_above','a')
                                f.write(str(abmd+'/'))
                                f.close()
                                plus_active=True


                        except:
                            f=open(r'standard/cal_above','a')
                            f.write(str(''))
                            f.close()

                            f=open(r'standard/main','w')
                            f.write('')
                            f.close()

                            f=open(r'standard/cal','w')
                            f.write('INVALID SYNTAX')
                            f.close()
                    elif Button_cut_rect.collidepoint(event.pos):
                        try:
                            if cut_equal_state:
                                f=open(r'standard/cal_above','w')
                                f.write('')
                                f.close()
                            else:
                                f=open(r'standard/cal','r')
                                cut_cal=f.read()
                                f.close()
                                f=open(r'standard/cal','w')
                                f.write(str(cut_cal[0:-1]))
                                f.close()

                                f=open(r'standard/main','r')
                                cut_cala=f.read()
                                f.close()

                                f=open(r'standard/main','w')
                                f.write(str(cut_cala[0:-1]))
                                f.close()
                        
                        except:
                            f=open(r'standard/cal_above','a')
                            f.write(str(''))
                            f.close()

                            f=open(r'standard/main','w')
                            f.write('')
                            f.close()

                            f=open(r'standard/cal','w')
                            f.write('INVALID SYNTAX')
                            f.close()

                        
                    elif Button_plus_minus_rect.collidepoint(event.pos):
                        f=open(r'standard/main','r')
                        equal_cal=f.read()
                        f.close()
                        try:
                            if eval(equal_cal)>=0:
                                equal_cal=str(eval(equal_cal)-(2*eval(equal_cal)))
                                f=open(r'standard/cal_above','w')
                                hg=equal_cal.replace('-','')
                                f.write(f'negative ({hg})')
                                f.close()
                            else:
                                f=open(r'standard/cal_above','w')
                                f.write(f'positive ({equal_cal})')
                                f.close()
                                equal_cal=str(int(equal_cal)-(2*int(equal_cal)))
                        except:
                            f=open(r'standard/cal_above','a')
                            f.write(str(''))
                            f.close()

                            f=open(r'standard/main','w')
                            f.write('')
                            f.close()

                            f=open(r'standard/cal','w')
                            f.write('INVALID SYNTAX')
                            f.close()

                        f=open(r'standard/main','w')
                        f.write(equal_cal)
                        f.close()


                        
                        f=open(r'standard/cal','w')
                        f.write(equal_cal)
                        f.close()

                        plus_active=True
                    elif Button_equal_rect.collidepoint(event.pos):
                        f=open(r'standard/cal_above','r')
                        sss=f.read()
                        f.close()

                        if '=' not in sss:
                            f=open(r'standard/main','r')
                            equal_cal=f.read()
                            f.close()

                            all_func_symbol=['*','/','-','+','=']
                            while equal_cal[-1] in all_func_symbol:
                                equal_cal=equal_cal[0:-1]

                            f=open(r'standard/cal','r')
                            abmd=f.read()
                            f.close()
                            f=open(r'standard/cal_above','a')
                            f.write(str(abmd+'='))
                            f.close()
                            cut_equal_state=True
                            plus_active=False
                            #all_list=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '%', '*', '/', '+', '-']
                            try:
                                evv=eval(equal_cal)
                                f=open(r'standard/cal','w')
                                f.write(str(evv))
                                f.close()
                            except:
                                f=open(r'standard/cal','w')
                                f.write('INVALID INPUT')
                                f.close()                 
                    elif Button_upon_rect.collidepoint(event.pos):
                        try:
                            f=open(r'standard/cal','r')
                            abmd=f.read()
                            f.close()

                            f=open(r'standard/cal_above','a')
                            f.write(str('1/('+abmd+')'))
                            f.close()

                            f=open(r'standard/main','w')
                            f.write(str(1/eval(abmd)))
                            f.close()

                            f=open(r'standard/cal','w')
                            f.write(str(1/eval(abmd)))
                            f.close()

                            cut_equal_state=True
                            plus_active=False
                        except:
                            f=open(r'standard/cal_above','a')
                            f.write(str(''))
                            f.close()

                            f=open(r'standard/main','w')
                            f.write('')
                            f.close()

                            f=open(r'standard/cal','w')
                            f.write('INVALID SYNTAX')
                            f.close()
                    elif Button_ro_rect.collidepoint(event.pos):
                        try:
                            f=open(r'standard/main','r')
                            equal_cal=f.read()
                            f.close()

                            f=open(r'standard/cal_above','w')
                            f.write('sq_root('+equal_cal+')')
                            f.close()

                            f=open(r'standard/main','w')
                            f.write(str(sqrt(eval(equal_cal))))
                            f.close()

                            f=open(r'standard/cal','w')
                            f.write(str(sqrt(eval(equal_cal))))
                            f.close()
                        except:
                            f=open(r'standard/cal_above','a')
                            f.write(str(''))
                            f.close()

                            f=open(r'standard/main','w')
                            f.write('')
                            f.close()

                            f=open(r'standard/cal','w')
                            f.write('INVALID SYNTAX')
                            f.close()
                    elif Button_sq_rect.collidepoint(event.pos):
                        try:
                            f=open(r'standard/main','r')
                            equal_cal=f.read()
                            f.close()

                            f=open(r'standard/cal_above','w')
                            f.write('('+equal_cal+') ²')
                            f.close()

                            f=open(r'standard/main','w')
                            f.write(str(eval(equal_cal)*eval(equal_cal)))
                            f.close()

                            f=open(r'standard/cal','w')
                            f.write(str(eval(equal_cal)*eval(equal_cal)))
                            f.close()
                        except:
                            f=open(r'standard/cal_above','a')
                            f.write(str(''))
                            f.close()

                            f=open(r'standard/main','w')
                            f.write('')
                            f.close()

                            f=open(r'standard/cal','w')
                            f.write('INVALID SYNTAX')
                            f.close()
                    elif Button_dot_rect.collidepoint(event.pos):
                        try:
                            f=open(r'standard/main','a')
                            f.write('.')
                            f.close()

                            f=open(r'standard/main','r')
                            equal_cal=f.read()
                            f.close()


                            f=open(r'standard/cal_above','a')
                            f.write('.')
                            f.close()
                            
                            f=open(r'standard/cal','a')
                            f.write('.')
                            f.close()
                        except:
                            f=open(r'standard/cal_above','a')
                            f.write(str(''))
                            f.close()

                            f=open(r'standard/main','w')
                            f.write('')
                            f.close()

                            f=open(r'standard/cal','w')
                            f.write('INVALID SYNTAX')
                            f.close()
                    elif Button_ce_rect.collidepoint(event.pos):
                        try:
                            f=open(r'standard/cal','r')
                            cut_cal=f.read()
                            f.close()

                            ce_cutting_process=len(cut_cal)


                            f=open(r'standard/cal','w')
                            f.write(str(cut_cal[0:-(ce_cutting_process)]))
                            f.close()

                            f=open(r'standard/main','r')
                            cut_cala=f.read()
                            f.close()

                            f=open(r'standard/main','w')
                            f.write(str(cut_cala[0:-(ce_cutting_process)]))
                            f.close()

                        except:
                            pass
                    elif Button_report_rect.collidepoint(event.pos):
                        try:
                            url = "http://www.kite.com"
                            request = requests.get(url)
                        except:
                            report_failed_of_internet_status=1

                        if report_failed_of_internet_status==0:
                            f=open(r'standard/cal_above','r')
                            sss=f.read()
                            f.close()
                            if len(sss)<2:
                                report_failed_of_calculation=True
                            else:
                                if '=' not in sss:
                                    f=open(r'standard/main','r')
                                    equal_cal=f.read()
                                    f.close()

                                    all_func_symbol=['*','/','-','+','=']
                                    while equal_cal[-1] in all_func_symbol:
                                        equal_cal=equal_cal[0:-1]

                                    f=open(r'standard/cal','r')
                                    abmd=f.read()
                                    f.close()
                                    f=open(r'standard/cal_above','a')
                                    f.write(str(abmd+'='))
                                    f.close()
                                    try:
                                        evv=eval(equal_cal)
                                        f=open(r'standard/cal','w')
                                        f.write(str(evv))
                                        f.close()
                                        f=open(r'standard/report_conf','w')
                                        f.write('y')
                                        f.close()
                                    except:
                                        f=open(r'standard/cal','w')
                                        f.write('INVALID INPUT')
                                        f.close()
                                        f=open(r'standard/report_conf','w')
                                        f.write('n')
                                        f.close()
                                f=open(r'standard/report_conf','r')
                                checking_report=f.read()
                                f.close()

                                if 'y' in checking_report :
                                    f=open(r'standard/cal_above','r')
                                    reporting_google=f.read()
                                    f.close()
                                    if len(reporting_google)>1:
                                        searching_online(reporting_google)
                        else:
                            report_failed_of_internet=True
                    elif Button_enlarge_rect.collidepoint(event.pos):
                        pin_to_top()
                    elif Button_menu_butt_rect.collidepoint(event.pos):
                        option_screen=True
                        standard_screen_typing=False
                        option_screen_count_clicks=1
                elif standard_screen and option_screen:
                    if Button_aboutus_rect.collidepoint(event.pos):
                        about_dev=True
                    elif Button_request_rect.collidepoint(event.pos):
                        get_feature()
                    elif Button_menu_butt_rect.collidepoint(event.pos):
                        option_screen=False
                        standard_screen_typing=True
                    elif option_rating_rect.collidepoint(event.pos):
                        standard_screen=False
                        standard_screen_typing=False
                        review_screen=True
                        review_screen_1=True
                        pygame.display.set_mode((719,352))
                        pygame.display.set_caption('Calculator-Review')
                        pygame.display.set_icon(pygame_icon1)
                
                
                elif about_dev:
                    if fohts_rect.collidepoint(event.pos):
                        pygame.display.set_mode((320,505))
                        about_dev=False
                        standard_screen=True
                        standard_screen_typing=True
                        option_screen=False

                elif review_screen:
                    option_screen=False
                    if review_screen_1:
                        if review_1_rect.collidepoint(event.pos):
                            f=open(r'rate/image','w')
                            f.write('1')
                            f.close()
                            review_screen_1=False
                            review_screen_2=True
                        elif review_2_rect.collidepoint(event.pos):
                            f=open(r'rate/image','w')
                            f.write('2')
                            f.close()
                            review_screen_1=False
                            review_screen_2=True
                        elif review_3_rect.collidepoint(event.pos):
                            f=open(r'rate/image','w')
                            f.write('3')
                            f.close()
                            review_screen_1=False
                            review_screen_2=True
                        elif review_4_rect.collidepoint(event.pos):
                            f=open(r'rate/image','w')
                            f.write('4')
                            f.close()
                            review_screen_1=False
                            review_screen_2=True
                        elif review_5_rect.collidepoint(event.pos):
                            f=open(r'rate/image','w')
                            f.write('5')
                            f.close()
                            review_screen_1=False
                            review_screen_2=True
                        elif back_button_rect.collidepoint(event.pos):
                            review_screen_1=False
                            standard_screen=True
                            standard_screen_typing=True
                            pygame.display.set_mode((320,505))
                            pygame.display.set_caption('Calculator')
                            pygame.display.set_icon(pygame_icon)
                    elif review_screen_2:
                        if review_write_rect.collidepoint(event.pos):
                            writs()
                            review_screen_3=True
                            review_screen_2=False
                        if back_button_rect.collidepoint(event.pos):
                            review_screen_2=False
                            review_screen_1=True
                    elif review_screen_3:
                        if review_welcome_rect.collidepoint(event.pos):
                            review_screen_3=False
                            review_screen=False
                            standard_screen=True
                            standard_screen_typing=True
                            option_screen=False
                            pygame.display.set_mode((320,505))
                            pygame.display.set_caption('Calculator')
                            pygame.display.set_icon(pygame_icon)

            if event.type==pygame.KEYDOWN :

                if standard_screen:
                    if event.key==pygame.K_0 or event.key==pygame.K_KP0 :
                        pygame.mouse.set_pos(Button_0_rect.x+35,Button_0_rect.y+20)
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('0')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('0')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('0')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False
                        else:
                            f=open(r'standard/cal','a')
                            f.write('0')
                            f.close()

                        f=open(r'standard/main','a')
                        f.write('0')
                        f.close()
                    elif event.key==pygame.K_1 or event.key==pygame.K_KP1:
                        pygame.mouse.set_pos(Button_1_rect.x+35,Button_1_rect.y+20)
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('1')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('1')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('1')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('1')
                            f.close()
                        f=open(r'standard/main','a')
                        f.write('1')
                        f.close()
                    elif event.key==pygame.K_2 or event.key==pygame.K_KP2:
                        pygame.mouse.set_pos(Button_2_rect.x+35,Button_2_rect.y+20)
                        f=open(r'standard/main','a')
                        f.write('2')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('2')
                            f.close()
                            plus_active=False

                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('2')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('2')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('2')
                            f.close()
                    elif event.key==pygame.K_3 or event.key==pygame.K_KP3:
                        pygame.mouse.set_pos(Button_3_rect.x+35,Button_3_rect.y+20)
                        f=open(r'standard/main','a')
                        f.write('3')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('3')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('3')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('3')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('3')
                            f.close()
                    elif event.key==pygame.K_4 or event.key==pygame.K_KP4:
                        pygame.mouse.set_pos(Button_4_rect.x+35,Button_4_rect.y+20)
                        f=open(r'standard/main','a')
                        f.write('4')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('4')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('4')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('4')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('4')
                            f.close()
                    elif event.key==pygame.K_5 or event.key==pygame.K_KP5:
                        pygame.mouse.set_pos(Button_5_rect.x+35,Button_5_rect.y+20)
                        f=open(r'standard/main','a')
                        f.write('5')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('5')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('5')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('5')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('5')
                            f.close()
                    elif event.key==pygame.K_6 or event.key==pygame.K_KP6:
                        pygame.mouse.set_pos(Button_6_rect.x+35,Button_6_rect.y+20)
                        f=open(r'standard/main','a')
                        f.write('6')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('6')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('6')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('6')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('6')
                            f.close()
                    elif event.key==pygame.K_7 or event.key==pygame.K_KP7:
                        pygame.mouse.set_pos(Button_7_rect.x+35,Button_7_rect.y+20)
                        f=open(r'standard/main','a')
                        f.write('7')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('7')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('7')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('7')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('7')
                            f.close()
                    elif event.key==pygame.K_8 or event.key==pygame.K_KP8:
                        pygame.mouse.set_pos(Button_8_rect.x+35,Button_8_rect.y+20)
                        f=open(r'standard/main','a')
                        f.write('8')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('8')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('8')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('8')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('8')
                            f.close()
                    elif event.key==pygame.K_9 or event.key==pygame.K_KP9:
                        pygame.mouse.set_pos(Button_9_rect.x+35,Button_9_rect.y+20)
                        f=open(r'standard/main','a')
                        f.write('9')
                        f.close()
                        if plus_active:
                            f=open(r'standard/cal','w')
                            f.write('9')
                            f.close()
                            plus_active=False
                        elif cut_equal_state:
                            f=open(r'standard/cal','w')
                            f.write('9')
                            f.close()
                            f=open(r'standard/main','w')
                            f.write('9')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                            cut_equal_state=False

                        else:
                            f=open(r'standard/cal','a')
                            f.write('9')
                            f.close()

                    elif event.key==pygame.K_c:
                        pygame.mouse.set_pos(Button_C_rect.x+35,Button_C_rect.y+20)
                        clear_all()
                        start=0
                        cut_equal_state=False
                    elif event.key==pygame.K_KP_PLUS:
                        pygame.mouse.set_pos(Button_plus_rect.x+35,Button_plus_rect.y+20)
                        if cut_equal_state:
                            f=open(r'standard/main','w')
                            f.write('/')
                            f.close()
                            f=open(r'standard/cal','w')
                            abmd=f.write('')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('/')
                            f.close()
                            plus_active=True
                            cut_equal_state=False
                        else:
                            f=open(r'standard/main','a')
                            f.write('+')
                            f.close()

                            f=open(r'standard/cal','r')
                            abmd=f.read()
                            f.close()
                            f=open(r'standard/cal_above','a')
                            f.write(str(abmd+'+'))
                            f.close()

                            plus_active=True

                    elif event.key==pygame.K_MINUS or event.key==pygame.K_KP_MINUS:
                        pygame.mouse.set_pos(Button_minus_rect.x+35,Button_minus_rect.y+20)
                        if cut_equal_state:
                            f=open(r'standard/main','w')
                            f.write('-')
                            f.close()
                            f=open(r'standard/cal','w')
                            abmd=f.write('')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('-')
                            f.close()
                            plus_active=True
                            cut_equal_state=False
                        else:
                            f=open(r'standard/main','a')
                            f.write('-')
                            f.close()
                            f=open(r'standard/cal','r')
                            abmd=f.read()
                            f.close()
                            f=open(r'standard/cal_above','a')
                            f.write(str(abmd+'-'))
                            f.close()
                            plus_active=True
                    elif event.key==pygame.K_ASTERISK or event.key==pygame.K_KP_MULTIPLY:
                        pygame.mouse.set_pos(Button_multi_rect.x+35,Button_multi_rect.y+20)
                        if cut_equal_state:
                            f=open(r'standard/main','w')
                            f.write('*')
                            f.close()
                            f=open(r'standard/cal','w')
                            abmd=f.write('')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('*')
                            f.close()
                            plus_active=True
                            cut_equal_state=False
                        else:

                            f=open(r'standard/main','a')
                            f.write('*')
                            f.close()

                            f=open(r'standard/cal','r')
                            abmd=f.read()
                            f.close()
                            f=open(r'standard/cal_above','a')
                            f.write(str(abmd+'*'))
                            f.close()
                            plus_active=True
                    elif event.key==pygame.K_SLASH:
                        pygame.mouse.set_pos(Button_divide_rect.x+35,Button_divide_rect.y+20)
                        if cut_equal_state:
                            f=open(r'standard/main','w')
                            f.write('/')
                            f.close()
                            f=open(r'standard/cal','w')
                            abmd=f.write('')
                            f.close()
                            f=open(r'standard/cal_above','w')
                            f.write('/')
                            f.close()
                            plus_active=True
                            cut_equal_state=False
                        else:
                            f=open(r'standard/main','a')
                            f.write('/')
                            f.close()
                            f=open(r'standard/cal','r')
                            abmd=f.read()
                            f.close()
                            f=open(r'standard/cal_above','a')
                            f.write(str(abmd+'/'))
                            f.close()
                            plus_active=True
                    elif event.key==pygame.K_BACKSPACE :
                        pygame.mouse.set_pos(Button_cut_rect.x+35,Button_cut_rect.y+20)
                        if cut_equal_state:
                            f=open(r'standard/cal_above','w')
                            f.write('')
                            f.close()
                        else:
                            f=open(r'standard/cal','r')
                            cut_cal=f.read()
                            f.close()
                            f=open(r'standard/cal','w')
                            f.write(str(cut_cal[0:-1]))
                            f.close()

                            f=open(r'standard/main','r')
                            cut_cala=f.read()
                            f.close()

                            f=open(r'standard/main','w')
                            f.write(str(cut_cala[0:-1]))
                            f.close()

                    elif event.key==pygame.K_p:
                        f=open(r'standard/main','r')
                        equal_cal=f.read()
                        f.close()
                        try:
                            if eval(equal_cal)>=0:
                                equal_cal=str(eval(equal_cal)-(2*eval(equal_cal)))
                                f=open(r'standard/cal_above','w')
                                f.write(f'negative ({equal_cal})')
                                f.close()
                        except:
                            f=open(r'standard/cal_above','w')
                            f.write(f'positive ({equal_cal})')
                            f.close()
                            equal_cal=str(int(equal_cal)-(2*int(equal_cal)))

                        f=open(r'standard/main','w')
                        f.write(equal_cal)
                        f.close()


                        
                        f=open(r'standard/cal','w')
                        f.write(equal_cal)
                        f.close()

                    elif event.key==pygame.K_KP_ENTER  :
                        pygame.mouse.set_pos(Button_equal_rect.x+35,Button_equal_rect.y)
                        f=open(r'standard/main','r')
                        equal_cal=f.read()
                        f.close()

                        f=open(r'standard/cal','r')
                        abmd=f.read()
                        f.close()
                        f=open(r'standard/cal_above','a')
                        f.write(str(abmd+'='))
                        f.close()
                        cut_equal_state=True
                        plus_active=False
                        #all_list=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '%', '*', '/', '+', '-']
                        try:
                            evv=eval(equal_cal)
                            f=open(r'standard/cal','w')
                            f.write(str(evv))
                            f.close()
                        except:
                            f=open(r'standard/cal','w')
                            f.write('INVALID INPUT')
                            f.close()


        
    if game_active:
        if standard_screen:

            if Button_0_rect.collidepoint(pygame.mouse.get_pos()):
                Button_0_photo=pygame.image.load(r'standard\01.png')
            else:
                Button_0_photo=pygame.image.load(r'standard\0.png')
            if Button_1_rect.collidepoint(pygame.mouse.get_pos()):
                Button_1_photo=pygame.image.load(r'standard\11.png')
            else:
                Button_1_photo=pygame.image.load(r'standard\1.png')
            if Button_2_rect.collidepoint(pygame.mouse.get_pos()):
                Button_2_photo=pygame.image.load(r'standard\21.png')
            else:
                Button_2_photo=pygame.image.load(r'standard\2.png')
            if Button_3_rect.collidepoint(pygame.mouse.get_pos()):
                Button_3_photo=pygame.image.load(r'standard\31.png')
            else:
                Button_3_photo=pygame.image.load(r'standard\3.png')
            if Button_4_rect.collidepoint(pygame.mouse.get_pos()):
                Button_4_photo=pygame.image.load(r'standard\41.png')
            else:
                Button_4_photo=pygame.image.load(r'standard\4.png')
            if Button_5_rect.collidepoint(pygame.mouse.get_pos()):
                Button_5_photo=pygame.image.load(r'standard\51.png')
            else:
                Button_5_photo=pygame.image.load(r'standard\5.png')
            if Button_6_rect.collidepoint(pygame.mouse.get_pos()):
                Button_6_photo=pygame.image.load(r'standard\61.png')
            else:
                Button_6_photo=pygame.image.load(r'standard\6.png')
            if Button_7_rect.collidepoint(pygame.mouse.get_pos()):
                Button_7_photo=pygame.image.load(r'standard\71.png')
            else:
                Button_7_photo=pygame.image.load(r'standard\7.png')
            if Button_8_rect.collidepoint(pygame.mouse.get_pos()):
                Button_8_photo=pygame.image.load(r'standard\81.png')
            else:
                Button_8_photo=pygame.image.load(r'standard\8.png')
            if Button_9_rect.collidepoint(pygame.mouse.get_pos()):
                Button_9_photo=pygame.image.load(r'standard\91.png')
            else:
                Button_9_photo=pygame.image.load(r'standard\9.png')
            if Button_dot_rect.collidepoint(pygame.mouse.get_pos()):
                Button_dot_photo=pygame.image.load(r'standard\d1.png')
            else:
                Button_dot_photo=pygame.image.load(r'standard\d.png')
            if Button_multi_rect.collidepoint(pygame.mouse.get_pos()):
                Button_multi_photo=pygame.image.load(r'standard\x1.png')
            else:
                Button_multi_photo=pygame.image.load(r'standard\x.png')
            if Button_plus_rect.collidepoint(pygame.mouse.get_pos()):
                Button_plus_photo=pygame.image.load(r'standard\+1.png')
            else:
                Button_plus_photo=pygame.image.load(r'standard\+.png')
            if Button_minus_rect.collidepoint(pygame.mouse.get_pos()):
                Button_minus_photo=pygame.image.load(r'standard\-1.png')
            else:
                Button_minus_photo=pygame.image.load(r'standard\-.png')
            if Button_divide_rect.collidepoint(pygame.mouse.get_pos()):
                Button_divide_photo=pygame.image.load(r'standard\di1.png')
            else:
                Button_divide_photo=pygame.image.load(r'standard\di.png')
            if Button_C_rect.collidepoint(pygame.mouse.get_pos()):
                Button_C_photo=pygame.image.load(r'standard\c1.png')
            else:
                Button_C_photo=pygame.image.load(r'standard\c.png')
            if Button_ce_rect.collidepoint(pygame.mouse.get_pos()):
                Button_ce_photo=pygame.image.load(r'standard\ce1.png')
            else:
                Button_ce_photo=pygame.image.load(r'standard\ce.png')
            if Button_plus_minus_rect.collidepoint(pygame.mouse.get_pos()):
                Button_plus_minus_photo=pygame.image.load(r'standard\+-1.png')
            else:
                Button_plus_minus_photo=pygame.image.load(r'standard\+-.png')
            if Button_equal_rect.collidepoint(pygame.mouse.get_pos()):
                Button_equal_photo=pygame.image.load(r'standard\=1.png')
            else:
                Button_equal_photo=pygame.image.load(r'standard\=.png')
            if Button_per_rect.collidepoint(pygame.mouse.get_pos()):
                Button_per_photo=pygame.image.load(r'standard\per1.png')
            else:
                Button_per_photo=pygame.image.load(r'standard\per.png')
            if Button_cut_rect.collidepoint(pygame.mouse.get_pos()):
                Button_cut_photo=pygame.image.load(r'standard\cut1.png')
            else:
                Button_cut_photo=pygame.image.load(r'standard\cut.png')
            if Button_sq_rect.collidepoint(pygame.mouse.get_pos()):
                Button_sq_photo=pygame.image.load(r'standard\sq1.png')
            else:
                Button_sq_photo=pygame.image.load(r'standard\sq.png')
            if Button_ro_rect.collidepoint(pygame.mouse.get_pos()):
                Button_ro_photo=pygame.image.load(r'standard\ro1.png')
            else:
                Button_ro_photo=pygame.image.load(r'standard\ro.png')
            if Button_upon_rect.collidepoint(pygame.mouse.get_pos()):
                Button_upon_photo=pygame.image.load(r'standard\upon1.png')
            else:
                Button_upon_photo=pygame.image.load(r'standard\upon.png')
            if Button_report_rect.collidepoint(pygame.mouse.get_pos()):
                Button_report_photo=pygame.image.load(r'standard\report1.png')
            else:
                Button_report_photo=pygame.image.load(r'standard\report.png')
            if Button_enlarge_rect.collidepoint(pygame.mouse.get_pos()):
                Button_enlarge_photo=pygame.image.load(r'standard\enlarge1.png')
            else:
                Button_enlarge_photo=pygame.image.load(r'standard\enlarge.png')
            if Button_menu_butt_rect.collidepoint(pygame.mouse.get_pos()):
                Button_menu_butt_photo=pygame.image.load(r'standard\menu_butt1.png')
            else:
                Button_menu_butt_photo=pygame.image.load(r'standard\menu_butt.png')




            screen.blit(bg_surface,(0,0))

            

            screen.blit(Button_0_photo,Button_0_rect)
            screen.blit(Button_1_photo,Button_1_rect)
            screen.blit(Button_2_photo,Button_2_rect)
            screen.blit(Button_3_photo,Button_3_rect)
            screen.blit(Button_4_photo,Button_4_rect)
            screen.blit(Button_5_photo,Button_5_rect)
            screen.blit(Button_6_photo,Button_6_rect)
            screen.blit(Button_7_photo,Button_7_rect)
            screen.blit(Button_8_photo,Button_8_rect)
            screen.blit(Button_9_photo,Button_9_rect)
            screen.blit(Button_plus_minus_photo,Button_plus_minus_rect)
            screen.blit(Button_dot_photo,Button_dot_rect)
            screen.blit(Button_equal_photo,Button_equal_rect)
            screen.blit(Button_plus_photo,Button_plus_rect)
            screen.blit(Button_multi_photo,Button_multi_rect)
            screen.blit(Button_minus_photo,Button_minus_rect)
            screen.blit(Button_divide_photo,Button_divide_rect)
            screen.blit(Button_C_photo,Button_C_rect)
            screen.blit(Button_ce_photo,Button_ce_rect)
            screen.blit(Button_per_photo,Button_per_rect)
            screen.blit(Button_cut_photo,Button_cut_rect)
            screen.blit(Button_sq_photo,Button_sq_rect)
            screen.blit(Button_ro_photo,Button_ro_rect)
            screen.blit(Button_upon_photo,Button_upon_rect)
            if option_screen:
                screen.blit(Button_options_photo,(0,40))
                screen.blit(Button_aboutus_photo,Button_aboutus_rect)
                screen.blit(Button_request_photo,Button_request_rect)
                screen.blit(option_rating_photo,option_rating_rect)
            screen.blit(Button_menu_butt_photo,Button_menu_butt_rect)
            screen.blit(Button_report_photo,Button_report_rect)
            screen.blit(Button_enlarge_photo,Button_enlarge_rect)

            pygame.font.init() 
            
            f=open(r'standard/cal','r')
            calculation=f.read()
            f.close()

            cal_len=len(calculation)
            if cal_len<10:
                myfont = pygame.font.SysFont('Lucida Fax', 40)
                textsurface = myfont.render(calculation, False, (255, 255, 255))
                textsurface_rect=textsurface.get_rect(bottomright=(300,150))
            else:
                myfont = pygame.font.SysFont('Lucida Fax', 20)
                textsurface = myfont.render(calculation, False, (255, 255, 255))
                textsurface_rect=textsurface.get_rect(bottomright=(300,150))
            

            f=open(r'standard/cal_above','r')
            calculation_re=f.read()
            f.close()

            myfonte = pygame.font.SysFont('Lucida Fax', 15)
            textsur = myfonte.render(calculation_re, False, (255, 255, 255))
            textsur_rect=textsur.get_rect(bottomright=(280,80))
                
            screen.blit(textsurface,textsurface_rect)
            screen.blit(textsur,textsur_rect)


            if report_failed_of_internet:
                report_failed_of_internet_count+=1/20
                if report_failed_of_internet_count<5:
                    screen.blit(Button_no_int_photo,(20,450))
                else:
                    report_failed_of_internet_count=0
                    report_failed_of_internet=False
            
            elif report_failed_of_calculation:
                report_failed_of_internet_count+=1/20
                if report_failed_of_internet_count<5:
                    screen.blit(Button_no_int_photo1,(20,450))
                else:
                    report_failed_of_internet_count=0
                    report_failed_of_calculation=False

        if about_dev:
            standard_screen=False
            standard_screen_typing=False
            pygame.display.set_mode((952,500))
            screen.blit(abo,(0,0))
            screen.blit(fohts,fohts_rect)

        if review_screen:
            if review_screen_1:
                if review_1_rect.collidepoint(pygame.mouse.get_pos()):
                    review_1_photo=pygame.image.load(r'rate\11.png')
                else:
                    review_1_photo=pygame.image.load(r'rate\1.png')

                if review_2_rect.collidepoint(pygame.mouse.get_pos()):
                    review_2_photo=pygame.image.load(r'rate\21.png')
                else:
                    review_2_photo=pygame.image.load(r'rate\2.png')

                if review_3_rect.collidepoint(pygame.mouse.get_pos()):
                    review_3_photo=pygame.image.load(r'rate\31.png')
                else:
                    review_3_photo=pygame.image.load(r'rate\3.png')

                if review_4_rect.collidepoint(pygame.mouse.get_pos()):
                    review_4_photo=pygame.image.load(r'rate\41.png')
                else:
                    review_4_photo=pygame.image.load(r'rate\4.png')

                if review_5_rect.collidepoint(pygame.mouse.get_pos()):
                    review_5_photo=pygame.image.load(r'rate\51.png')
                else:
                    review_5_photo=pygame.image.load(r'rate\5.png')


                screen.blit(review_main_photo,(0,0))
                screen.blit(review_1_photo,review_1_rect)
                screen.blit(review_2_photo,review_2_rect)
                screen.blit(review_3_photo,review_3_rect)
                screen.blit(review_4_photo,review_4_rect)
                screen.blit(review_5_photo,review_5_rect)
                screen.blit(back_button_photo,back_button_rect)
            if review_screen_2:
                screen.fill((255,255,255))
                f=open(r'rate/image','r')
                rate_image=f.read()
                f.close()

                rate_chossen_image=pygame.image.load(f'rate\{rate_image}.png') 
                screen.blit(rate_chossen_image,(300,0))
                screen.blit(review_write_photo,review_write_rect)
                screen.blit(back_button_photo,back_button_rect)
            if review_screen_3:
                screen.blit(photo_thanks,(0,0))
                screen.blit(review_welcome_photo,review_welcome_rect)




    pygame.display.update()
    clock.tick(30)