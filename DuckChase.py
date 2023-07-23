import tkinter as tk
import Duck
import random 
from PIL import Image,ImageTk


class DuckChase:
    def __init__(self):
        #Construct Window
        self.root = tk.Tk()
        self.root.geometry("1000x1000")
        self.playAreaHeight = 800
        self.playAreaWidth = 800
        self.root.title("Duck Chase")
        self.canvas = tk.Canvas(self.root, bg = "black",height= 800, width=800)
        self.canvas.pack()

       

        #Duck Stats
        self.smallDuck = Duck.Duck("donald",1 )
        self.bigDuck = Duck.Duck ("fred", 5 )
        self.smallDucksize = 10 * self.smallDuck.weight
        self.bigDucksize = 10 * self.bigDuck.weight
    
        self.root.bind('<Up>', self.keyUp)
        self.root.bind('<Down>', self.keyDown)
        self.root.bind('<Right>', self.keyRight)
        self.root.bind('<Left>', self.keyLeft)
        # self.root.bind('<Button-1', self.LeftClick)

        self.root.bind('<w>', self.keyW)
        self.root.bind('<s>', self.keyS)
        self.root.bind('<d>', self.keyD)
        self.root.bind('<a>', self.keyA)
      
        self.smallDuckImg = ImageTk.PhotoImage(Image.open("smallDuck.png"))
        self.BigDuckImg = ImageTk.PhotoImage(Image.open("bigDuck.png"))
        self.smallDucksize = self.smallDuckImg.width()
        self.bigDucksize = self.BigDuckImg.width()
        self.setNewPosition()

        self.canvas.create_image(self.smallDuck.x,self.smallDuck.y,anchor=tk.NW,image=self.smallDuckImg)
        self.canvas.create_image(self.bigDuck.x,self.bigDuck.y,anchor=tk.NW,image=self.BigDuckImg)



        # x = 20
        # y = 30
        # self.canvas.after(2000,lambda:self.canvas.create_rectangle(x,y,x+10,y+10, fill = "red" ,outline= "white" ))
        # self.canvas.after(4000,lambda:self.canvas.create_rectangle(x,y,x+10,y+10, fill = "white",outline= "white"))

        # self.canvas.after(4000,lambda: self.canvas.create_rectangle(x+10,y,x+20,y+10, fill = "red",outline= "white"))
        # self.canvas.after(6000,lambda: self.canvas.create_rectangle(x+10,y,x+20,y+10, fill = "white",outline= "white"))

        # xtwo=240
        # ytwo=240
        # self.canvas.after(6000,lambda:self.canvas.create_rectangle(xtwo,ytwo,x+300,y+300, fill = "yellow",outline= "white"))
        # self.canvas.after(8000,lambda:self.canvas.create_rectangle(xtwo,ytwo,x+300,y+300, fill = "white",outline= "white"))

        
        # self.canvas.after(8000,lambda:self.canvas.create_rectangle(xtwo,ytwo+60,x+300,y+330, fill = "yellow",outline= "white"))
        # self.canvas.after(10000,lambda:self.canvas.create_rectangle(xtwo,ytwo+60,x+300,y+330, fill = "white",outline= "white"))
       

        # self.canvas.create_oval(300,200,200,300, fill = "blue") 
        # self.canvas.create_arc(600, 700, 1200, 10, start = 0,extent = 300, outline = "blue",fill = "yellow", width = 2)
        # self.canvas.create_arc(200, 700, 400, 10, start = 0,extent = 20, outline = "blue",fill = "orange", width = 2)

        self.root.mainloop()

    def checkIfDucksAreTouching(self):
        if self.smallDuck.x > self.bigDuck.x and self.smallDuck.x < self.bigDuck.x + self.bigDucksize and self.smallDuck.y > self.bigDuck.y and self.smallDuck.y < self.bigDuck.y + self.bigDucksize:
            self.eraseDuck(self.smallDuck, self.smallDucksize)
            self.eraseDuck(self.bigDuck, self.bigDucksize)
            self.setNewPosition()
            self.canvas.create_image(self.smallDuck.x,self.smallDuck.y,anchor=tk.NW,image=self.smallDuckImg)
            self.canvas.create_image(self.bigDuck.x,self.bigDuck.y,anchor=tk.NW,image=self.BigDuckImg)

    def setNewPosition(self):
            self.smallDuck.x = random.randint(0,self.playAreaWidth//2 - self.smallDucksize)
            self.smallDuck.y = random.randint(0,self.playAreaHeight//2 - self.smallDucksize)
            self.bigDuck.x = random.randint(self.playAreaWidth//2,self.playAreaHeight -self.bigDucksize)
            self.bigDuck.y = random.randint(self.playAreaWidth//2,self.playAreaHeight - self.bigDucksize)

    def eraseDuck(self,duck,duckSize):
        self.canvas.create_rectangle(duck.x,duck.y,duck.x + duckSize ,duck.y + duckSize,fill= "black", outline = "black")

    def keyLeft(self,event):
        self.eraseDuck(self.smallDuck, self.smallDucksize)
        self.smallDuck.x = self.smallDuck.x - self.smallDucksize
        self.canvas.create_image(self.smallDuck.x,self.smallDuck.y,anchor=tk.NW,image=self.smallDuckImg)
        self.checkIfDucksAreTouching()

    def keyDown(self,event):
        self.eraseDuck(self.smallDuck, self.smallDucksize)
        self.smallDuck.y = self.smallDuck.y + self.smallDucksize
        self.canvas.create_image(self.smallDuck.x,self.smallDuck.y,anchor=tk.NW,image=self.smallDuckImg)
        self.checkIfDucksAreTouching()

    def keyUp(self,event):
        self.eraseDuck(self.smallDuck, self.smallDucksize)
        self.smallDuck.y = self.smallDuck.y - self.smallDucksize
        self.canvas.create_image(self.smallDuck.x,self.smallDuck.y,anchor=tk.NW,image=self.smallDuckImg)
        self.checkIfDucksAreTouching()

    def keyRight(self,event):
        self.eraseDuck(self.smallDuck, self.smallDucksize)
        self.smallDuck.x = self.smallDuck.x + self.smallDucksize
        self.canvas.create_image(self.smallDuck.x,self.smallDuck.y,anchor=tk.NW,image=self.smallDuckImg)
        self.checkIfDucksAreTouching()


    def keyA(self,event):
        self.eraseDuck(self.bigDuck, self.bigDucksize)
        self.bigDuck.x = self.bigDuck.x - self.bigDucksize
        self.canvas.create_image(self.bigDuck.x,self.bigDuck.y,anchor=tk.NW,image=self.BigDuckImg)
        self.checkIfDucksAreTouching()

    def keyS(self,event):
        self.eraseDuck(self.bigDuck, self.bigDucksize)
        self.bigDuck.y = self.bigDuck.y + self.bigDucksize
        self.canvas.create_image(self.bigDuck.x,self.bigDuck.y,anchor=tk.NW,image=self.BigDuckImg)
        self.checkIfDucksAreTouching()

    def keyW(self,event):
        self.eraseDuck(self.bigDuck, self.bigDucksize)
        self.bigDuck.y = self.bigDuck.y - self.bigDucksize
        self.canvas.create_image(self.bigDuck.x,self.bigDuck.y,anchor=tk.NW,image=self.BigDuckImg)
        self.checkIfDucksAreTouching()

    def keyD(self,event):
        self.eraseDuck(self.bigDuck, self.bigDucksize)
        self.bigDuck.x = self.bigDuck.x + self.bigDucksize
        self.canvas.create_image(self.bigDuck.x,self.bigDuck.y,anchor=tk.NW,image=self.BigDuckImg)
        self.checkIfDucksAreTouching()