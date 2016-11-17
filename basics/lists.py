myList = ['item1', 2, 'item3', 4]

print(myList[2])

for i in myList:
    print(i)

del myList[2]

print(myList[-2])

print(myList[1:2])

myList[1:3] = [1, 2, 4, 5]    # mutate parts of list

print(myList)

compList = [myList, myList]

print(compList, compList[0][2])

myList.append('item5')

myList.remove('item1')

myList.insert(2, 'itemx')

print(myList, len(myList))

otherList = [1, 3, 2, 5, 8]

sortIt = otherList.sort()
reverseIt = otherList.reverse()

print(sortIt, reverseIt, max(otherList), min(otherList))
