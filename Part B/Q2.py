value=0
def kelvin_fahrenheit(value):
	value = ((value-273)*9)/5+32
	print (value)
def kelvin_calcius(value):
	value = ((value-32)*(5/9))+273
	print (value)
def fahrenheit_kelvin(value):
	value= ((value-32)*5)/9+273
	print (value)	
def fahrenheit_celcius(value):
	value= ((value-32)*5)/9
	print (value)				
def celcius_kelvin(value):	
	value= value+273
	print (value)
def celcius_fahrenheit(value):
	print("Value is")
	value = value*33.8
	print(value)


print("These are the conversions we provide")
li = ['celcius', 'fahrenheit', 'kelvin']
print(li)
choice = input("Enter your value type:")
value = int(input("Enter the value:"))

if(choice == 'celcius'):
	c = input("Convert to?")
	if(c == 'fahrenheit'):
		celcius_fahrenheit(value)
	if(c == 'kelvin'):
		celcius_kelvin(value)

if(choice == 'kelvin'):
	c = input("Convert to?")
	if(c == 'fahrenheit'):
		kelvin_fahrenheit(value)
	if(c == 'celcius'):
		kelvin_calcius(value)

if(choice == 'fahrenheit'):
	c = input("Convert to?")
	if(c == 'celcius'):
		fahrenheit_celcius(value)
	if(c == 'kelvin'):
		fahrenheit_kelvin(value)