list = [ 1,2,3,4,5,6 ]
print("Original list is")
print(list)
multiplied = [x*3 for x in list]
print("Multiplied List is")
print(multiplied)
sum = 0
sum1 = 0
for x in list:
	sum = lambda x, sum : sum + x
for y in multiplied:
	sum2 = lambda x, sum2 : sum2 + x
print(sum)
print(sum1)
