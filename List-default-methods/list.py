list = [ 1,2,3,4,5,6 ]
print("Original list is")
print(list)
multiplied = [x*3 for x in list]
print("Multiplied List is")
print(multiplied)
sum = 0
sum1 = 0
sum = reduce(lambda x, y : x+y , list)
sum1 = reduce(lambda x, y : x+y , multiplied)
print(sum)
print(sum1)
