
# Layout of the game is build

from tkinter import *


def SGEN(x,y):

    return str(x)+" "+str(y)


dX = [0,1,1,-1,-1,0,-1,1]
dY = [1,0,1,-1,0,-1,1,-1]

flag = {}

class Grid:

    def LoopWithZero(self,frame,x,y):

        flag[SGEN(x,y)]=1
        TotalMinesAround  = 0
            
        for i in range(8):
            xa = x+dX[i]
            ya = y+dY[i]

            s = SGEN(xa,ya)

            if s in self.MINE:
                TotalMinesAround+=1

            
        if TotalMinesAround == 0:

            lab = Label(frame,text=" ",fg="green",bg="snow3",relief="flat",height=2,width=4,borderwidth=0.5)
            lab.place(relx=0.086+0.045*x,rely=0.072+(0.080)*y,anchor="ne")

            for i in range(8):

                xa = x+dX[i]
                ya = y+dY[i]
                if SGEN(xa,ya) in flag:
                    continue
                if xa>=0 and xa<self._ROW and ya>=0 and ya<self._COL:

                    flag[SGEN(xa,ya)] = 1
                    self.LoopWithZero(frame,xa,ya)

        else:
            lab = Label(frame,text=str(TotalMinesAround),fg="green",bg="snow3",relief="flat",height=2,width=4,borderwidth=0.5)
            lab.place(relx=0.086+0.045*x,rely=0.072+(0.080)*y,anchor="ne")


                

        

    def _build_button(self,frame):
        # create all the sites which may or mat not have mine

        # dictionary to save button object with their respective coordinate
        place_array = {}
            
            
        def checkmine(event):
           
            x = place_array[event.widget][0]
            y = place_array[event.widget][1]
            s = SGEN(x,y)
            flag[s] = 1
            if s in self.MINE:
                self._Score -= 10
                self._score_board(frame)
                lab = Label(frame,text="M",fg="red",bg="snow3",relief="flat",height=2,width=4,borderwidth=0.5)
                lab.place(relx=0.086+0.045*x,rely=0.072+(0.080)*y,anchor="ne")
            else:

                TotalMinesAround = 0

                for i in range(8):
                    xa = x+dX[i]
                    ya = y+dY[i]

                    s =SGEN(xa,ya)

                    if s in self.MINE:
                        TotalMinesAround += 1

                
                for mines in self.MINE:
                    #print(mines)
                    mines = mines.strip().split()
                    x1 = int(mines[0])
                    y1 = int(mines[1])
                    c = 0
                    r = 0
                    if SGEN(x1,y1) in flag:
                        continue;
                    for i in range(8):
                        xa = x1+dX[i]
                        ya = y1+dY[i]
                        
                        if xa>=0 and xa<self._ROW and ya>=0 and ya<self._COL:
                            c+=1
                            s = SGEN(xa,ya)
                            if s in flag:
                                r+=1
                            else:
                                if s in self.MINE:
                                    r+=1

                    if r==c:
                        self._Score+=1
                        flag[SGEN(x1,y1)] = 1
                        lab = Label(frame,text="M",fg="red",bg="snow3",relief="flat",height=2,width=4,borderwidth=0.5)
                        lab.place(relx=0.086+0.045*x1,rely=0.072+(0.080)*y1,anchor="ne")

                self._score_board(frame)            
                if TotalMinesAround == 0:
                    self.LoopWithZero(frame,x,y)
                else:
                    lab = Label(frame,text=str(TotalMinesAround),fg="green",bg="snow3",relief="flat",height=2,width=4,borderwidth=0.5)
                    lab.place(relx=0.086+0.045*x,rely=0.072+(0.080)*y,anchor="ne")
            
        
        for i in range(self._ROW):

            for j in range(self._COL):

                btn = Button(frame,text="",height=2,width=4,borderwidth=0.5)

                btn.bind("<Button-1>",checkmine)
                
                # binding the button with event which is enabled when triggered ny user
                # it checks for mine and perform approriate task
                
                btn.place(relx=0.09+0.045*i,rely=0.07+(0.080)*j,anchor="ne")

                place_array[btn] = [i,j]
                # saving object in dictionary to get its position at run time
                
    def _score_board(self,frame):

        lab = Label(frame,text="Score : "+str(self._Score),width=10,height=3)
        lab.place(relx=0.15,rely=0.9,anchor="ne")

        
    def _make_grid(self):

        root = Tk()
        root.geometry("850x500")
        frame = Frame(root,height=500,width=850)
        
        self._build_button(frame)
        self._score_board(frame)
        frame.pack()
        root.mainloop()

    def __init__(self,row,col,mines):

        self._ROW = row
        self._COL = col
        self._Score = 0
        # Mine List
        self.MINE = mines
        
        
        self._make_grid()



