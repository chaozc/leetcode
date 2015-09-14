import os
import subprocess
fs = os.listdir('.')
for f in fs:
	if f != '.DS_Store':
		if len(f) < 7:
			nf = 'p'
			for i in range(7-len(f)):
				nf += '0'
			nf += f[1:]
			print nf
			subprocess.call(['mv', f, nf])