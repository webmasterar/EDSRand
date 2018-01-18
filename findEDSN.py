#License: GNU GPL 3.0 (2018) Ahmad Retha

import sys

if len(sys.argv) == 1:
	print 'Error: no filename given'
	sys.exit(1)

try:
	i = 0
	with open(sys.argv[1], 'r') as f:
		for line in f:
			for c in line:
				if c in ['A','C','G','T']:
					i += 1
except IOError:
	print 'Error: could not access file'
	sys.exit(1)

print i
