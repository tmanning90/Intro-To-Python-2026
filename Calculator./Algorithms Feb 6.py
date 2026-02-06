def search(inputList, target, leftBound, rightBound):
    # Base case: bounds crossed means target is not present
    if leftBound > rightBound:
        return -1
    
    mid = (leftBound + rightBound) // 2
    
    # Found the target
    if inputList[mid] == target:
        return mid
    
    # Target is smaller: search left half
    elif target < inputList[mid]:
        return search(inputList, target, leftBound, mid - 1)
    
    # Target is larger: search right half
    else:
        return search(inputList, target, mid + 1, rightBound)



myList = [0,3,4,9]
print(search(myList, 9, 0, len(myList)))
print(search(myList, 2, 0, len(myList)))

newList = [1,25,3,14,5,64,7,8]
print(search(newList, 2, 0, len(newList)))
print(search(newList, 8, 0, len(newList)))
            