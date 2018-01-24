#License: GNU GPL 3.0 (2018) Ahmad Retha

import sys

if len(sys.argv) == 1:
	print 'Error: no filename given'
	sys.exit(1)

try:
	inDegSeg = False
	n = 0
	N = 0
	with open(sys.argv[1], 'r') as f:
		for line in f:
			for c in line:
				if c == '{':
					inDegSeg = True
				elif c == '}':
					inDegSeg = False
					n += 1
				elif c in ['A','C','G','T','N']:
					N += 1
					if not inDegSeg:
						n += 1
except IOError:
	print 'Error: could not access file'
	sys.exit(1)

print "n: %d, N: %d" % (n, N)

