
# To create random list of mines

import random


class MinesGenerator:

    def Mines(self):

        # Generated new length of mines
        
        TotalMines = random.randrange(20,50)

        count = 0
        dic = {}
        # to check if mines not repeated
        
        while count < TotalMines:
            
            a = random.randrange(0,self._ROW)
            # a : x-axis of new mine
            
            b = random.randrange(0,self._COL)
            # b : y-axis of new mine

            s = str(a)+" "+str(b)

            # check if new mine is not repeated
            
            if s not in dic:

                dic[s] = 1
                count += 1
                self.mines[s]=1
                
        return self.mines
            
        
    def __init__(self,row,col):

        self._ROW = row
        self._COL = col

        self.mines = {}

        # new list of mines



