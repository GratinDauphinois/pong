from tkinter import *

#oui
x0=10
y0=200
x1=30
y1=400
bx0 = 390
by0 = 290
bx1 = 410
by1 = 310
largeur = 800
hauteur = 600
dx = 0
dy = 0

#Création fenetre canevas
fenetre = Tk()
Canevas = Canvas(fenetre, width = largeur, height = hauteur, bg='black')
Canevas.pack()

#création raquettes
raquettep1 = Canevas.create_rectangle(x0,y0,x1,y1, fill="white")
raquettep2 = Canevas.create_rectangle(largeur - x1, y0, largeur - x0, y1, fill="white")

#création balle
balle = Canevas.create_oval(bx0,by0,bx1,by1, fill="white")
#mouvement raquettes
def hautp1(event):
    Canevas.move(raquettep2,0,-10)
def basp1(event):
    Canevas.move(raquettep2,0,10)
def  hautp2(event):
    Canevas.move(raquettep1,0,-10)
def basp2(event):
    Canevas.move(raquettep1,0,10)

#On associe les fleches du clavier aux fonctions droite() et gauche():
Canevas.bind_all('<Up>',  hautp1)
Canevas.bind_all('<Down>', basp1)
Canevas.bind_all('<z>',  hautp2)
Canevas.bind_all('<s>', basp2)


#Boutton quitter
quitter=Button(fenetre, text="Fermer", command=fenetre.quit)
quitter.pack()



#affichage fenetre
fenetre.mainloop()