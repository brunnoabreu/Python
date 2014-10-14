import os
from random import randint

widthMat = 4
heightMat = 4
numMat = 2
minVal = 0
maxVal = 255


def genwrite_rand(arq):
        a = 0
        for y in range(heightMat):
                a = randint(minVal,maxVal)
		if a >= 100:
			arq.write(str(a))
		elif a >= 10 and a <= 99:
			arq.write("0" + str(a))
		elif a<10:
			arq.write("00" + str(a))
                for z in range(widthMat - 1):
                        a = randint(minVal,maxVal)
			if a >= 100:
                        	arq.write(" " + str(a))
			elif a>= 10 and a<=99:
				arq.write(" 0" + str(a))
			elif a<10:
				arq.write(" 00" + str(a))
                arq.write("\n")



source_file = '~/Documents/Prog_Python/'
destination = '~/Documents/vhdl/calcSAD'

arq = open("matA.txt", "w")
genwrite_rand(arq)
arq.close()
os.system('mv ' + source_file + 'matA.txt' + ' ' + destination)

arq = open("matB.txt", "w")
genwrite_rand(arq)
arq.close()
os.system('mv ' + source_file + 'matB.txt' + ' ' + destination)
