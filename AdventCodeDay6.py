import numpy as np
def partOne():
    time = []
    distance = []
    options = []
    with open("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\daysix.txt","r") as data:
        for line in data:            
            array = line.replace('\n','').split(' ')
            print(array)
            if array[0] == 'Time:':
                time =[x for x in array if x.isnumeric()]
            else:
                distance = [x for x in array if x.isnumeric()]
    options = np.zeros(len(time))
    for i in range(len(time)):
        for j in range(1,int(time[i])):
           if (int(time[i])-j)*j > int(distance[i]):
               options[i]+=1
             
    print(np.prod(options))
def partTwo():
     options = 0
     with open("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\daysix.txt","r") as data:
        for line in data:    
            arr = line.replace('\n','').split(' ')  
            if arr[0] == 'Time:':
                time = ''.join([x for x in arr if x.isnumeric()])  
            else :
                distance = ''.join([x for x in arr if x.isnumeric()])
     for i in range(1,int(time)):
          if (int(time)-i)*i > int(distance):
               options+=1
     return options

print(partTwo())   

