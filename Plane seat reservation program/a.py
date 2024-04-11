from tkinter import *
from functools import partial
from mysql.connector import connect

db = connect(host="localhost",user="root",password="1234")
cursor = db.cursor()

try:
    open("login.txt")
    cursor.execute("use seat")
except:
    cursor.execute("CREATE DATABASE seat")
    cursor.execute("use seat")
    cursor.execute("create table main(name varchar(30) PRIMARY KEY,age int,gender varchar(10),seat varchar(5),fare int)")
    db.commit()
    open("login.txt","w").close()
BACKGROUND_COLOR = "#F0F0F0"
PASSWORD = "shaunak"

def load_random_fare_func():
    from random import randint
    load_random_fare.clear()
    for i in range(90):
        a = []
        for i in range(6):
            a.append(randint(4000,7000))
        load_random_fare.append(a)

load_random_fare = []
load_random_fare_func()

def load_home():
    welcome.place(x=0,y=100)
    option1.place(x=120,y=250)
    option2.place(x=320,y=250)
    option3.place(x=520,y=250)
    option5.place(x=120,y=380)
    option6.place(x=320,y=380)

def home_out():
    welcome.place_forget()
    option1.place_forget()
    option2.place_forget()
    option3.place_forget()
    option5.place_forget()
    option6.place_forget()

def check_login(event=None):
    pw = login_input.get().strip()
    if pw == PASSWORD:
        login_out()
        load_home()
    else:
        login_error.place(x=50,y=180)

def login():
    welcome_login.place(x=40,y=40)
    login_name_label.place(x=50,y=150)
    login_input.place(x=50,y=220)
    login_submit.place(x=260,y=300)

def login_out():
    welcome_login.destroy()
    login_name_label.destroy()
    login_input.destroy()
    login_submit.destroy()
    login_error.destroy()

def on_mouse_scroll(event):
    if event.delta:
        canvas.yview_scroll(-1*(event.delta//120), "units")
    else:
        if event.num == 5:
            move = 1
        else:
            move = -1

        canvas.yview_scroll(move, "units")

def on_mouse_scroll_choose(event):
    if event.delta:
        choose_canvas.yview_scroll(-1*(event.delta//120), "units")
    else:
        if event.num == 5:
            move = 1
        else:
            move = -1

        choose_canvas.yview_scroll(move, "units")

view_list=[]

def view_seat():
    home_out()
    view_label.pack()
    view_back.place(x=10,y=-20)
    view_text.place(x=100,y=0)
    update_booked_seat()
    
    canvas.bind_all("<MouseWheel>", on_mouse_scroll)
    lis ="1ABC1DEF"
    view_list.append(Label(canvas,width=100,bg="white"))
    view_list[-1].place(x=0,y=0)
    for j in range(8):
        if j in [0,4]:
            view_list.append(Label(canvas,text="",bg="white"))
            view_list[-1].grid(row=0,column=j,padx=10,pady=2)
        else:
            view_list.append(Label(canvas,text=lis[j],width=4,bg="white"))
            view_list[-1].grid(row=0,column=j,padx=10,pady=2)
    for i in range(91):
        if i==0:
            view_list.append(Label(scrollable_frame,text=""))
            view_list[-1].grid(row=i,column=j,padx=10,pady=2)
            continue
        for j in range(8):
            if j==0:
                view_list.append(Label(scrollable_frame,text=str(i),bg="white"))
                view_list[-1].grid(row=i,column=j,padx=10,pady=2)
            elif j==4:    
                view_list.append(Label(scrollable_frame,text="",bg="white"))
                view_list[-1].grid(row=i,column=j,padx=10,pady=2)
            else:
                # booked_seat = [ (1,2) , (3,4) ]
                if (i,j) in booked_seat:
                    view_list.append(Button(scrollable_frame,bd=1,width=5,bg="red",cursor="hand2"))
                else:
                    view_list.append(Button(scrollable_frame,width=5,bd=1,bg="green",cursor="hand2"))

                view_list[-1].grid(row=i,column=j,padx=5,pady=2)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def view_out():
    canvas.unbind_all("<MouseWheel>")
    canvas.pack_forget()
    scrollbar.pack_forget()
    view_label.pack_forget()
    view_back.place_forget()
    view_text.place_forget()
    for i in view_list:
        i.pack_forget()
    view_list.clear()
    load_home()

choose_list = []
update_seat_data = ["name","age","gender","seat","fare"] 
booked_seat=[] #contains tuple (row,column)
def update_booked_seat():
    booked_seat.clear()
    cursor.execute("select seat from MAIN")
    a = cursor.fetchall()
    seat = "abc&def"
    for i in a:
        booked_seat.append((int(i[0][0:-1]),seat.find(i[0][-1])+1))

def seat_book():
    cd = "insert into MAIN values('%s',%d,'%s','%s',%d)"%(update_seat_data[0],int(update_seat_data[1]),update_seat_data[2],update_seat_data[3],int(update_seat_data[4]))
    cursor.execute(cd)
    db.commit()
    choose_seat_out()
    
def choose_seat_in():
    home_out()
    create_out()
    update_booked_seat()
    update_seat_data[0] = create_name_input.get()
    update_seat_data[1] = create_age_input.get()
    update_seat_data[2] = create_gender_input.get()
    create_age_input.delete(0,END)
    create_name_input.delete(0,END)
    create_gender_input.delete(0,END)
    choose_label.pack()
    choose_canvas.bind_all("<MouseWheel>", on_mouse_scroll_choose)
    choose_back.place(x=10,y=-20)
    choose_text.place(x=100,y=0)
    choose_seat.place(x=600,y=0)
    choose_submit.place(x=700,y=0)
    lis ="1ABC1DEF"
    choose_list.append(Label(choose_canvas,width=100,bg="white"))
    choose_list[-1].place(x=0,y=0)
    def choosed(row,column,fare):
        seat = "abc&def"
        choosen_seat = str(row)+seat[column-1]
        update_seat_data[3] = choosen_seat
        update_seat_data[4] = fare
        choose_seat.config(text="seat : "+choosen_seat)

    for j in range(8):
        if j in [0,4]:
            choose_list.append(Label(choose_canvas,text="  ",bg="white"))
            choose_list[-1].grid(row=0,column=j,padx=10,pady=2)
            # pass
        else:
            choose_list.append(Label(choose_canvas,text=" "+lis[j],font=("microsoft yahei light",11),width=7,bg="white"))
            choose_list[-1].grid(row=0,column=j,padx=10,pady=2)
    for i in range(91):
        if i==0:
            choose_list.append(Label(choose_scrollable_frame,text="",))
            choose_list[-1].grid(row=i,column=j,padx=10,pady=2)
            continue
        for j in range(8):
            if j==0:
                choose_list.append(Label(choose_scrollable_frame,text=str(i),bg="white"))
                choose_list[-1].grid(row=i,column=j,padx=10,pady=2)
            elif j==4:    
                choose_list.append(Label(choose_scrollable_frame,text="",bg="white"))
                choose_list[-1].grid(row=i,column=j,padx=10,pady=2)
            else:
                if (i,j) in booked_seat:
                    choose_list.append(Button(choose_scrollable_frame,bd=0,bg="red",text="",font=("microsoft yahei light",15),width=7,cursor="hand2"))
                    choose_list[-1].grid(row=i,column=j,padx=5,pady=5)
                else:
                    # random_fare = [ [4365,1345,2346,5246,2345,3246] , [13589,3450,3462346,2345,3254,345]  ]
                    if j>4:
                        fare = load_random_fare[i-1][j-2]
                    else:
                        fare = load_random_fare[i-1][j-1]
                    choose_list.append(Button(choose_scrollable_frame,bd=0,bg="lightgreen",text="₹ "+str(fare),font=("microsoft yahei light",15),width=7,cursor="hand2",command=partial(choosed,i,j,fare)))
                    choose_list[-1].grid(row=i,column=j,padx=5,pady=5)
    choose_canvas.pack(side="left", fill="both", expand=True)
    choose_scrollbar.pack(side="right", fill="y")

def choose_seat_out():
    choose_canvas.unbind("<MouseWheel>")
    choose_submit.place_forget()
    choose_seat.place_forget()
    choose_back.place_forget()
    choose_text.place_forget()
    choose_canvas.pack_forget()
    choose_scrollbar.pack_forget()
    choose_label.pack_forget()
    for i in choose_list:
        i.pack_forget()
    choose_list.clear()
    load_home()

def found():
    user_find_out()
    name = user_input.get().lower()
    booked_seat.clear()
    cursor.execute("select * from MAIN")
    a = cursor.fetchall()
    datas = {}
    for i in a:
        datas[i[0].lower()] = i[1:]
    if name in datas:
        fd = datas[name]
        user_found_name.config(text="Name : "+name)
        user_found_age.config(text="Age : "+str(fd[0]))
        user_found_gender.config(text="Gender : "+fd[1])
        user_found_seat.config(text="Seat : "+str(fd[2]))
        user_found_fare.config(text="Fare : "+str(fd[3]))
        return finds(1)
    else:
        return finds(0)

def user_find_out():
    user_found.place_forget()
    user_found_name.place_forget()
    user_found_age.place_forget()
    user_found_gender.place_forget()
    user_not.place_forget()
    user_found_seat.place_forget()
    user_found_fare.place_forget()

def finds(find):
    if find == 1:
        user_found.place(x=350,y=250)
        user_found_name.place(x=350,y=300)
        user_found_age.place(x=350,y=330)
        user_found_gender.place(x=350,y=330)
        user_found_seat.place(x=350,y=360)
        user_found_fare.place(x=350,y=390)
    else:
        user_not.place(x=350,y=220)
    
def user_in():
    home_out()
    user_back.place(x=0,y=-20)
    user_title.place(x=100,y=0)
    user_name.place(x=20,y=100)
    user_input.place(x=20,y=160)  
    user_submit.place(x=20,y=260) 

def user_out():
    user_back.place_forget()
    user_title.place_forget()
    user_name.place_forget()
    user_input.place_forget()
    user_not.place_forget()
    user_submit.place_forget()
    user_found.place_forget()
    user_found_name.place_forget()
    user_found_age.place_forget()
    user_found_gender.place_forget()
    user_found_seat.place_forget()
    user_found_fare.place_forget()
    load_home()

def create_in():
    home_out()
    create_back.place(x=0,y=-20)
    create_title.place(x=100,y=0)
    create_name.place(x=30,y=100)
    create_name_input.place(x=30,y=150)
    create_age.place(x=30,y=210)
    create_age_input.place(x=30,y=260)
    create_gender.place(x=30,y=320)
    create_gender_input.place(x=30,y=370)
    create_choose_seat.place(x=350,y=420)

def create_out():
    create_back.place_forget()
    create_title.place_forget()
    create_name.place_forget()
    create_name_input.place_forget()
    create_age.place_forget()
    create_age_input.place_forget()
    create_gender.place_forget()
    create_gender_input.place_forget()
    create_choose_seat.place_forget()
    load_home()

def delete_check():
    name = delete_input.get().lower()
    lis = []
    cursor.execute("select name from MAIN")
    a = cursor.fetchall()    # [("pranay",),("shaunak",)]
    for i in a:
        lis.append(i[0].lower())
    if name in lis:
        cd = "DELETE FROM MAIN where name = '%s'"%name
        cursor.execute(cd)
        db.commit()  
        delete_found.place(x=30,y=220)
    else:
        delete_not.place(x=30,y=220)

def delete_in():
    home_out()
    delete_back.place(x=0,y=-20)
    delete_title.place(x=100,y=0)
    delete_name.place(x=20,y=100)
    delete_input.place(x=20,y=150)
    delete_submit.place(x=20,y=280)

def delete_out():
    delete_back.place_forget()
    delete_title.place_forget()
    delete_name.place_forget()
    delete_input.place_forget()
    delete_not.place_forget()
    delete_submit.place_forget()
    delete_found.place_forget()
    load_home()


window = Tk()
window.title("Seat Reservation")
window.geometry("800x500")
window.resizable(0,0)
window.config(bg=BACKGROUND_COLOR)
welcome = Label(window,text="Welcome to plane seat reservation program!",bd=0,font=("microsoft yahei light",30))
option1 = Button(window,text="View all Seat",cursor="hand2",bd=0,width=10,height=3,font=("microsoft yahei light",16),command=lambda:view_seat())
option2 = Button(window,text="View User's\nReservation",cursor="hand2",bd=0,width=10,height=3,font=("microsoft yahei light",16),command=lambda:user_in())
option3 = Button(window,text="Create new\nReservations",cursor="hand2",bd=0,width=10,height=3,font=("microsoft yahei light",16),command=lambda:create_in())
# option4 = Button(window,text="Update user's\nReservations",cursor="hand2",bd=0,width=10,height=3,font=("microsoft yahei light",16))
option5 = Button(window,text="Delete\nReservations",cursor="hand2",bd=0,width=10,height=3,font=("microsoft yahei light",16),command=lambda:delete_in())
option6 = Button(window,text="Exit",fg="red",cursor="hand2",bd=0,width=10,height=3,font=("microsoft yahei light",16),command=lambda:exit())

welcome_login = Label(window,text="Please Login to Continue :-",font=("microsoft yahei light",30))
login_name_label = Label(window,text="Password :",font=("microsoft yahei light",16))
login_input = Entry(window,fg="grey",show="☻",bd=1,bg=BACKGROUND_COLOR,width=30,font=("microsoft yahei light",25))
login_submit = Button(window,text="submit →",font=("microsoft yahei light",16,"bold"),bg="blue",fg="white",command=check_login)
login_error = Label(window,text="The password you entered is incorrect !!",fg="red",font=("microsoft yahei light",13))

login()

view_back = Button(window,text="←",bd=0,font=("microsoft yahei light",30),cursor="hand2",command=lambda:view_out())
view_label = Label(window,text=" ",height=3,width=100)
view_text = Label(window,text="All Seat Reservation",font=("microsoft yahei light",24))
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
canvas =Canvas(window, bg="white")
scrollbar = Scrollbar(window, orient="vertical",bg="white", command=canvas.yview)
scrollable_frame = Frame(canvas,bg="white")
scrollable_frame.bind("<Configure>", on_frame_configure)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

user_back = Button(window,text="←",bd=0,font=("microsoft yahei light",30),cursor="hand2",command=lambda:user_out())
user_title = Label(window,text="User Booking's",font=("microsoft yahei light",24))
user_name = Label(window,text="Name of person :",font=("microsoft yahei light",18))
user_input = Entry(window,width=50,font=("microsoft yahei light",18))
user_submit = Button(window,text="Find !",font=("microsoft yahei light",15,"bold"),bd=0,cursor="hand2",bg="blue",fg="white",command=lambda:found())
user_not = Label(window,fg="red",text="User not found !",font=("microsoft yahei light",18))
user_found = Label(window,text="User Found :",fg="green",font=("microsoft yahei light",18))
user_found_name = Label(window,text="Name : User ka naam hai",font=("microsoft yahei light",15))
user_found_seat = Label(window,text="Seat no. :  34b",font=("microsoft yahei light",15))
user_found_age = Label(window,text="Age : 34",font=("microsoft yahei light",15))
user_found_gender = Label(window,text="Gender : Male",font=("microsoft yahei light",15))
user_found_fare = Label(window,text="Fare : $500",font=("microsoft yahei light",15))


create_back = Button(window,text="←",bd=0,font=("microsoft yahei light",30),cursor="hand2",command=lambda:create_out())
create_title = Label(window,text="New Reservation!",font=("microsoft yahei light",24))
create_name = Label(window,text="Name : ",font=("microsoft yahei light",16))
create_name_input = Entry(window,font=("microsoft yahei light",18))
create_age = Label(window,text="Age : ",font=("microsoft yahei light",16))
create_age_input = Entry(window,font=("microsoft yahei light",18))
create_gender = Label(window,text="Gender : ",font=("microsoft yahei light",16))
create_gender_input = Entry(window,font=("microsoft yahei light",18))
create_choose_seat = Button(window,text="Choose a seat !",font=("microsoft yahei light",18),cursor="hand2",command=lambda:choose_seat_in())

delete_back = Button(window,text="←",bd=0,font=("microsoft yahei light",30),cursor="hand2",command=lambda:delete_out())
delete_title = Label(window,text="Delete Booking's",font=("microsoft yahei light",24))
delete_name = Label(window,text="Name of person :",font=("microsoft yahei light",18))
delete_input = Entry(window,width=50,font=("microsoft yahei light",18))
delete_not = Label(window,fg="red",text="User not found !",font=("microsoft yahei light",18))
delete_found = Label(window,text="Successfully Deleted !!!",fg="green",font=("microsoft yahei light",18))
delete_submit = Button(window,text="Submit",fg="white",bg="darkblue",font=("microsoft yahei light",18,"bold"),bd=0,command=lambda:delete_check())

choose_back = Button(window,text="←",bd=0,font=("microsoft yahei light",30),cursor="hand2",command=lambda:choose_seat_out())
choose_label = Label(window,text=" ",height=3,width=100)
choose_text = Label(window,text="All Seat Reservation",font=("microsoft yahei light",24))
def on_frame_configure_choose(event):
    choose_canvas.configure(scrollregion=choose_canvas.bbox("all"))
choose_canvas =Canvas(window, bg="white")
choose_scrollbar = Scrollbar(window, orient="vertical",bg="white", command=choose_canvas.yview)
choose_scrollable_frame = Frame(choose_canvas,bg="white")
choose_scrollable_frame.bind("<Configure>", on_frame_configure_choose)
choose_canvas.create_window((0, 0), window=choose_scrollable_frame, anchor="nw")
choose_canvas.configure(yscrollcommand=choose_scrollbar.set)
choose_seat = Label(window,text="seat :",fg="red",bd=0,font=("microsoft yahei light",15))
choose_submit = Button(window,text="Book !",cursor="hand2",fg="darkblue",bd=0,font=("microsoft yahei light",15,"bold"),command=lambda:seat_book())


window.mainloop()