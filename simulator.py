import os
import manip import organize
videos = ['BQSquare.cfg', 'RaceHorsesC.cfg', 'BasketballDrive.cfg']
QP = ['32']
CFG = ['encoder_lowdelay_main.cfg', 'random_acess.cfg']
frames = '9'

for video in videos:
	for qps in QP:
		for cfgs in CFG:
			for i in xrange(0,31):
				command = './TAppEncoderStatic -c ../cfg/' + cfgs + ' -c ../cfg/per-sequence/' + video + ' -f ' + frames + '--TZSearchConfig=' + i + '>out.txt'
				os.system(command)
				organize()
