#!/usr/bin/python
import math

#returns a sorted list of the prime numbers <= n (2 is the first prime number)
def primes(k):
	k1 = k+1
	primenumbers = [i for i in range(2,k1)]

	for i in primenumbers:
		factors = range(i, k1, i)
		for f in factors[1:]:
			if f in primenumbers:
				primenumbers.remove(f)
	return primenumbers

#returns two primes a and b with a<= b such that a + b = k or returns 0, 0 if no such primes exist.
def sumOfPrimes(limit):
	list=primes(limit)
	for i in list:
		for j in list:
			if j < i:
				continue
			if i + j ==limit:
				return(i,j)
	return(0,0)

#returns a list of all pairs (a, b) such that a and b are prime, a <=  b, and a + b = k.
def allSumOfPrimes(limit):
	list=primes(limit)
	allsum_list=[]
	for i in list:
		for j in list:
			if j<i:
				continue
			if i+j==limit:
				allsum_list.append((i,j))
	return allsum_list

#tests all the even integers <= k to see whether they can be written as the sum of 2 primes and returns a boolean value that is True if every even integer <= k isrepresented within the list, or False otherwise.
def goldbach(k):
	list=primes(k)
	evenlist=[i for i in range(4,k+1) if i%2==0]
	goldbach_list=[]
	check=True
	globalCheck = True
	for n in evenlist:
		check=False
		for i in list:
			for j in list:
				if j<i:
					continue
				if i+j==n:
					goldbach_list.append((n,i,j))
					check=True
		globalCheck=globalCheck & check
		
	
	return (goldbach_list,globalCheck)

# returns a list with all the even numbers which are expressed as sum of two primes
def goldbachWidthlist(k):
	list=primes(k)
	evenlist=[i for i in range(2,k+1) if i%2==0]
	
	list_n=[]
	count=0
	for n in evenlist:
		for i in list:
			for j in list:
				if j<i:
					continue
				if i+j==n:
					list_n.append(n)
	return list_n

# returns a list of even numbers and the number of ways they can be expressed as a sum of two primes. 
def goldbachWidthfreq(k):
	goldbach_list=goldbachWidthlist(k)
	goldbachfreq_list=[] 
	
	for i in goldbach_list:
		goldbachfreq_list.append((i,goldbach_list.count(i)))
	return goldbachfreq_list

#  dictionary (map) D such that D[z] is the number of ways each even number 2 < z ? k can be written as the sum of two primes.
def goldbachWidth(k):
	newlist=goldbachWidthfreq(k)
	dict_gb=dict(newlist)
	return dict_gb

					
def main():
    #main() function that calls these functions
	print primes(13)
	print sumOfPrimes(10)
	print allSumOfPrimes(48)
	print goldbach(10)
	print goldbachWidth(25)

if __name__ == "__main__": main() # call main if program run from command line
	
					
					





	


		



