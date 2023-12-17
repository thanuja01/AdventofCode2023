from operator import itemgetter
def partOne():
    maps = ['seed-to-soil map','soil-to-fertilizer map','fertilizer-to-water map','water-to-light map','light-to-temperature map','temperature-to-humidity map','humidity-to-location map']
    seedsInfo = {}
    seedLocations = []
    with open("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\dayfive.txt","r") as data:
        currentkey= ""
        seedsInfo['seeds'] = []
        for line in data:
            if line == '\n':
                continue
            if line[:5] == 'seeds' or seedsInfo.keys() == ['seeds']:
                seedsInfo['seeds'].append(line[7:].replace(':\n','').split())
            elif not line[0].isnumeric():
                key = line
                key = key.replace(':\n','')
                seedsInfo[key] = []
            else:
                seedsInfo[key].append(line.split())
    mapped =0
    for seed in seedsInfo['seeds'][0]:
        mapped = int(seed)
        for map in maps:
            valueFound = False
            for xrange in seedsInfo[map]:
                if mapped>=int(xrange[1]) and mapped<=int(xrange[1])+int(xrange[2]):
                    mapped = mapped - int(xrange[1])  + int(xrange[0])
                    valueFound = True
                    break
        seedLocations.append(mapped)


    print(seedLocations)
    return min(seedLocations)
def partTwo():
    
    maps = ['seed-to-soil map','soil-to-fertilizer map','fertilizer-to-water map','water-to-light map','light-to-temperature map','temperature-to-humidity map','humidity-to-location map']
    seedsInfo = {}
    seedLocations = []
    with open("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\dayfive.txt","r") as data:
        currentkey= ""
        seedsInfo['seeds'] = []
        for line in data:
            if line == '\n':
                continue
            if line[:5] == 'seeds' or seedsInfo.keys() == ['seeds']:
                seedsInfo['seeds'].append(line[7:].replace(':\n','').split())
            elif not line[0].isnumeric():
                key = line
                key = key.replace(':\n','')
                seedsInfo[key] = []
            else:
                seedsInfo[key].append(line.split())
    print('original dict created...')
    newSeeds = []     
    for i in range(0,len(seedsInfo['seeds'][0]),2):
        newSeeds.append(seedsInfo['seeds'][0][i])
        newSeeds.append(seedsInfo['seeds'][0][i]+seedsInfo['seeds'][0][i+1])
    # for i in range(0,len(seedsInfo['seeds'][0]),2):
    #     #for j in range(int(seedsInfo['seeds'][0][i]),int(seedsInfo['seeds'][0][i])+int(seedsInfo['seeds'][0][i+1])):
    #         newSeeds.append(list(range(int(seedsInfo['seeds'][0][i]), int(seedsInfo['seeds'][0][i])+int(seedsInfo['seeds'][0][i+1]))))
    #         print('range ',i,' added')
    # print('ranged seeds added...')   
    mapped =0
    for seed in newSeeds:
        mapped = int(seed)
        for map in maps:
            valueFound = False
            for xrange in seedsInfo[map]:
                if mapped>=int(xrange[1]) and mapped<=int(xrange[1])+int(xrange[2]):
                    mapped = mapped - int(xrange[1])  + int(xrange[0])
                    valueFound = True
                    break
        seedLocations.append(mapped)

    print('locations calculated')
    print(seedLocations)
    return min(seedLocations)
def finalLocation(maps,seedsInfo,mapped,seedLocations):
    for map in maps:
        # valueFound = False
                
                for xrange in seedsInfo[map]:
                    if mapped>=int(xrange[1]) and mapped<int(xrange[1])+int(xrange[2]):
                        mapped = mapped - int(xrange[1])  + int(xrange[0])
                        #valueFound = True
                        break
           # toAdd.append(mapped)

    seedLocations.append(mapped)
def checkRanges(seedLocations,splits):
    changed = True
    for i in range(0,len(seedLocations),2):
        if seedLocations[i]>seedLocations[i+1]:  
            if i ==0:
                index = 0
            elif i%2==0:
                index = round(i/2)
            elif i%2==1:
                index = round((i+1)/2)
            if index != int(splits[index][0])+1!=int(splits[index][1]) :
                newfirstRangeEnd = round((splits[index][0]+splits[index][1])/2)
                newsecondRangeEnd = splits[index][1]
                splits[index] = [splits[index][0],round(newfirstRangeEnd)]
                splits.insert(index+1,[newfirstRangeEnd+1,newsecondRangeEnd])
                break
        if i == len(seedLocations) -2:
            changed = False
    return changed
def partTwoMethodB():
   # maps = ['humidity-to-location map','temperature-to-humidity map','light-to-temperature map','water-to-light map','fertilizer-to-water map','soil-to-fertilizer map','seed-to-soil map']
    maps = ['seed-to-soil map','soil-to-fertilizer map','fertilizer-to-water map','water-to-light map','light-to-temperature map','temperature-to-humidity map','humidity-to-location map']

    seedsInfo = {}
    seedLocations = []
    with open("C:\\Users\\thanu\\OneDrive\\Documents\\Advent of Code 2023\\dayfive.txt","r") as data:
        ##add in all data
        currentkey= ""
        seedsInfo['seeds'] = []
        for line in data:
            if line == '\n':
                continue
            if line[:5] == 'seeds' or seedsInfo.keys() == ['seeds']:
                seedsInfo['seeds'].append(line[7:].replace(':\n','').split())
            elif not line[0].isnumeric():
                key = line
                key = key.replace(':\n','')
                seedsInfo[key] = []
            else:
                seedsInfo[key].append(line.split())
    print('original dict created...')
    ##sort seeds in increasing order
    for key in seedsInfo.keys():
        seedsInfo[key] = (sorted(seedsInfo[key], key=itemgetter(1)))
    splits = []
    ##create ranges for my seeds and add them all to splits in pairs
    for i in range(0,len(seedsInfo['seeds'][0]),2):
        splits.append([int(seedsInfo['seeds'][0][i]),int(seedsInfo['seeds'][0][i])+round(int(seedsInfo['seeds'][0][i+1])/4)])
        splits.append([int(seedsInfo['seeds'][0][i])+round(int(seedsInfo['seeds'][0][i+1])/4)+1,int(seedsInfo['seeds'][0][i])+round(int(seedsInfo['seeds'][0][i+1])/4)*2+1])
      #  splits.append([int(seedsInfo['seeds'][0][i])+round(int(seedsInfo['seeds'][0][i+1])/4)*2+2,int(seedsInfo['seeds'][0][i])+round(int(seedsInfo['seeds'][0][i+1])/4)*3+2])
        splits.append([int(seedsInfo['seeds'][0][i])+round(int(seedsInfo['seeds'][0][i+1])/4)*2+2,int(seedsInfo['seeds'][0][i])+int(seedsInfo['seeds'][0][i+1])])
    print('ranges added...',splits)
    ##calculate the final location map of each bound of each range
    for split in splits:
        
        for bound in split:                
            mapped = bound
            finalLocation(maps,seedsInfo,mapped,seedLocations) 
    print('splits:',splits)
    print('seedLocations:',seedLocations)
    ##make sure that the range is all good: map is increasing for each range
    changed = True
    while changed == True:
     changed = checkRanges(seedLocations,splits)
     #finalLocation(maps,seedsInfo,mapped,seedLocations) 
     seedLocations =[]
     for split in splits:
        for bound in split:                
            mapped = bound
            finalLocation(maps,seedsInfo,mapped,seedLocations) 
     print(splits)
     print(seedLocations)
    ##this is something i used for another method, no longer needed            
    if seedLocations.index(min(seedLocations))%2 == 1:
        lowestLocationRange =  splits[seedLocations.index(min(seedLocations)) -1]
    else:
        lowestLocationRange =  splits[seedLocations.index(min(seedLocations)) ]
    print('lowest range found: ',lowestLocationRange)

    print(seedLocations)
    print(splits)
    return min(seedLocations)
print(partTwoMethodB())



 