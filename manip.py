inArq = open("out.txt","r")
outArq = open("outF.txt","w")

for lines in inArq:
	for words in lines:

inArq.close()
outArq.close()
