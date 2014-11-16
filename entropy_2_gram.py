#!/usr/bin/python 
# -*- coding: UTF-8 -*-

import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    from sets import Set
import math
import re
with open ("newspapers.txt", "r") as myfile:
	st=myfile.read().decode('utf-8').replace('\n', '').replace(' ','')
	#st=re.sub(r"[A-Za-z0-9-.,=_;:?<\">?/|\}\{\[\]\n\+\*-~\r\'#()$%^`@&!\t ]","",st);
	#print 'Input string:'
	#print st
	print
	stList = list(st)
	regex=re.compile(ur'[\u0a00-\u0a7f]')
	stList=[i for i in stList if regex.search(i)]
	alphabet = list(Set(stList)) # list of symbols in the string
	
	print "Symbol Set Size: ",len(alphabet)ep
	print
	print 'Alphabet of symbols in the string:'
	print alphabet
	print
	ent = 0.0

	# calculate the frequency of each symbol in the string
	freqList = [0.0 for x in range(len(alphabet))]
	for sym in stList:
		freqList[alphabet.index(sym)]+=1.0;
	a= sum(freqList);
	alphabet_size=len(alphabet);
	for i in range(len(alphabet)):
		freqList[i]=freqList[i]/a
	print 'Frequencies of alphabet symbols:'
	print freqList
	#print "Sum",sum(freqList)
	# Shannon entropy
	
	for freq in freqList:
	    ent = ent + freq * math.log(freq, 2)
	ent = -ent
	print '1-gram Shannon entropy: ',ent
	print 'Minimum number of bits required to encode each symbol:',(math.ceil(ent))
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
	for i in range(len(alphabet)):
		for j in range(len(alphabet)):
				freqs[i][j]=freqs[i][j]/totalSum
				if(freqs[i][j]!=0):
					ent = ent + freqs[i][j] * math.log(freqs[i][j], 2)
	ent=-ent
	print '2-gram Shannon entropy: ',ent
	print 'Minimum number of bits required to encode each symbol: ',(math.ceil(ent))
	
