myList = []
myList.append("art")
myList.append("book")
myList.append("captcha")
temp = myList[0]
myList.remove(temp)
myList.insert(0, myList[1])
myList.remove(myList[2])
myList.insert(2, temp)

for item in myList:
    print (item, end=" ")






