
myList = []
for i in range(3):
	myList.append(input("Please enter values for list1 : "))
myList2 = []
for j in range(3):
	myList2.append(input("Please enter values for list2 : "))
mergedList = myList + myList2
mergedList.sort()
print(mergedList)
