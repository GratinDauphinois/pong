from tkinter import *
from random import randrange

Player1 = 0
Player2 = 0

tk=Tk()
tk.title("Player1 : "+str(Player1)+"    |   "+"Player2 : "+str(Player2))

X = 800
Y = 600
speed = 5 


PLAY = False

class Raquette :
    def __init__(self,x,y,haut,bas):
        self.x = x
        self.y = y
        self.tx = 10
        self.ty = 50
        self.speed = 10
        self.haut = haut
        self.bas = bas
        self.ra = terrain.create_rectangle(self.x, self.y, self.x+self.tx, self.y+self.ty, fill = "white")
        tk.bind_all(self.haut,self.monter)
        tk.bind_all(self.bas,self.descendre)

    def monter(self,event):
        self.deplacer(-self.speed)
    def descendre(self,event):
        self.deplacer(self.speed)



    def deplacer (self,dy):
        if PLAY :
            self.y += dy
            if self.y < 0 :
                self.y = 0
            if self.y > Y-self.ty:
                self.y = Y-self.ty
            self.reset()
    def placer(self,x,y):
        self.x = x
        self.y = y
        terrain.coords(self.ra, self.x, self.y, self.x+self.tx, self.y+self.ty)


    def reset(self):
        terrain.coords(self.ra, self.x, self.y, self.x+self.tx, self.y+self.ty)


class Pong :
    def __init__(self):
        self.tx = 10
        self.ty = 10
        self.r1 = Raquette(30,Y/2-self.ty/2,"<z>","<s>")
        self.r2 = Raquette(X-30,Y/2-self.ty/2,"<Up>","<Down>")
        self.dummy = randrange(0, 100)

        self.x = X/2-self.tx/2
        self.y = Y/2-self.ty/2
        self.dx = 0
        if self.dummy < 50 :
            self.dx = -1
        else :
            self.dx=1

        self.dy = float(randrange(-100,100))/100

        self.balle = terrain.create_rectangle(self.x, self.y, self.x+self.tx, self.y+self.ty, fill = "white")
        self.deplacer()
        tk.bind_all("<Return>",self.pause)

    def pause(self, event):
        global PLAY
        if PLAY :
            PLAY = False
        else :
            PLAY = True


    def reset(self):
        terrain.coords(self.balle, self.x, self.y, self.x+self.tx, self.y+self.ty)

    def deplacer(self):
        global Player1, Player2, PLAY
        if PLAY :
            self.x += self.dx*speed
            self.y += self.dy*speed

            if self.y <= 0 or self.y >= Y-self.ty :
                self.dy =- self.dy
            if self.r1.y <= self.y + self.ty and self.r1.y + self.r1.ty >= self.y :
                if self.x <= self.r1. x+ self.r1.tx and not self.x + self.tx <= self.r1.x:
                    self.dx =- self.dx
                    self.dy = float(randrange(-100,100))/100

            if self.r2.y <= self.y + self.ty and self.r2.y + self.r2.ty >= self.y :
                if self.x + self.tx >= self.r2.x and not self.x >= self.r2.x + self.r2.tx :
                    self.dx =- self.dx
                    self.dy = float(randrange(-100,100))/100

            if self.x+self.tx<0 :
                self.x = X/2-self.tx/2
                self.y = Y/2-self.ty/2
                Player2 += 1
                self.dx =- self.dx
                self.dy = float(randrange(-100,100))/100
                self.r1.placer(30, Y/2-self.ty/2)
                self.r2.placer(X-30, Y/2-self.ty/2)
                PLAY = False


            if self.x + self.tx>X :
                self.x = X/2-self.tx/2
                self.y = Y/2-self.ty/2
                Player1 += 1
                self.dx =- self.dx
                self.dy = float(randrange(-100,100))/100
                self.r1.placer(30, Y/2-self.ty/2)
                self.r2.placer(X-30, Y/2-self.ty/2)
                PLAY = False



            tk.title("Player1 : "+str(Player1)+"    |   "+"Player2 : "+str(Player2))
            self.reset()

        tk.after(30,self.deplacer)


if __name__ == '__main__':
    terrain = Canvas(tk, bg="black",height = Y, width = X)
    terrain.pack()
    jeu = Pong()

    tk.mainloop()