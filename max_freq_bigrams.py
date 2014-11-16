#!/usr/bin/python 
# -*- coding: UTF-8 -*-

import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    from sets import Set
import math
import re
import sys
with open ("newspapers+blogs.txt", "r") as myfile:
	st=myfile.read().decode('utf-8').replace('\n', '').replace(' ','')
	#st=re.sub(r"[A-Za-z0-9-.,=_;:?<\">?/|\}\{\[\]\n\+\*-~\r\'#()$%^`@&!\t ]","",st);
	#print 'Input string:'
	#print st
	print
	stList = list(st)
	regex=re.compile(ur'[\u0a00-\u0a7f]')
	stList=[i for i in stList if regex.search(i)]
	alphabet = list(Set(stList)) # list of symbols in the string
	
	print "Symbol Set Size: ",len(alphabet)
	print
	print 'Alphabet of symbols in the string:'
	print alphabet
	print
	freqs=[[0.0 for x in range(len(alphabet))] for y in range(len(alphabet))]
	#freqs stores frequencies in form of a 2d array
	#a[i][j]=200 means symbol at j in alphabet occurs 200 times after symbol at i in alphabet
	prev=None;
	current=None;
	totalSum=0.0;
	for sym in stList:
		current=sym;
		if(prev!=None):
			prev_index=alphabet.index(prev)
			#print prev_index
			curr_index=alphabet.index(current)
			freqs[prev_index][curr_index]+=1
			totalSum+=1.0
		prev=current
	max_val=0
	maxi=[0,0]
	for x in range(100):
		max_val=0
		for i in range(len(alphabet)):
			for j in range(len(alphabet)):
				if max_val<freqs[i][j]:
					max_val=freqs[i][j]
					maxi=[i,j]
		sys.stdout.write(alphabet[maxi[0]])
		sys.stdout.write(alphabet[maxi[1]])
		print " : ",max_val
		freqs[maxi[0]][maxi[1]]=0.0
		
