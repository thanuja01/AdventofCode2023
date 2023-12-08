
redCubes = 12
greenCubes = 13
blueCubes = 14
gameNoSum = 0

def partone():
    with open("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\daytwo.txt","r") as data:
        for line in data:
        
            sets = line.split(": ")[1].replace('\n','')
            sets = sets.split('; ')
            #print(sets)
            validGame = True
            for x in sets:
                red = 0
                blue = 0 
                green = 0
                x = x.split(', ')
                for y in x:
                    if y.split(' ')[1][0] =='r':
                        red = int(y.split(' ')[0])
                    if y.split(' ')[1][0] =='g':
                        green = int(y.split(' ')[0])
                    if y.split(' ')[1][0] =='b':
                        blue = int(y.split(' ')[0])
                #print('red: ',red,'green: ',green,'blue: ',blue)       
                if not(red <= redCubes and green <= greenCubes and blue <= blueCubes):
                    validGame = False
            if validGame:
                gameNoSum+= int(line.split(": ")[0][5:])
        print('gameno: ',gameNoSum)

def parttwo():
    totalSum =0
    with open("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\daytwo.txt","r") as data:
        for line in data:
            sets = line.split(": ")[1].replace('\n','')
            sets = sets.split('; ')
            #print(sets)
            red = 0
            blue = 0 
            green = 0
            for x in sets:
               
                x = x.split(', ')
                for y in x:
                    #print(y)
                    if y.split(' ')[1][0] =='r':
                        if  int(y.split(' ')[0]) >red:
                            red = int(y.split(' ')[0])
                    if y.split(' ')[1][0] =='g':
                       if  int(y.split(' ')[0]) >green:
                            green = int(y.split(' ')[0])
                    if y.split(' ')[1][0] =='b':
                        if  int(y.split(' ')[0]) >blue:
                           # print('change blue',y.split(' ')[0],'current',blue)
                            blue = int(y.split(' ')[0])
            totalSum += red * blue * green  
    return totalSum

print(parttwo())