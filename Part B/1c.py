# def findmax(list,n):
# 	if(n==1):
# 		return list[0]
# 	return max(list[n-1],findmax(list,n-1))

# list = [1,2,3,4,5]
# n = len(list)
# print(findmax(list,n))


def findmax(list,n):
	if(n==1):
		return list[0]
	return max(list[n-1], findmax(list,n-1))

# list = [5,100,8,4,1]
list = []
n = int(input("Enter size : "))
for i in range(0,n):
	b = int(input("Enter value : "))
	list.append(b)

# n = len(list)
a = findmax(list,n)
print(a)

