def AtomicDictionary():
	atomic =	{
  	"H": "Hydrogen" 
	}
	print("Enter a unique element")
	symbol = input('Enter the symbol: ')
	name = input('Enter the name: ')
	if symbol in atomic:
		print("Element is duplicate")
	else:
		atomic[symbol] = name		
	print("Your final dictionary is")
	print(atomic)	
	print("Length is")	
	print(len(atomic))
	element = input("Enter an element symbol to search: ")
	if element in atomic:
		print("Found")
	else:
		print("Not found")


