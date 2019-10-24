def remove(list):
	newList = []
	for num in list:
		if num not in newList:
			newList.append(num)
	return newList 

list = [1,2,3,4,5,6,7,8,9,2,3,4,5,6,2,3,4,5]
newList = remove(list)
print(newList)

evenList = [elem for elem in newList if elem%2 == 0]
print(evenList)
reverse = newList[::-1]
print(reverse)
