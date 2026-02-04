numberList = [10, 3, 5, 11, 15, 11, 13, 3, 7, 1, 5, 7, 14, 4, 9, 10, 11, 11, 8, 12, 1, 12, 1, 2]
def rotate_left(numberList):
    numberList.append(numberList[0])
    numberList.remove(numberList[0])
    return numberList
print(rotate_left(numberList))

def greaterThanZero(inputList):
    allPositve=True
    for i in range(len(inputList)):
        if inputList[i]<=0:
            allPositve=False
    return allPositve
print(greaterThanZero (numberList))


