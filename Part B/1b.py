text = open("file.txt","r")
d = dict()
for line in text:
	line = line.lower()
	words = line.split(" ")

for word in words:
	if word in d:
		d[word] = d[word]+1
	else:
		d[word] = 1


for k,v in d.items():

	print(str(k)+'-->'+str(v))


