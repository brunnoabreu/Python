import os
from manip import manip

outArq = open("arqf.csv", "w")
outArq.write('Nr of Frames' + '\t' + 'Config' + '\t' + 'Video' + '\t' + 'QP' + '\t' + 'TZSearchConfig' + '\t' + 'Bit Rate' + '\t' + 'Y-PSNR' + '\t' + 'U-PSNR' + '\t' + 'V-PSNR' + '\t' + 'Total Time' +  '\n')
videos = ['Traffic', 'BasketballDrive', 'BQMall', 'BlowingBubbles']
QP = ['32', '37']
CFG = ['encoder_randomaccess_main.cfg', 'encoder_lowdelay_main.cfg']
frames = ['9']

for cfgs in CFG:
	for video in videos:
		for qps in QP:
			for frame in frames:
				for i in xrange(0,32):
					command = '~/hm-brunno/bin/TAppEncoderStatic -c ~/hm-brunno/cfg/' + cfgs + ' -c ~/hm-brunno/cfg/per-sequence/' + video + '.cfg' + ' -f ' + frame + '--TZSearchConfig=' + str(i) + '>out.txt'
					outArq.write(frame + '\t' + cfgs + '\t' + video + '\t' + qps + '\t' + str(i) + '\t')
					os.system(command)
					manip(outArq)
outArq.close()
