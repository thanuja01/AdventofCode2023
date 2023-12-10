
from binhex import LINELEN
import curses
import re
from tkinter import CURRENT
import numpy as np

def partOne():
    totalParts =[]

    with open("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\daythree.txt","r") as data:
       schematicArray = []
       numberCheckArr = []
       allnum = []
       currentstr = ""
       regEx = r"/\.+/"
       for line in data:      

           schematicArray.append([x for x in line if x != '\n'])
           currentnum = ""
           valid = True 
       for row in range(len(schematicArray)):
           for column in range(len(schematicArray[0])):               
               if schematicArray[row][column].isdigit():
                   currentstr  +=schematicArray[row][column]
                   currentnum +=schematicArray[row][column]
                   #print('digit: ',schematicArray[row][column])
                   for r in range(-1,2):
                       for c in range(-1,2):
                           if row+r<=len(schematicArray)-1 and column+c<= len(schematicArray[0])-1:                              
                               if  schematicArray[row+r][column+c].isalnum() and schematicArray[row+r][column+c] != '.':
                                   valid = False 
                                   currentnum = ""
                                 
               else:
                   if currentstr:
                       allnum.append(int(currentstr))
                       currentstr = ""
                   if  valid and currentnum:
                       totalParts.append(int(currentnum))
                   valid = True
                   currentnum = ""
       #for i in range(len(schematicArray)):
       #    print(schematicArray[i])
       print(allnum)
       return   sum([i for i in allnum if i not in totalParts])
def partOnea():
    totalParts =[]

    with open("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\daythree.txt","r") as data:
       schematicArray = []
       currentstr = ""
       validParts = []
       index = []
       for line in data:      

           schematicArray.append([x for x in line if x != '\n'])
           currentnum = ""
           valid = False 

       for row in range(len(schematicArray)):
           for column in range(len(schematicArray[0])):      
               print('row and column: ',row,column)
               if schematicArray[row][column].isdigit():
                   if not currentstr:
                       index = [row,column]
                   currentstr += schematicArray[row][column]
                    
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

print(partOnea())