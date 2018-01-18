## EDSRand

Generate a random Elastic Degenerate String (EDS) using the DNA alphabet. This
program runs under Python 2.7 and requires the Numpy package to be installed too.

Usage example:

`python EDSRand.py 100`

This creates an EDS with total size N = 100.

`ATCGATGGG{T,C}AACTT{T,G}AG{G,T}CCGGTTTATATTGAT{T,C}CCTA{T,G}{T,A}{A,T}A{T,A}GGGGGTCCTTTGCTTGCTGTTG{A,G}CTC{T,G}TGAGTGAGCTTGCGAGATA`

N is the only required parameter of the program.

Optional parameters include:

* --P_deg The maximum percentage of positions in the sequence that are degenerate (default=10)
* --P_eps The maximum percentage of degenerate segments to contain Epsilon (default=0)
* --S_max The maximum size (number of strings) in a degenerate segment (default=2)
* --L_max The maximum length of each string in a degenerate segment (default=1)

## findEDSN

Also included is a little tool (findEDSN) which you can use to find the total size
of an EDS string. Use it like so:

`python findEDSN.py file.eds`

It will print out N.

### License

GNU GPL 3.0 (2018) Ahmad Retha
