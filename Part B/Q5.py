import sys  #system import
import os   #os import
from functools import reduce

dict={}  #empty dictionary create

if(len(sys.argv)!=2):               #length of arguments must strictly be 2
	print("Invalid arguments")
	sys.exit()

if(not(os.path.exists(sys.argv[1]))):    #check if file path is valid
	print("File not present in path")
	sys.exit()

if(sys.argv[1].split(".")[-1]!="txt"):  # Ensure it's a text file only
	print("Only txt files accepted")
	sys.exit()

with open(sys.argv[1]) as file:   #open file and store words in dictionary
	for line in file:
		for word in line.split():  
			dict[word]=dict.get(word,0)+1  #count number of occurences of each word
	print(dict)

sl=[]  #list of lists
sl=sorted(dict.items(), key=lambda x:x[1], reverse=True)  #sort based on key, where key=occurrences
print(sl[:10])  #printing top 10 results

word=[]
for i,j in sl[:10]:       #i=key,j=value in each iteration of list of lists
	word.append(len(i))
print(word)

sum=reduce((lambda x,y:x+y),word)
print("Avs is", sum/len(word))

print([x*x for x in word if x%2!=0])
