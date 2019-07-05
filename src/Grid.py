
# Layout of the game is build

from tkinter import *
import threading

NUMBER_OF_THREAD = 8

# creating thread
def create_worker(argument):

    # argument = [self,frame,x,y]
    t = threading.Thread(target=argument[0].LoopWithZero,args=argument[1:])
    t.daemon = True
    t.start()
    


# string generation of x and y co-ordinate
def SGEN(x,y):

    return str(x)+" "+str(y)


dX = [0,1,1,-1,-1,0,-1,1]
dY = [1,0,1,-1,0,-1,1,-1]

# Dictionary for chacking wheather the cell is uncovered of not
flag = {}

class Grid:

    def LoopWithZero(self,frame,xm,ym):

        # building stack for Depth First Search
        stack = [[xm,ym]]

        while len(stack) > 0:
            
            # poping the last element
            x = stack[len(stack)-1][0]
            y = stack[len(stack)-1][1]
            stack.pop()
            print((x,y))
            flag[SGEN(x,y)]=1
            TotalMinesAround  = 0

            # looping thraugh all neighbouring cell
            for i in range(8):
                xa = x+dX[i]
                ya = y+dY[i]

                s = SGEN(xa,ya)

                if s in self.MINE:
                    TotalMinesAround+=1

            
            if TotalMinesAround == 0:

                # if no mines were found 
                lab = Label(frame,text=" ",fg="green",bg="snow3",relief="flat",height=2,width=4,borderwidth=0.5)
                lab.place(relx=0.086+0.045*x,rely=0.072+(0.080)*y,anchor="ne")

                # adding the neighbouring cell in stack
                for i in range(8):

                    xa = x+dX[i]
                    ya = y+dY[i]

                    # checking if cell is uncovered or not
                    if SGEN(xa,ya) in flag:
                        continue

                    # if uncovered checking for its coordinates
                    if xa>=0 and xa<self._ROW and ya>=0 and ya<self._COL:

                        flag[SGEN(xa,ya)] = 1
                        # pushing the element in stack
                        stack.append([xa,ya])

            else:
                # if mines were found showing appropriate result
                lab = Label(frame,text=str(TotalMinesAround),fg="green",bg="snow3",relief="flat",height=2,width=4,borderwidth=0.5)
                lab.place(relx=0.086+0.045*x,rely=0.072+(0.080)*y,anchor="ne")


                

    def ALLMINE(self,frame):

        # checking all the mines if they are uncovered or not
        # mine is uncovered either by if its cell is triggered
        # or if all its surrounding cell are uncovered

        for mines in self.MINE:
            #print(mines)
            mines = mines.strip().split()
            x1 = int(mines[0])
            y1 = int(mines[1])
            # to inintalize all the valid neighbouring cell
            c = 0
            # all the uncovered neighbouring cell
            r = 0

            # if r == c
            # the mine should be uncovered

            # check for if this mine was earlier uncovered
            if SGEN(x1,y1) in flag:
                continue;

            # looping through all the surrounding cell
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
            # uncovering the mine
            if r==c:

                # incrementing user score
                self._Score+=1
                flag[SGEN(x1,y1)] = 1
                # uncovering the mine
                lab = Label(frame,text="M",fg="red",bg="snow3",relief="flat",height=2,width=4,borderwidth=0.5)
                lab.place(relx=0.086+0.045*x1,rely=0.072+(0.080)*y1,anchor="ne")

    def _build_button(self,frame):
        # create all the sites which may or mat not have mine

        # dictionary to save button object with their respective coordinate
        place_array = {}
            
        
        def checkmine(event):

            # accessing coordinate of button on grid thraugh place_array based upon event object
            x = place_array[event.widget][0]
            y = place_array[event.widget][1]
            s = SGEN(x,y)
            # asign its status
            flag[s] = 1

            # checking if cell is mine or not
            if s in self.MINE:

                # if mine then reducing the score
                self._Score -= 10
                self._score_board(frame)

                # uncovering the mine    
                lab = Label(frame,text="M",fg="red",bg="snow3",relief="flat",height=2,width=4,borderwidth=0.5)
                lab.place(relx=0.086+0.045*x,rely=0.072+(0.080)*y,anchor="ne")
            
            else:

                # if not mine the calculating total mine around in its neighbour
                TotalMinesAround = 0

                # looping thraugh all the mines
                for i in range(8):
                    xa = x+dX[i]
                    ya = y+dY[i]

                    s = SGEN(xa,ya)

                    if s in self.MINE:
                        TotalMinesAround += 1

                

                # score update
                self._score_board(frame)            

                # checking if in surrounding no mines were found
                if TotalMinesAround == 0:

                    # uncovering the cell
                    lab = Label(frame,text=" ",fg="green",bg="snow3",relief="flat",height=2,width=4,borderwidth=0.5)
                    lab.place(relx=0.086+0.045*x,rely=0.072+(0.080)*y,anchor="ne")

                    # creating a thread for each neighbouring cell
                    for i in range(8):

                        # thread is created
                        # comment it for non multithreading process
                        xa = x+dX[i]
                        ya = y+dY[i]
                        if xa>=0 and xa<self._ROW and ya>=0 and ya<self._COL:
                            create_worker([self,frame,xa,ya])

                            # uncomment below command for non multithreading process
                            #self.LoopWithZero(frame,x+dX[i],y+dY[i])

                else:

                    # displaying count of totalminesaround on uncovered cell
                    lab = Label(frame,text=str(TotalMinesAround),fg="green",bg="snow3",relief="flat",height=2,width=4,borderwidth=0.5)
                    lab.place(relx=0.086+0.045*x,rely=0.072+(0.080)*y,anchor="ne")

                # mine check
                self.ALLMINE(frame)
                self._score_board(frame)
            
        # ----------------------------------------------------------------------------------------------------------------------------


        # building the grid with buttons
        for i in range(self._ROW):

            for j in range(self._COL):
                #print(i,j)
                btn = Button(frame,text="",height=2,width=4,borderwidth=0.5)

                # assignung event when triggered
                btn.bind("<Button-1>",checkmine)
                
                # binding the button with event which is enabled when triggered ny user
                # it checks for mine and perform approriate task
                
                btn.place(relx=0.09+0.045*i,rely=0.07+(0.080)*j,anchor="ne")

                place_array[btn] = [i,j]
                # saving object in dictionary to get its position at run time
            

                
    def _score_board(self,frame):

        # setting up scroing area
        lab = Label(frame,text="Score : "+str(self._Score),width=10,height=3)
        lab.place(relx=0.15,rely=0.9,anchor="ne")

        
    def _make_grid(self):

        # setting up grid structure
        root = Tk()
        root.geometry("850x500")

        # setting main game frame
        frame = Frame(root,height=500,width=850)

        # building button
        self._build_button(frame)

        # building scroe board
        self._score_board(frame)
        frame.pack()
        root.mainloop()

    def __init__(self,row,col,mines):
        print("Game is Rolling!!!")
        self._ROW = row
        self._COL = col
        self._Score = 0
        # Mine List
        self.MINE = mines
        
        
        self._make_grid()



