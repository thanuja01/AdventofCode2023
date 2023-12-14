from collections import defaultdict 

def partOne():
    totalPoints = 0
    with open("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\dayfour.txt","r") as data:
        for line in data:
            points = 0
            winningNumbers = line[line.index(':')+2:line.index('|')-1].split()
            print(winningNumbers)
            myNumbers = line[line.index('|')+1:].split()
            print(myNumbers)
            for n in winningNumbers:
                if n in myNumbers:
                    if points ==0:
                        points+=1
                    else:
                        points*=2
            totalPoints +=points     
    return totalPoints    

def partTwo():
     
     cardsDict = {}
     copies = defaultdict(lambda:1)
     final = defaultdict(int)
     with open("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\dayfour.txt","r") as data:
        for line in data:   
            print(str(line[line.index('d')+2:line.index('d')+5]).strip()+'w')
            #print('actual',line[line.index('|')+2:].split())
            cardsDict[str(line[line.index('d')+2:line.index('d')+5]).strip()+'w'] = line[line.index(':')+2:line.index('|')-1].split()
            cardsDict[str(line[line.index('d')+2:line.index('d')+5]).strip()+'a'] = line[line.index('|')+2:].split()
        for key in cardsDict.keys():
            if 'w' in key:

                wins = 0
                akey = key.replace('w', 'a')
                
                number = key.replace('w', '')
                for num in cardsDict[key]:
                    if num in cardsDict[akey]:
                        wins+=1
                noCopies = copies[int(number)]
                for i in range(1,(wins)+1):
                    copies[int(number)+i] = copies[int(number)+i] + noCopies 


     #print(copies)
     return sum(copies.values())



print(partTwo())