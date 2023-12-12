
from binhex import LINELEN
from curses.ascii import isdigit
from inspect import currentframe
import re
from tkinter import CURRENT
import numpy as np
from collections import defaultdict

def partOne():
    totalParts =[]

    with open("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\daythree.txt","r") as data:
       schematicArray = []
       currentstr = ""
       validParts = []
       index = []
       for line in data:      

           schematicArray.append([x for x in line if x != '\n'])
        
           valid = False 

       for rowSchematic in range(len(schematicArray)):
           for columnSchematic in range(len(schematicArray[0])):      
               print('row and column: ',rowSchematic,columnSchematic)
               if schematicArray[rowSchematic][columnSchematic].isdigit():
                   if not currentstr:
                       index = [rowSchematic,columnSchematic]
                   currentstr += schematicArray[rowSchematic][columnSchematic]
                    
               else:
                    if currentstr:
                        for i in range(len(currentstr)):
                            row = index[0]
                            column = index[1]+i
                            for r in range(-1,2):
                               for c in range(-1,2):
                                   if row+r<=len(schematicArray)-1 and row+r>=0 and  column+c>=0 and column+c<= len(schematicArray[0])-1:                              
                                       if not( schematicArray[row+r][column+c].isalnum()) and schematicArray[row+r][column+c] != '.':
                                         #  print('allnum: ',allnum)
                                          # print('key',key)
                                          print('key: ',currentstr[i],'row: ',row+r,'column: ',column+c,'char: ',schematicArray[row+r][column+c])
                                          valid = True
                    if valid:
                        print('adding...',currentstr)
                        validParts.append(int(currentstr))
                    currentdict = {}
                    valid = False
                    index = []
                    currentstr = ""
   
    print('rows: ',len(schematicArray),'columns: ',len(schematicArray[0]))
    print(validParts)
    return sum(validParts)

def partTwo():
     with open("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\daythree.txt","r") as data:
       schematicArray = []
       allNum = {}
       currentstr = ""
       currentnum = []
       validGear = defaultdict(int)
       gearRatios = 0
       for line in data:      
           schematicArray.append([x for x in line if x != '\n'])

     for rowSchematic in range(len(schematicArray)):
           for columnSchematic in range(len(schematicArray[0])):      
               #print('row and column: ',rowSchematic,columnSchematic)
               if schematicArray[rowSchematic][columnSchematic].isdigit():
                   if not currentstr:
                       index = str(rowSchematic) +'.' + str(columnSchematic)
                   currentstr += schematicArray[rowSchematic][columnSchematic]
                    
               else:
                    if currentstr:
                        print('num: ',currentstr)
                        allNum[index] = int(currentstr)
                    currentstr = ""

     for row in range(len(schematicArray)):
           for column in range(len(schematicArray[0])):      
              # print('row and column: ',row,column)
               if schematicArray[row][column]== '*':
                   for r in range(-1,2):
                               for c in range(-1,2):
                                   if row+r<=len(schematicArray)-1 and row+r>=0 and  column+c>=0 and column+c<= len(schematicArray[0])-1:                              
                                       if  schematicArray[row+r][column+c].isdigit():
                                           
                                           if  not schematicArray[row+r][column+c-1].isdigit():
                                        
                                                 if allNum[str(row+r)+'.'+str(column+c)] not in currentnum:
                                                    currentnum.append(allNum[str(row+r)+'.'+str(column+c)])
                                           elif  (schematicArray[row+r][column+c-1].isdigit() and not schematicArray[row+r][column+c-2].isdigit()) :
                                           
                                                 if allNum[str(row+r)+'.'+str(column+c-1)] not in currentnum:
                                                   currentnum.append(allNum[str(row+r)+'.'+str(column+c-1)])
                                           elif (schematicArray[row+r][column+c-1].isdigit() and schematicArray[row+r][column+c-2].isdigit()):
                                            
                                                 if allNum[str(row+r)+'.'+str(column+c-2)] not in currentnum:
                                                  currentnum.append(allNum[str(row+r)+'.'+str(column+c-2)])
                   if len(currentnum) == 2:
                       print('currentnum: ',currentnum)
                       gearRatios += (currentnum[0]*currentnum[1])
                   currentnum = []
                   validGear = defaultdict(int)

     return gearRatios
print(partTwo())