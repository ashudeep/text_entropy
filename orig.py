#!/usr/bin/python 
# -*- coding: UTF-8 -*-

import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    from sets import Set
import math
import re
with open ("newspapers.txt") as myfile:
	st=myfile.read()
	st=st.replace('\n', '')
	st=st.replace(' ','');
	st=re.sub(r"[A-Za-z0-9-.,=_;:?<\">?/|\}\{\[\]\n\+\*-~\r\'#()$%^`@&!\t]","",st);
	#st=re.sub(r"\\x","",st)
	st=st.decode('utf-8')
	print
	stList = list(st)
	#alphabet = list(Set(stList)) # list of symbols in the string
	#regex=re.compile(r'\\x')
	#alphabet=[i for i in alphabet if not regex.search(i)]
	#print 'Alphabet of symbols in the string:'
	#print alphabet
	#print len(alphabet)
	alphabet =[u'\u0a00', u'\U00100083', u'\u0902', u'\u10e6', u'\u0906', u'\u0a08', u'\u090a', u'\u200c',  u'\u0a10',  u'\u2202', u'\u0a14',  u'\u0916', u'\u0a18', u'\u091a', u'\u1e6f', u'\u0a1c', u'\u1e0f', u'\u0a20',  u'\u255a', u'\u0a24', u'\uf0a7', u'\u0926', u'\u0a28',  u'\u092a', u'\u202c',  u'\u092e', u'\u0a30', u'\u0932', u'\uf034',  u'\u03b9', u'\u0a38',  u'\u0a3c', u'\u0abf', u'\u093e', u'\u0a40',  u'\u0942',  u'\u0a48', u'\u2502', u'\u202d', u'\u0a4c', u'\u2606',  u'\u0152', u'\u0454',  u'\u200e', u'\u0a5c',  u'\u25ba', u'\u2020',  u'\u2010', u'\u0a68', u'\u0966', u'\u0a6c', u'\uf0ef', u'\u256e', u'\u0a70', u'\u0a74',  u'\uf02b', u'\u06be', u'\ufffd', u'\u0aff', u'\u2014', u'\u0101', u'\u0941', u'\u0a03', u'\u096a', u'\u0905', u'\uf02e', u'\u0a07', u'\u0909', u'\u0713', u'\u200b', u'\u0a0f', u'\u096c',  u'\u2013', u'\u2192', u'\u0915',  u'\u0a17', u'\u2018', u'\u0a98', u'\u0a1b', u'\u091d', u'\u0a1f',  u'\u0921', u'\u0aa0', u'\u0a23', u'\u201a', u'\u0925', u'\u0aa4', u'\u0a27', u'\u0abd', u'\u0a2b', u'\u092d',  u'\u0a2f', u'\u201c',  u'\u0a33', u'\u0935',  u'\u1e47', u'\u0939',  u'\u201e',  u'\u0a3f', u'\u2741',  u'\u0641', u'\u0af7', u'\u0a47', u'\uf020', u'\u0149', u'\u0a4b', u'\u094d', u'\u2551',  u'\u2022', u'\u094c',  u'\u0a5b', u'\u262c',  u'\u0965', u'\u0a67', u'\u0969', u'\u0a6b', u'\u2026', u'\u096d', u'\u0aec', u'\u0a6f', u'\U001000a9', u'\u0a73', u'\ufeff', u'\uf028', u'\u0a7f', u'\u0a02', u'\u0a06', u'\u0908', u'\u0a0a', u'\u0ab2', u'\u0a2c', u'\u0a91', u'\u0910', u'\U00100082', u'\u2714', u'\u0a16', u'\u0a99', u'\u0918', u'\uf0d8', u'\u0a1a', u'\u091c', u'\u0a1e',  u'\u0920', u'\u0a22',  u'\u0924', u'\u0a26', u'\u06a9', u'\u0928', u'\u25ab', u'\u0a2a', u'\u092c', u'\u0a2e',  u'\u0930', u'\u0a32', u'\u0442', u'\u0a36', u'\u0938',  u'\u093c', u'\u0a3e', u'\u2740', u'\u03c3', u'\u0a42', u'\u2033', u'\u1e5b', u'\u0948',  u'\u1e14', u'\u25cf',  u'\u2550', u'\u200f', u'\u0a56', u'\u2032', u'\u0a5a', u'\u095c', u'\u0a5e', u'\u0964', u'\u0a66', u'\u0968', u'\u0a6a', u'\u0a13', u'\u0a6e', u'\u10f1', u'\u0970', u'\u0a72',  u'\u016b', u'\u067e', u'\u0a01', u'\u0903', u'\u0a82', u'\u0a05', u'\u0117', u'\u0907', u'\u0940', u'\u0a09', u'\u2588', u'\u090b', u'\u1e96', u'\u200d', u'\u258c', u'\u090f', u'\u2011', u'\u2019', u'\u0913',  u'\u0a15', u'\uf06f', u'\u0917',  u'\u0a19', u'\u091b', u'\u0a9a', u'\u0a1d', u'\u201b', u'\u091f', u'\u0a21', u'\u0923',  u'\u0a25', u'\u0927',  u'\uf029', u'\u201d', u'\u012b', u'\u0a2d', u'\u25ac', u'\u092f',  u'\u0a35',  u'\u0a39', u'\u0aba', u'\u093f', u'\u0af4', u'\u0a41', u'\u043c', u'\u0943',  u'\u0947', u'\u02c6', u'\u094b', , u'\u0a4d', u'\u25cc',  u'\u0a51', u'\u0153',  u'\u0a59', u'\u0e51', u'\u215f', u'\u2661', u'\u2665', u'\u0967',  u'\u0a69', u'\u096b', u'\u0a6d', u'\u093d', u'\u096f', u'\u2570', u'\u0a71',  u'\u0af6',  u'\u0a7d', u'\u092b', u'\u201f' ]
	print 'Alphabet of symbols in the string:'
	print alphabet
	print len(alphabet)
	print
	
	# calculate the frequency of each symbol in the string
	freqList = []
	for symbol in alphabet:
	    ctr = 0
	    for sym in stList:
		if sym == symbol:
		    ctr += 1
	    freqList.append(float(ctr) / len(stList))
	print 'Frequencies of alphabet symbols:'
	print freqList
	print
	# Shannon entropy
	ent = 0.0
	for freq in freqList:
	    ent = ent + freq * math.log(freq, 2)
	ent = -ent
	print 'Shannon entropy:'
	print ent
	print 'Minimum number of bits required to encode each symbol:'
	print int(math.ceil(ent))
