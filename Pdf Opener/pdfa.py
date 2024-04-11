class Pdf_Opner:
    def __init__(self) :
        from functools import partial
        from tkinter import Button,Label,Text,Entry,Scrollbar,PhotoImage,Tk,Toplevel,Menubutton,Menu,Canvas,Frame,VERTICAL,Y,END,INSERT,TOP,LEFT,RIGHT,BOTH
        from gc import collect
        from PyPDF2 import PdfReader,PdfFileWriter,PdfFileMerger
        from tkinter import filedialog,messagebox
        from threading import Thread
        from os import rename,makedirs,walk,chdir
        from shutil import rmtree
        from sys import argv,exit
        PYTHON_FILE_LOCATION=__file__.replace('pdfa.py','')
        chdir(PYTHON_FILE_LOCATION)
        collect()

        try:
            rmtree('image')
            makedirs('image')
        except:
            pass
        def page_text_extractor(event=None):
            ro=Tk()
            ro.withdraw()
            ro.attributes('-topmost',True)
            single_page_or_double_page=messagebox.askyesno(title='Select',message='Do you want full pdf\'s text')

            file_loca=filedialog.askdirectory()
            a1=filename.get()
            acd=file_loca+'/'+a1
            if file_loca:
                #For single page
                if not single_page_or_double_page:
                    d=page_number.get('1.0',END)
                    d=eval(d)
                    d-=1
                    first_page = ALL_TEXT[d]
                    with open(acd+f'page-{d}.txt','w',encoding='utf-8')as f:
                        f.write(first_page)
                else:
                    re=''
                    for i in ALL_TEXT:
                        re+=i
                    with open(acd+'.txt','w',encoding='utf-8')as f:
                        f.write(re)
            ro.destroy()

        def create_pdf(event=None):
            asd=Toplevel()
            asd.withdraw()
            asd.attributes('-topmost',True)
            pdf_writer = PdfFileWriter()
            pdf_writer.addBlankPage(width=1080, height=720)
            file_loca=filedialog.askdirectory()
            if file_loca:
                with open(file_loca+r"\blank.pdf",mode="wb") as output_file:
                    pdf_writer.write(output_file)
            asd.destroy()

        def merge_pdf(event=None):
            asd=Toplevel()
            asd.withdraw()
            asd.attributes('-topmost',True)
            pdf1=filedialog.askopenfilename(title='Open a file',filetypes=(('Pdf files', '*.pdf'),('All files', '*.*')))
            pdf2=filedialog.askopenfilename(title='Open a file',filetypes=(('Pdf files', '*.pdf'),('All files', '*.*')))
            if pdf1 and pdf2:
                pdf_merger = PdfFileMerger()
                pdf_merger.append(str(pdf1))
                pdf_merger.merge(1, str(pdf2))
                file_loca=filedialog.askdirectory()
                if file_loca:
                    with open(file_loca+r"\final_pdf_after_merging.pdf",mode="wb") as output_file:
                        pdf_merger.write(output_file)
            asd.destroy()

        def rotataing_page(pdf,right_or_left_r_l,event=None): 
            page_no_to_rotate=page_number.get('1.0',END)
            page_no_to_rotate=eval(page_no_to_rotate)
            page_no_to_rotate-=1
            pdf_reader = PdfReader(str(pdf))
            pdf_writer = PdfFileWriter()
            for n in range(len(pdf_reader.pages)):
                page = pdf_reader.getPage(n)
                if n==(page_no_to_rotate):
                    if 'r' in right_or_left_r_l:
                        page.rotateClockwise(90)
                    else:
                        page.rotateClockwise(-90)
                pdf_writer.addPage(page)
                with open(pdf,mode="wb") as output_file:
                    pdf_writer.write(output_file)

            global Kaka
            import fitz
            doc = fitz.open(PDF_FILE_MAIN_NAME[-1])
            zoom = 2 # to increase the resolution
            mat = fitz.Matrix(zoom, zoom)
            image_folder = r"image\\"
            page = doc.loadPage(page_no_to_rotate) #number of page
            pix = page.getPixmap(matrix = mat)
            output = image_folder + str(page_no_to_rotate) + '.png' # you could change image format accordingly
            pix.writePNG(output)
            Kaka=PhotoImage(file='image\\'+str(page_no_to_rotate)+'.png')
            main_images[page_no_to_rotate].config(image=Kaka)

        def encrypting_pdf(pdf,event=None):
            if not len(pass_pw):
                askingroot=Toplevel()
                askingroot.attributes('-topmost',True)
                askingroot.title('Enter The Password :')
                askingroot.config(bg='white')
                askingroot.geometry('300x200')
                Label(askingroot,text='Enter The Password      :',bg='white',font=('@microsoft yahei light' ,10)).place(x=0,y=0)
                p=Entry(askingroot,bg='white',font=('@microsoft yahei light' ,8))
                p.place(x=150,y=5)
                passw=[]
                def ha():
                    l=p.get()
                    l1=p1.get()
                    if l==l1 and len(l)>1:
                        passw.append(l)
                        pdf_reader = PdfReader(str(pdf))
                        pdf_writer = PdfFileWriter()
                        pdf_writer.appendPagesFromReader(pdf_reader)
                        pdf_writer.encrypt(user_pwd=passw[0],owner_pwd=passw[0])
                        with open(pdf,mode="wb") as output_file:
                            pdf_writer.write(output_file)
                        messagebox.askokcancel(title='Success',message='Your File Has Been Encrypted')
                        askingroot.destroy()
                    else:
                        Label(askingroot,text='Password doesnt matched',fg='red',bg='white',font=('@microsoft yahei light' ,9)).place(x=40,y=120)
                Label(askingroot,text='Confirm The Password :',bg='white',font=('@microsoft yahei light' ,10)).place(x=0,y=70)
                p1=Entry(askingroot,bg='white',font=('@microsoft yahei light' ,8))
                p1.place(x=150,y=70)
                Button(askingroot,text='Okay',bd=0,bg='white',font=('@microsoft yahei light' ,10),command=ha).place(x=130,y=150)
                askingroot.mainloop()

        def decrypt_pdf_file(pdf,event=None):
            if len(pass_pw):
                ro=Tk()
                ro.withdraw()
                ro.attributes('-topmost',True)
                out = PdfFileWriter()
                file = PdfReader(pdf)
                file.decrypt(pass_pw[0])
                num = file.numPages
                for idx in range(num):
                    page = file.getPage(idx)
                    out.addPage(page)
                with open(pdf, "wb") as f:
                    out.write(f)
                messagebox.askokcancel(title='Success',message='Your File Has Been Decrypted:')
                ro.destroy()

        def copying_image(event=None):
            asd=Toplevel()
            asd.withdraw()
            asd.attributes('-topmost',True)
            file_loca=filedialog.askdirectory()
            if file_loca:
                a1=filename.get()
                acd=file_loca+'/'+a1
                try:
                    makedirs(acd)
                except:
                    rmtree(acd)
                    makedirs(acd)

                ep=[]
                for a,b,c in walk(PYTHON_FILE_LOCATION+'/image'):
                    if a==PYTHON_FILE_LOCATION+'/image':
                        ep=c
                for i in ep:
                    f=open(PYTHON_FILE_LOCATION+'/image'+'/'+i,"rb")
                    d=f.read()
                    f.close()
                    with open(acd+'/'+i,'wb') as f:
                        f.write(d)
                    f.close()
            asd.destroy()
        def ask_pw():
            ro=Tk()
            ro.withdraw()
            oo=Toplevel()
            oo.title('Enter Pssword')
            oo.attributes('-topmost',True)
            oo.geometry('200x150')
            oo.config(bg='white')
            Label(oo,text='Enter the password',font=('arial 15'),bg='white').place(x=0,y=0)
            ak=Entry(oo,font=('arial 15'),bg='white')
            ak.place(x=0,y=50)  
            def sub(event=None):
                cd=ak.get()
                pdf_ka_file_reader[0].decrypt(cd)
                try:
                    pdf_ka_file_reader[0].getNumPages()
                    pass_pw.append(cd)
                    oo.destroy()
                    ro.destroy()

                except:
                    S=messagebox.askokcancel(title='Wrong Password',message='ENTERED PASSWORD IS WRONG\nPLEASE TRY AGAIN.')
                    if not S:
                        exit()

            def closer(event=None):
                exit()

            oo.protocol("WM_DELETE_WINDOW",closer)

            Button(oo,text='Submit',font=('arial 15'),bg='white',command=sub).place(x=50,y=100)
            oo.mainloop()

        def opens(event=None):
            asd=Toplevel()
            asd.withdraw()
            asd.attributes('-topmost',True)
            pdf1=filedialog.askopenfilename(title='Open a file',filetypes=(('Pdf files', '*.pdf'),('All files', '*.*')))
            if pdf1 and '.pdf' in pdf1:
                for i in main_images:
                    i.forget()
                main_images.clear()
                image_st.clear()
                length.clear()
                PDF_FILE_MAIN_NAME[-1]=pdf1

                if '\\' in PDF_FILE_MAIN_NAME[-1]:
                    a=PDF_FILE_MAIN_NAME[-1].split('\\')
                elif '/' in PDF_FILE_MAIN_NAME[-1]:
                    a=PDF_FILE_MAIN_NAME[-1].split('/')
                PDF_FILE_LOCATION_WITHOUT_NAME[0]=''
                for tbs in range(0,len(a)-1):
                    PDF_FILE_LOCATION_WITHOUT_NAME[0]+=a[tbs]+'\\'
                FILE_NAME[0]=a[-1]
                FILE_NAME[0]=str(FILE_NAME[0])
                pdf_ka_file_reader[0] = PdfReader(PDF_FILE_MAIN_NAME[-1])
                pass_pw.clear()
                if pdf_ka_file_reader[0].is_encrypted:
                    ask_pw()


                Converting_pdf_to_image_thread=Thread(target=converting_to_img)
                Converting_pdf_to_image_thread.start()

            asd.destroy()

        # PDF_FILE_MAIN_NAME=argv
        PDF_FILE_MAIN_NAME=["",r"C:\Users\prana\Desktop\Black White Minimalist CV Resume.pdf"]

        if '.pdf' not in PDF_FILE_MAIN_NAME[-1]:
            exit()
        if '\\' in PDF_FILE_MAIN_NAME[-1]:
            a=PDF_FILE_MAIN_NAME[-1].split('\\')
        elif '/' in PDF_FILE_MAIN_NAME[-1]:
            a=PDF_FILE_MAIN_NAME[-1].split('/')
        PDF_FILE_LOCATION_WITHOUT_NAME=['']
        for tbs in range(0,len(a)-1):
            PDF_FILE_LOCATION_WITHOUT_NAME[0]+=a[tbs]+'\\'
        FILE_NAME=['a']
        FILE_NAME[0]=a[-1]
        FILE_NAME[0]=str(FILE_NAME[0])
        pdf_ka_file_reader=['ala']
        pdf_ka_file_reader[0] = PdfReader(PDF_FILE_MAIN_NAME[-1])
        pass_pw=[]
        if pdf_ka_file_reader[0].is_encrypted:
            ask_pw()


        root=Tk()
        root.title('PDFs')
        root.geometry('500x300')
        root.config(bg='white')
        def renames(event=None):
            p=filename.get()
            rename(PDF_FILE_MAIN_NAME[-1],PDF_FILE_LOCATION_WITHOUT_NAME[0]+p+'.pdf')
            PDF_FILE_MAIN_NAME[-1]=PDF_FILE_LOCATION_WITHOUT_NAME[0]+p+'.pdf'
            filename.delete(0,END)
            filename.insert(INSERT,p)
        tppp=PhotoImage(file='pdf.png')
        root.iconphoto(1,tppp)
        NO_OF_PAGE =len(pdf_ka_file_reader[0].pages)
        all_text=''
        ALL_TEXT=[]
        for page in pdf_ka_file_reader[0].pages:
            all_text+=page.extract_text()
            ALL_TEXT.append(page.extract_text())
        total_text=len(all_text.split(' '))
        main_images=[]
        image_st=[]
        length=[]

        def converting_to_img():
            import fitz
            doc = fitz.open(PDF_FILE_MAIN_NAME[-1])
            zoom = 2
            if len(pass_pw):
                doc.authenticate(pass_pw[0])

            mat = fitz.Matrix(zoom, zoom)
            noOfPages = doc.pageCount
            image_folder = r"image\\"
            c=0
            for pageNo in range(noOfPages):
                page = doc.loadPage(pageNo) #number of page
                pix = page.getPixmap(matrix = mat)
                output = image_folder + str(pageNo) + '.png' # you could change image format accordingly
                pix.writePNG(output)
                c+=1
                image_st.append(PhotoImage(file=image_folder + str(pageNo) + '.png'))
                main_images.append(Label(second_frame,image=image_st[pageNo],bg='white'))
                main_images[pageNo].pack()
                Label(second_frame,image=end_page,bg='white').pack()
                length.append(image_st[pageNo].height())

        open_image=PhotoImage(file='open.png')
        lock_image=PhotoImage(file='lock.png')
        lock1_image=PhotoImage(file='lopen.png')
        create_image=PhotoImage(file='create.png')
        tools_image=PhotoImage(file='tools.png')
        images_image=PhotoImage(file='images.png')
        r_l_image=PhotoImage(file='r_l.png')
        r_r_image=PhotoImage(file='r_r.png')
        tick_image=PhotoImage(file='tick.png')
        end_page=PhotoImage(file='tick.png')
        shield_image=PhotoImage(file='shield.png')
        merge_image=PhotoImage(file='merge.png')
        text_image=PhotoImage(file='text.png')
        UPPER=Label(root,text='',width=350,bg='white',font=('arial 37'),height=1)
        UPPER.pack()
        Open=Button(root,image=open_image,text='Open',compound=TOP,bd=0,font=('@microsoft yahei light' ,12),cursor='hand2',bg='white',command=opens)
        Open.place(x=10,y=0)
        filename1=Label(root,text='Filename :\n\t\t\t\t\t      .pdf',font=('@microsoft yahei' ,12,'bold'),bg='white')
        filename1.place(x=502,y=-3)
        TExt_label=Button(root,image=text_image,text='Convert\nto text',compound=TOP,bd=0,font=('@microsoft yahei light' ,9),cursor='hand2',bg='white',command=page_text_extractor)
        TExt_label.place(x=90,y=0)
        filename=Entry(root,font=('@microsoft yahei light' ,12),width=26,bg='white')
        filename.place(x=695,y=20)
        tick=Button(root,image=tick_image,bd=0,font=('@microsoft yahei light' ,9),cursor='hand2',bg='white',command=renames)
        tick.place(x=980,y=20)
        filename.insert(INSERT,FILE_NAME[0].replace('.pdf',''))                 #todo LATER
        Images=Button(root,image=images_image,text='Convert to\nImages',compound=TOP,bd=0,font=('@microsoft yahei light' ,9),cursor='hand2',bg='white',command=copying_image)
        Images.place(x=160,y=0)
        rotate_left=Button(root,image=r_l_image,text='Rotate\nRight',compound=TOP,bd=0,font=('@microsoft yahei light' ,8),cursor='hand2',bg='white',command=partial(rotataing_page,PDF_FILE_MAIN_NAME[-1],'r'))
        rotate_left.place(x=380,y=0)
        rotate_right=Button(root,image=r_r_image,text='Rotate\nLeft',compound=TOP,bd=0,font=('@microsoft yahei light' ,8),cursor='hand2',bg='white',command=partial(rotataing_page,PDF_FILE_MAIN_NAME[-1],'l'))
        rotate_right.place(x=420,y=0)
        shield=Menubutton(root,image=shield_image,bg='white',text='Passwords',compound=TOP,font=('@microsoft yahei light' ,9))
        shieldmenu=Menu(shield,tearoff=False)
        shieldmenu.add_command(label="Encrypt This Pdf File",image=lock_image,compound=LEFT,font=('@microsoft yahei light' ,9),background='white',command=partial(encrypting_pdf,PDF_FILE_MAIN_NAME[-1]))
        shieldmenu.add_command(label="Decrypt This Pdf File",image=lock1_image,compound=LEFT,font=('@microsoft yahei light' ,9),background='white',command=partial(decrypt_pdf_file,PDF_FILE_MAIN_NAME[-1]))
        shield.config(menu=shieldmenu)
        shield.place(x=240,y=0)
        tools=Menubutton(root,image=tools_image,bg='white',text='Tools',compound=TOP,font=('@microsoft yahei light' ,9))
        toolsmenu=Menu(tools,tearoff=False)
        toolsmenu.add_command(label="Create a Pdf",image=create_image,compound=LEFT,font=('@microsoft yahei light' ,9),background='white',command=create_pdf)
        toolsmenu.add_command(label="Merge Pdf",image=merge_image,compound=LEFT,font=('@microsoft yahei light' ,9),background='white',command=merge_pdf)
        tools.config(menu=toolsmenu)
        tools.place(x=320,y=0)
        page_number=Text(root,font=('@microsoft yahei light' ,15),width=3,bd=0,bg='white',height=1)
        page_number.place(x=1183,y=10)
        page_number.insert('1.0','0')
        page_number.config(state='disabled')
        page_number1=Label(root,text='Current Page',font=('@microsoft yahei' ,10),bg='white')
        page_number1.place(x=1150,y=-8)
        rat=all_text.replace(' ','')
        rat=str(len(rat)/40)
        Stats=Label(root,text=f'Pages : {NO_OF_PAGE}   Words Present : {total_text}\nTime To write  : {rat[0:5]} minutes',font=('@microsoft yahei light', 10),bg='white',height=5)
        Stats.place(x=1350,y=-25)
        main_frame=Frame(root)
        main_frame.pack(fill=BOTH,expand=1)
        my_canvas=Canvas(main_frame)
        my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        my_scrollbar=Scrollbar(main_frame,orient=VERTICAL,cursor='hand2',command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        second_frame=Frame(my_canvas)
        my_canvas.create_window((0,0),window=second_frame,anchor='nw')
        Converting_pdf_to_image_thread=Thread(target=converting_to_img)
        Converting_pdf_to_image_thread.start()
        def a(event=None):
            try:
                p=-2*(event.delta//120)
                my_canvas.yview_scroll(p, "units")
                t=0
                af=abs(main_images[0].winfo_rooty())+450

                k=0
                for i in range(len(length)):
                    k+=length[i]
                    if af<k:
                        t=i
                        break
                t+=1
                page_number.config(state='normal')
                page_number.delete('1.0',END)
                page_number.insert('1.0',str(t))
                page_number.config(state='disabled')
            except:
                pass
        root.bind_all("<MouseWheel>",a)

        def closw(event=None):
            exit()
        def fullscreen(event=None):
            root.attributes('-fullscreen',True)
        def escap(event=None):
            root.attributes('-fullscreen',False)
        root.bind('<f>',fullscreen)
        root.bind('<Escape>',escap)
        root.protocol("WM_DELETE_WINDOW",closw)
        collect()
        root.mainloop()

Pdf_Opner()




