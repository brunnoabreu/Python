def manip(outArq):

	inArq = open("out.txt","r")

	numLin = 0
	numWord = 0
	PSNR = ''
	bitRate = ''
	elapsedTime = ''
	for lines in inArq:
		numWord = 0
		if numLin == 45:
			for words in lines.split():
				if numWord == 2:
					bitRate = words
				elif numWord == 3:
					PSNR = words
				elif numWord >= 4 and numWord <= 5:
					PSNR = PSNR + '\t' + words
				numWord = numWord + 1
		elif numLin == 65:
			for words in lines.split():
				if numWord == 2:
					elapsedTime = words
				numWord = numWord + 1
		numLin = numLin + 1
	outArq.write(bitRate + '\t' + PSNR + '\t' + elapsedTime+ '\n')
	inArq.close()
