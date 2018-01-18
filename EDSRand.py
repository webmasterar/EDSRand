#License: GNU GPL 3.0 (2018) Ahmad Retha

import sys
import argparse
import numpy.random as rnd

##
# Given the size of the text and number of degenerate segments required, it
# returns a sorted list of indexes to place degenerate positions at
#
# @param n size of sequence
# @param nds number of degenerate segments
# @return sorted list of positions
#
def getDegPositions(n, nds):
	positions = rnd.choice(n, nds, replace=False)
	return sorted(list(positions))

##
# Creates a degenerate segment
#
# @param S_max Maximum size of list (2 to S_max strings in a segment)
# @param L_max Maximum length of any string in the degenerate segment
# @param epsilon Include the epsilon char 'E' representing a deleted segment?
# @return A degenerate segment
#
def getDegSeg(S_max, L_max, epsilon=False):
	S = []
	lim = rnd.randint(2, S_max+1)
	while len(S) < lim:
		rndSeq = getRandSeq(rnd.randint(1, L_max+1))
		if rndSeq not in S:
			S.append(rndSeq)
	if epsilon:
		S.append('E')
	return S

##
# Get a random DNA sequence of a specified size
#
# @param size The number of bases
# @return A random DNA string with _size_ bases
#
def getRandSeq(size):
	if size <= 0:
		return ''
	dna = ['A','C','G','T']
	arr = [dna[i] for i in rnd.randint(4, size=size)]
	return ''.join(arr)

##
# Get segment size (N)
#
# @param S A segment
# @return The number of characters in the segment (excluding epsilon)
#
def getSegSize(S):
	if type(S) == 'string':
		return len(S)
	total = 0
	for s in S:
		if s == 'E':
			continue
		total += len(s)
	return total

def main():
	#
	# Parse command line arguments and check input
	#
	parser = argparse.ArgumentParser(description='Generate a random DNA Elastic Degenerate String (EDS)')
	parser.add_argument('N', type=int, help='The total size of the EDS')
	parser.add_argument('--P_deg', type=int, default=10, help='The maximum percentage of positions in the sequence that are degenerate (default=10)')
	parser.add_argument('--P_eps', type=int, default=0, help='The maximum percentage of degenerate segments to contain Epsilon (default=0)')
	parser.add_argument('--S_max', type=int, default=2, help='The maximum size (number of strings) in a degenerate segment (default=2)')
	parser.add_argument('--L_max', type=int, default=1, help='The maximum length of each string in a degenerate segment (default=1)')
	args = parser.parse_args()

	if args.N < 10:
		print 'N is too short!'
		sys.exit(1)
	if args.P_deg < 0 or args.P_deg > 100:
		print 'Invalid percentage of degenerate segments'
		sys.exit(1)
	if args.P_eps < 0 or args.P_eps > 100:
		print 'Invalid percentage of epsilon in degenerate segments'
		sys.exit(1)
	if args.S_max < 2:
		print 'Invalid degenerate segment size'
		sys.exit(1)
	if args.L_max < 1:
		print 'Invalid string length for a degenerate segment'
		sys.exit(1)

	#
	# Create degenerate segments
	#
	nN = args.N
	numDegSegsToMake = int(float(nN)*(float(args.P_deg)/100.0))
	epsilonNumber = int(float(numDegSegsToMake) * float(args.P_eps)/100.0)
	shouldShuffle = epsilonNumber > 0
	degSegs = []
	segsN = 0
	for i in range(numDegSegsToMake):
		if epsilonNumber > 0:
			epsilon = True
			epsilonNumber -= 1
		else:
			epsilon = False
		S = getDegSeg(args.S_max, args.L_max, epsilon)
		Ssize = getSegSize(S)
		if segsN + Ssize > nN:
			break
		segsN += Ssize
		degSegs.append(S)
	n = max(nN - segsN, len(degSegs))
	if shouldShuffle:
		rnd.shuffle(degSegs)
	positions = getDegPositions(n, len(degSegs))

	#
	# Print out the EDS
	#
	i = 0
	seq = []
	numDegSegs = len(degSegs)
	while i < n and len(positions) > 0:
		if i == positions[0]:
			seq.append('{' + ','.join(degSegs[0]) + '}')
			del positions[0]
			del degSegs[0]
			i += 1
		else:
			strLen = positions[0] - i
			seq.append(getRandSeq(strLen))
			i += strLen
	seq.append(getRandSeq(n + numDegSegs - i))
	print ''.join(seq)

if __name__ == '__main__':
	main()
