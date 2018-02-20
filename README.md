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

## SynthesiseRandomEDS

Generates a random Elastic Degenerate String (EDS) of size n, where degenerate positions count as 1.
To compile this program:

`g++ synthesiseRandomEDS.cpp -o synthesise -std=c++11`

And to run it:

`./synthesise -n <int> -d <int> -Smax <int> -Lmax <int> -o <string>`

The parameters that must be supplied are:

* -n    The size or number of positions in the ED string
* -d    The percentage of positions in the text which are degenerate
* -Smax The maximum size of the set at any degenerate position
* -Lmax The upper bound on length of any string in a degenerate position
* -o    The desired name of the output file

## getEDSsize

Also included is a little tool (getEDSsize) which you can use to find the number
of positions (n) and total size (N) of an EDS string (counting degenerate positions
as 1). Use it like so:

`python getEDSsize.py file.eds`

It will count DNA characters (including 'N') and print out the number of positions
(n) and total number of characters (N) in the EDS file. e.g.

`n: 9000, N:10000`

### License, e.t.c.

To create EDS files using genomic data (reference sequence + VCF file), please use the tool [EDSO](https://github.com/webmasterar/edso)

GNU GPL 3.0 (2018) Ahmad Retha and Fatima Vayani
