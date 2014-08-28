from random import randint

widthMat = 32
heightMat = 32
numMat = 2
minVal = 0
maxVal = 255


def genwrite_rand(arq):
	a = 0
	for y in range(heightMat * 2):
		a = randint(minVal,maxVal)
		arq.write(str(a))
		for z in range(widthMat - 1):
			a = randint(minVal,maxVal)
			arq.write(" " + str(a))
		arq.write("\n")


def get_from_file(mat, arq):
	width = 0
	height = 0
	num = 0
	for line in arq:
		for word in line.split():
			mat[num][width][height] = int(word.strip())
			width += 1
		height += 1
		if height > 31 and num == 0:
			num += 1
			height = 0
		width = 0


def calc_SAD(mat):
	a = 0
	for x in range(widthMat):
		for y in range(heightMat):
			a += abs(mat[0][x][y] - mat[1][x][y])
	return a


def calc_SSE(mat):
	a = 0
	for x in range(widthMat):
		for y in range(heightMat):
			a += (mat[0][x][y] - mat[1][x][y]) ** 2
	return a


def print_mat(mat):
	for x in range(numMat):
		for y in range(heightMat):
			for z in range(widthMat):
				print str(mat[x][z][y]) + " "
			print "\n"
		print "\n\n\n"


mat = [ [ [0 for i in xrange(heightMat)] for j in xrange(widthMat) ] for k in xrange(numMat) ]

#geracao da matriz e insercao no arquivo
arq = open("file.txt", "w")

genwrite_rand(arq)

arq.close()

#leitura da matriz do arquivo
arq = open("file.txt", "r")

get_from_file(mat, arq)

print "SAD = " + str(calc_SAD(mat))
print "SSE = " + str(calc_SSE(mat))

arq.close()
