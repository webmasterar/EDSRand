//License: GNU GPL 3.0 (2018) Fatima Vayani

/************************************************************************************/
/*******************************         README        ******************************/
/************************************************************************************/

/*************************************************************************************

PARAMETERS ---> EXAMPLES
- n : number of positions in text T ---> 1000000
- d% : percentage of positions in text T which are degenerate i.e. represent indels ---> 3
- S_max : maximum size of set at any position T[i] i.e. maximum number of S_j ---> 3
- L_max : upper bound on length of any string S_j in T[i] ---> 6
- o: desired name of output file ---> results.txt

The program takes the parameters and makes use of DNA (a vector of chars holding the DNA alphabet) in order to...
1. define an int vector D of random positions in T (totalling d% of T) which should be sets instead of singleton chars
2. from 0 to n-1:
	if pos in D then:
		createSet()
	else:
		pickRandomBase()
...where...
createSet():
1. set random s <= S_max (range begins from 2)
2. for each i in s, set random l <= L_max (range begins from 0, where 0 is epsilon)
3. pickRandomBase() l times, s times 
pickRandomBase():
1. randomNumberGenerator for int x = {0, 1, 2, 3}
2. return DNA[x]
*************************************************************************************/

/*************************************************************************************
To compile:
$ g++ synthesiseRandomEDS.cpp -o synthesise -std=c++11
To run:
$ ./synthesise -n <int> -d <int> -Smax <int> -Lmax <int> -o <string>
For example:
$ ./synthesise -n 30 -d 10 -Smax 5 -Lmax 5 -o result.txt
*************************************************************************************/

/************************************************************************************/
/*******************************        HEADERS        ******************************/
/************************************************************************************/

#include <iostream> 
#include <string> 
#include <vector> 
#include <fstream> 
#include <sstream>
#include <ctime>
#include <cstdlib> 
#include <cmath> 
#include <algorithm> 

/************************************************************************************/
/******************************* FUNCTION DECLARATIONS ******************************/
/************************************************************************************/

std::string pickRandomBase(std::vector<std::string> *dna);
std::string createSet(int *Smax, int *Lmax, std::vector<std::string> *dna);
bool check(std::string s, std::vector<std::string> sslist);

/************************************************************************************/
/*******************************         MAIN          ******************************/
/************************************************************************************/

int main(int argc, char* argv[])
{

/* user given parameters */

int n = atoi(argv[2]); 
int d = atoi(argv[4]); 
int Smax = atoi(argv[6]); 
int Lmax = atoi(argv[8]); 
std::string o = argv[10]; 

/* define DNA alphabet */
std::vector<std::string> dna = {"A", "G", "C", "T"};

/* set seed for random base generator */
std::srand(std::time(NULL));

/*
* build D
* (vector of random positions in T (equating to d% of T)
* which should be sets instead of singleton chars)
*/

std::vector<int> D;
float dprime = ceil( ( float(n) / 100 ) * d );
for (int i=0; i<dprime; i++){
	D.push_back( std::rand() % n );
}
std::sort(D.begin(), D.end());

/* build T */

std::ofstream file;
file.open(o);
for (int x=0; x<n; x++){
	if ( std::find(D.begin(), D.end(), x) != D.end() ){ //present in D
		file << createSet(&Smax, &Lmax, &dna);
	} else {
		file << pickRandomBase(&dna);
	}
}
file.close();

return 0;
}

/************************************************************************************/
/******************************* FUNCTION DEFINITIONS *******************************/
/************************************************************************************/

/******************************* CREATE DEG. POSITION *******************************/

std::string createSet(int *Smax, int *Lmax, std::vector<std::string> *dna)
{

/* set random s <= Smax (range begins from 2) */
int s = ( std::rand() % ( (*Smax) -1) ) + 2;
if (s >= (*Smax)) s=(*Smax);

std::vector<std::string> sslist;
std::stringstream Tistream;
Tistream << "{";
int i = 0;
while (i != s){
	std::stringstream ss;
	int l = std::rand() % (*Lmax);
	if (l==0){
		ss << "E";
	} else {
		for (int j = 0; j<l; j++) ss << pickRandomBase(dna);
	}
	if (check(ss.str(), sslist)==0){
		sslist.push_back(ss.str());
		Tistream << ss.str() << ",";
		i++;
	}
}
std::string Ti = Tistream.str();
Ti.pop_back();
Ti += "}";
return Ti;

}

/******************************* CHECK IF S_j ALREADY EXISTS *******************************/

bool check(std::string s, std::vector<std::string> sslist)
{
for (std::vector<std::string>::iterator it = sslist.begin(); it!=sslist.end(); it++){
	if (s==*it) return 1;
}
return 0;
}

/******************************* PICK RANDOM DNA BASE *******************************/

std::string pickRandomBase(std::vector<std::string> *dna)
{
int number = ( std::rand() % 4 );
return (*dna)[number];
}
