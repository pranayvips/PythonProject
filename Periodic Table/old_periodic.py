from functools import partial
from tkinter import *
from csv import reader

phd=__file__.replace('periodic.py','')
root=Tk()
root.title('heelo')
root.geometry('1360x730')
root.resizable(0,0)
root.config(bg='white')
bt=PhotoImage(file='a.png')
root.iconphoto(False,bt)
Button_list=[]
image_list=[]
def search(any):
    eka.delete(0,END)
    if any.isdigit():
        f=open('q.csv')
        a=reader(f)
        k=[]
        f=0
        for i in a :
            if i[0]==str(any):
                k=i[0]
                f=1
                break
        if f:
            call(k)
    else:
        f=open('q.csv')
        a=reader(f)
        k=[]
        f=0
        for i in a :
            if any.lower() in i[2].lower():
                k=i[0]
                f=1
                break
        if f:
            call(int(k))
    
    if not f:
        Label(root,text="not found for the search %s..."%any,bg='white',fg='red',font=('arial',10)).place(x=320,y=140)

def call(num):
    f=open('q.csv')
    a=reader(f)
    k=[]
    for i in a :
        if i[0]==str(num):
            k=i
            break
    m=Toplevel()
    m.attributes('-topmost',1)
    m.geometry('600x650')
    m.config(bg='white')
    Label(m,text=k[2],bg='white',fg='black',font=('georgia',25)).place(relx=0.415,y=0)
    p=['AtomicNumber', 'Symbol', 'Name', 'AtomicMass', 'CPKHexColor', 'ElectronConfiguration', 'Electronegativity', 'AtomicRadius', 'IonizationEnergy', 'ElectronAffinity', 'OxidationStates', 'StandardState', 'MeltingPoint', 'BoilingPoint', 'Density', 'GroupBlock', 'YearDiscovered']
    o=80
    for i in range(len(p)):
        a=Text(m,height=1,bd=0,bg='white',fg='grey',font=('georgia',14))
        a.place(x=0,y=o)
        a.insert(INSERT,p[i])
        a.config(state='disabled')
        Label(m,text=":",bg='white',font=('georgia',14)).place(x=230,y=o)
        a1=Text(m,height=1,bd=0,bg='white',fg='blue',font=('georgia',14))
        a1.place(x=280,y=o)
        a1.insert(INSERT,k[i])
        a1.config(state='disabled')
        Label(m,text="_"*700,bg='white',font=('georgia',1)).place(x=0,y=o+25)
        
        o+=30
    Button(m,text="OKAY",bg='white',fg='red',bd=0,activeforeground='light blue',font=('georgia',15),command=lambda:m.destroy()).place(x=470,y=o+20)
    import webbrowser
    Button(m,text="wanna search more about it?",bg='white',fg='green',bd=0,activeforeground='light blue',font=('georgia',10),command=lambda:webbrowser.open("https://pubchem.ncbi.nlm.nih.gov/element/"+str(num))).place(x=0,y=o+25)
    m.mainloop()
    

for i in range(1,119):
    image_list.append(PhotoImage(file='ha/'+str(i)+'.png'))
    Button_list.append(Button(root,image=image_list[i-1],bg='white',bd=0,highlightbackground='white',cursor='hand2',command=partial(call,i)))

Button_list[0].place(x=0,y=25                                    )
Button_list[1].place(x=75*17-3,y=25                                    )
Button_list[2].place(x=0,y=100                                    )
Button_list[3].place(x=75,y=100                                    )
Button_list[4].place(x=75*12-3,y=100                                    )
Button_list[5].place(x=75*13-3,y=100                                    )
Button_list[6].place(x=75*14-3,y=100                                    )
Button_list[7].place(x=75*15-3,y=100                                    )
Button_list[8].place(x=75*16-3,y=100                                    )
Button_list[9].place(x=75*17-3,y=100                                    )
Button_list[10].place(x=0,y=174                                    )
Button_list[11].place(x=75*1,y=174                                    )
Button_list[12].place(x=75*12-3,y=174                                    )
Button_list[13].place(x=75*13-3,y=174                                    )
Button_list[14].place(x=75*14-3,y=174                                    )
Button_list[15].place(x=75*15-3,y=174                                    )
Button_list[16].place(x=75*16-3,y=174                                    )
Button_list[17].place(x=75*17-3,y=174                                    )
Button_list[18].place(x=0,y=249                                    )            
Button_list[19].place(x=75*1-3,y=249                                    )      
Button_list[20].place(x=75*2-3,y=249                                    )      
Button_list[21].place(x=75*3-3,y=249                                    )      
Button_list[22].place(x=75*4-3,y=249                                    )      
Button_list[23].place(x=75*5-3,y=249                                    )      
Button_list[24].place(x=75*6-3,y=249                                    )      
Button_list[25].place(x=75*7-3,y=249                                    )      
Button_list[26].place(x=75*8-3,y=249                                    )      
Button_list[27].place(x=75*9-3,y=249                                    )      
Button_list[28].place(x=75*10-3,y=249                                    )
Button_list[29].place(x=75*11-3,y=249                                    )
Button_list[30].place(x=75*12-3,y=249                                    )
Button_list[31].place(x=75*13-3,y=249                                    )
Button_list[32].place(x=75*14-3,y=249                                    )
Button_list[33].place(x=75*15-3,y=249                                    )
Button_list[34].place(x=75*16-3,y=249                                    )
Button_list[35].place(x=75*17-3,y=249                                    )
Button_list[36].place(x=0,y=324                                    )         
Button_list[37].place(x=75*1-3,y=324                                    )                    
Button_list[38].place(x=75*2-3,y=324                                    )                                  
Button_list[39].place(x=75*3-3,y=324                                    )                  
Button_list[40].place(x=75*4-3,y=324                                    )                       
Button_list[41].place(x=75*5-3,y=324                                    )               
Button_list[42].place(x=75*6-3,y=324                                    )                
Button_list[43].place(x=75*7-3,y=324                                    )                              
Button_list[44].place(x=75*8-3,y=324                                    )                     
Button_list[45].place(x=75*9-3,y=324                                    )                      
Button_list[46].place(x=75*10-3,y=324                                    )              
Button_list[47].place(x=75*11-3,y=324                                    )               
Button_list[48].place(x=75*12-3,y=324                                    )        
Button_list[49].place(x=75*13-3,y=324                                    )
Button_list[50].place(x=75*14-3,y=324                                    )
Button_list[51].place(x=75*15-3,y=324                                    )
Button_list[52].place(x=75*16-3,y=324                                    )
Button_list[53].place(x=75*17-3,y=324                                    )
Button_list[54].place(x=0,y=324+75                                    )      
Button_list[55].place(x=75*1-3,y=324+75                                    ) 

Button_list[56].place(x=75* 2  -29,y=576                                    )
Button_list[57].place(x=75*3-29,y=576                                    )
Button_list[58].place(x=75*4-29,y=576                                    )
Button_list[59].place(x=75*5-29,y=576                                    )
Button_list[60].place(x=75*6-29,y=576                                    )
Button_list[61].place(x=75*7-29,y=576                                    )
Button_list[62].place(x=75*8-29,y=576                                    )
Button_list[63].place(x=75*9-29,y=576                                    )
Button_list[64].place(x=75*10-29,y=576                                    )
Button_list[65].place(x=75*11-29,y=576                                    )
Button_list[66].place(x=75*12-29,y=576                                    )
Button_list[67].place(x=75* 13-29,y=576                                    )
Button_list[68].place(x=75* 14-29,y=576                                    )
Button_list[69].place(x=75* 15-29,y=576                                    )
Button_list[70].place(x=75* 16-29,y=576                                    )
Button_list[71].place(x=75*3-3,y=324+75                                    )
Button_list[72].place(x=75*4-3,y=324+75                                    )             
Button_list[73].place(x=75*5-3,y=324+75                                    )             
Button_list[74].place(x=75*6-3,y=324+75                                    )             
Button_list[75].place(x=75*7-3,y=324+75                                    )             
Button_list[76].place(x=75*8-3,y=324+75                                    )             
Button_list[77].place(x=75*9-3,y=324+75                                    )             
Button_list[78].place(x=75*10-3,y=324+75                                    )            
Button_list[79].place(x=75*11-3,y=324+75                                    )            
Button_list[80].place(x=75*12-3,y=324+75                                    )            
Button_list[81].place(x=75*13-3,y=324+75                                    )            
Button_list[82].place(x=75*14-3,y=324+75                                    )            
Button_list[83].place(x=75*15-3,y=324+75                                    )            
Button_list[84].place(x=75*16-3,y=324+75                                    )            
Button_list[85].place(x=75*17-3,y=324+75                                    )            
Button_list[86].place(x=0,y=324+150                                    )      
Button_list[87].place(x=75*1-3,y=324+150                                    ) 
Button_list[88].place(x=75* 2  -29,y=576+75                                    )
Button_list[89].place(x=75*3-29,y=576+75                                    )
Button_list[90].place(x=75*4-29,y=576+75                                    )
Button_list[91].place(x=75*5-29,y=576+75                                    )
Button_list[92].place(x=75*6-29,y=576+75                                    )
Button_list[93].place(x=75*7-29,y=576+75                                    )
Button_list[94].place(x=75*8-29,y=576+75                                    )
Button_list[95].place(x=75*9-29,y=576+75                                    )
Button_list[96].place(x=75*10-29,y=576+75                                    )
Button_list[97].place(x=75*11-29,y=576+75                                    )
Button_list[98].place(x=75*12-29,y=576+75                                    )
Button_list[99].place(x=75* 13-29,y=576+75                                    )
Button_list[100].place(x=75* 14-29,y=576+75                                    )
Button_list[101].place(x=75* 15-29,y=576+75                                    )
Button_list[102].place(x=75* 16-29,y=576+75                                    )
Button_list[103].place(x=75*3-3,y=324+150                                    )
Button_list[104].place(x=75*4-3,y=324+75+75                                    )
Button_list[105].place(x=75*5-3,y=324+75+75                                    ) 
Button_list[106].place(x=75*6-3,y=324+75+75                                    ) 
Button_list[107].place(x=75*7-3,y=324+75+75                                    ) 
Button_list[108].place(x=75*8-3,y=324+75+75                                    ) 
Button_list[109].place(x=75*9-3,y=324+75+75                                    ) 
Button_list[110].place(x=75*10-3,y=324+75+75                                    ) 
Button_list[111].place(x=75*11-3,y=324+75+75                                    )
Button_list[112].place(x=75*12-3,y=324+75+75                                    )
Button_list[113].place(x=75*13-3,y=324+75+75                                    )
Button_list[114].place(x=75*14-3,y=324+75+75                                    )
Button_list[115].place(x=75*15-3,y=324+75+75                                    )
Button_list[116].place(x=75*16-3,y=324+75+75                                    )
Button_list[117].place(x=75*17-3,y=324+75+75                                    )

eka=Entry(root,fg='purple',bg='white',font=('arial',20))
eka.place(x=300,y=60)
Button(root,text='Z/A',bg='white',highlightbackground='white',bd=0,font=('georgia',20),command=lambda:search(eka.get())).place(x=620,y=60)


Label(root,text='*',bg='white',font=('arial',15)).place(x=180,y=410)
Label(root,text='*',bg='white',font=('arial',15)).place(x=100,y=590)
Label(root,text='**',bg='white',font=('arial',15)).place(x=180,y=490)
Label(root,text='**',bg='white',font=('arial',15)).place(x=100,y=650)

def jal():
    a=Toplevel()
    a.geometry('400x400')
    a.title('About me')
    a.config(bg='white')
    Label(a,text='Hello there I am pranay\ndeveloper of this program\n feel free to use this',font=('georgia',20),bg='white',fg='blue').place(x=0,y=0)
    a.mainloop()

Button(root,text="i",font=('georgia',20),bg='white',fg='blue',command=jal).place(x=1300,y=680)
root.mainloop()