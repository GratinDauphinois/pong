from tkinter import *
import time
import random

tk = Tk()
tk.title("jeu")
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=800, height=600, bd=0, highlightthickness=0, bg="black")
canvas.pack()
tk.update()

x0=10
y0=200
x1=30
y1=400
largeur = 800
hauteur = 600
dx = 5
dy = 5

class Raquette :
    def __init__(self, canvas, couleur):
        self.canvas = canvas
        raquettep1 = canvas.create_rectangle(x0,y0,x1,y1, fill="white")

        raquettep2 = canvas.create_rectangle(largeur - x1, y0, largeur - x0, y1, fill="white")

    def hautp1(event):
        canvas.move(raquettep2,0,-20)
    def basp1(event):
        canvas.move(raquettep2,0,20)
    def  hautp2(event):
        canvas.move(raquettep1,0,-20)
    def basp2(event):
        canvas.move(raquettep1,0,20)

    canvas.bind_all('<Up>',  hautp1)
    canvas.bind_all('<Down>', basp1)
    canvas.bind_all('<z>',  hautp2)
    canvas.bind_all('<s>', basp2)

class Balle :
    def __init__(self, canvas, raquette, couleur):
        self.canvas = canvas
        self.raquette = raquette
        self.id = canvas.create_oval(10,10,25,25, fill="white")
        self.canvas.move(self.id, 245, 100)
        departs = [-3, -2, -1, 1, 2, 3]
        random.shuffle(departs)
        self.x = departs[0]
        self.y = -3
        self.hauteur_canevas = self.canvas.winfo_height()
        self.largeur_canevas = self.canvas.winfo_width()
    def heurter_raquette(self, pos):
        pos_raquette = self.canvas.coords(self.raquette.id)
        if pos[2] >= pos_raquette[0] and pos[0] <= pos_raquette[2]:
            if pos[3] >= pos_raquette[0] and pos[3] <= pos_raquette[3]:
                return True
        return False

    def dessiner(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if self.heurter_raquette(pos) == True:
            self.y = -3
        if pos[3] >= self.hauteur_canevas:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.largeur_canevas:
            self.x = -3

balle = Balle(canvas,Raquette, "white")

while True:
    balle.dessiner()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


quitter=Button(tk, text="Fermer", command=tk.quit)
quitter.pack()

tk.mainloop()