import pygame
from tkinter import *
from csv import reader
from tkinter import filedialog
from PIL import Image, ImageTk
from webbrowser import open as webopen
pygame.init()
screen = pygame.display.set_mode((1360, 730))
clock = pygame.time.Clock()
pygame.display.set_caption("Pranay's Perodic")
element_list = []
for i in range(1, 119):
    element_list.append(pygame.image.load(fr'ha\{i}.png'))
RUN = 1

positions = [(75, 97), (1347, 97), (75, 172), (150, 172), (972, 172), (1047, 172), (1122, 172), (1197, 172), (1272, 172), (1347, 172), (75, 246), (150, 246), (972, 246), (1047, 246), (1122, 246), (1197, 246), (1272, 246), (1347, 246), (75, 321), (147, 321), (222, 321), (297, 321), (372, 321), (447, 321), (522, 321), (597, 321), (672, 321), (747, 321), (822, 321), (897, 321), (972, 321), (1047, 321), (1122, 321), (1197, 321), (1272, 321), (1347, 321), (75, 396), (147, 396), (222, 396), (297, 396), (372, 396), (447, 396), (522, 396), (597, 396), (672, 396), (747, 396), (822, 396), (897, 396), (972, 396), (1047, 396), (1122, 396), (1197, 396), (1272, 396), (1347, 396), (75, 471), (147, 471), (196, 648), (271, 648), (346, 648),
             (421, 648), (496, 648), (571, 648), (646, 648), (721, 648), (796, 648), (871, 648), (946, 648), (1021, 648), (1096, 648), (1171, 648), (1246, 648), (297, 471), (372, 471), (447, 471), (522, 471), (597, 471), (672, 471), (747, 471), (822, 471), (897, 471), (972, 471), (1047, 471), (1122, 471), (1197, 471), (1272, 471), (1347, 471), (75, 546), (147, 546), (196, 723), (271, 723), (346, 723), (421, 723), (496, 723), (571, 723), (646, 723), (721, 723), (796, 723), (871, 723), (946, 723), (1021, 723), (1096, 723), (1171, 723), (1246, 723), (297, 546), (372, 546), (447, 546), (522, 546), (597, 546), (672, 546), (747, 546), (822, 546), (897, 546), (972, 546), (1047, 546), (1122, 546), (1197, 546), (1272, 546), (1347, 546)]
element_list_rect = []
for i in range(len(element_list)):
    element_list_rect.append(
        element_list[i].get_rect(bottomright=(positions[i])))
call_wait = 1


def call(num):
    pygame.display.set_mode((800, 600), flags=pygame.HIDDEN)
    f = open('q.csv')
    a = reader(f)
    k = []
    for i in a:
        if i[0] == str(num):
            k = i
            break
    m = Tk()
    m.attributes('-topmost', 1)
    m.geometry('1060x500')
    m.config(bg='white')
    try:
        img = (Image.open(rf'img\{num}.jpg'))
        resized_image = img.resize((75, 72), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)
    except:
        new_image = PhotoImage(file=r'img\no.png')
    Label(m, image=new_image).place(x=0, y=0)
    Label(m, text=k[2], bg='white', fg='black', font=(
        'microsoft jhenghei UI', 30, 'bold')).place(relx=0.1, y=10)
    p = ['Atomic Number', 'Symbol', 'Name', 'Atomic Mass', 'CPKHex Color', 'Electron Configuration', 'Electronegativity', 'Atomic Radius', 'Ionization Energy',
         'Electron Affinity', 'Oxidation States', 'Standard State', 'Melting Point', 'Boiling Point', 'Density', 'Group Block', 'Year Discovered']
    o = 140
    a1 = Label(m, height=1, text=k[0], bd=0, bg='white',
               fg='dark green', font=('georgia', 14))
    a1.place(x=350, y=0)
    a = Label(m, height=1, bd=0, bg='white', fg='purple',
              text='{'+p[0]+'}', font=('microsoft jhenghei UI Light', 14))
    a.place(x=400, y=0)
    a1 = Label(m, height=1, text=k[1], bd=0, bg='white',
               fg='dark green', font=('georgia', 14))
    a1.place(x=350, y=50)
    a = Label(m, height=1, bd=0, bg='white', fg='purple',
              text='{'+p[1]+'}', font=('microsoft jhenghei UI Light', 14))
    a.place(x=400, y=50)
    for i in range(3, len(p)):
        if i == 10:
            o = 140
        if i < 10:
            a = Text(m, height=1, bd=0, bg='white',
                     fg='black', font=('georgia', 14, 'bold'))
            a.place(x=0, y=o)
            a.insert(INSERT, p[i])
            a.config(state='disabled')
            Label(m, text=":", bg='white', font=(
                'georgia', 14)).place(x=230, y=o)
            if len(k[i]) < 10:
                a1 = Text(m, height=1, bd=0, bg='white', fg='dark blue',
                          font=('microsoft jhenghei UI', 14, 'bold'))
            else:
                a1 = Text(m, height=1, bd=0, bg='white', fg='dark blue',
                          font=('microsoft jhenghei UI', 11, 'bold'))
            a1.place(x=280, y=o)
            a1.insert(INSERT, k[i])
            a1.config(state='disabled')
        else:
            a = Text(m, height=1, bd=0, bg='white',
                     fg='black', font=('georgia', 14, 'bold'))
            a.place(x=100+450, y=o)
            a.insert(INSERT, p[i])
            a.config(state='disabled')
            Label(m, text=":", bg='white', font=(
                'georgia', 14)).place(x=100+680, y=o)
            a1 = Text(m, height=1, bd=0, bg='white', fg='dark blue',
                      font=('microsoft jhenghei UI', 14, 'bold'))
            a1.place(x=100+730, y=o)
            a1.insert(INSERT, k[i])
            a1.config(state='disabled')
        o += 40

    def update_image():
        filename = filedialog.askopenfilename(initialdir="/", title="Select An Image", filetypes=(
            ("jpg files", "*.jpg"), ("jepg files", "*.jpeg*"), ("png files", "*.png"), ("all files", "*")))
        if filename:
            ho = open(filename, 'rb').read()
            with open(rf'img\{num}.jpg', 'wb') as f:
                f.write(ho)
            f.close()
    Button(m, text="OKAY", bg='light blue', fg='red', bd=0, activeforeground='light blue', font=(
        'georgia', 15, 'bold'), cursor='hand2', command=lambda: m.destroy()).place(x=450, y=o+30)
    Button(m, text="Update Image", bg='light green', fg='blue', bd=0, activeforeground='light blue',
           font=('georgia', 15, 'bold'), cursor='hand2', command=update_image).place(x=850, y=o+30)
    Button(m, text="wanna search more about it?", bg='yellow', fg='green', bd=0, activeforeground='light blue', font=(
        'georgia', 10), command=lambda: webopen("https://pubchem.ncbi.nlm.nih.gov/element/"+str(num)), cursor='hand2').place(x=50, y=o+35)
    m.mainloop()
    f.close()
    pygame.display.set_mode((1360, 730), pygame.SHOWN)


real_image = []
for i in range(1, 119):
    try:
        real_image.append(pygame.transform.scale(
            pygame.image.load(rf'img\{i}.jpg'), (75, 72)))
    except:
        real_image.append(pygame.image.load(r'img\no.jpg'))

while RUN:
    for evnet in pygame.event.get():
        if evnet.type == pygame.QUIT:
            RUN = 0
        if evnet.type == pygame.MOUSEBUTTONDOWN:
            for i in range(118):
                if element_list_rect[i].collidepoint(pygame.mouse.get_pos()):
                    if call_wait >= 1:
                        call(i+1)
                        call_wait = 0

    screen.fill((255, 255, 255))
    for i in range(118):
        if element_list_rect[i].collidepoint(pygame.mouse.get_pos()):
            screen.blit(real_image[i], element_list_rect[i])
        else:
            screen.blit(element_list[i], element_list_rect[i])

    if call_wait < 1:

        call_wait += 1/10

    pygame.display.update()
    clock.tick(20)
pygame.quit()