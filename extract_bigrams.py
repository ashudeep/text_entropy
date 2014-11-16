from sets import Set
with open ("newspapers+blogs.txt", "r") as myfile:
	list_of_words=myfile.read().replace('.',' ').replace('\n',' ').replace('  ',' ').split(' ')
	#print Set(list_of_words)
	list_of_unigrams=list(Set(list_of_words))
	bigram_freqs=[[0 for x in range(len(list_of_unigrams))] for y in range(len(list_of_unigrams))]
	print list_of_unigrams,list_of_words
	for word in list_of_unigrams:
		for j in [i for i, x in enumerate(list_of_words) if x == word]:
			if j==len(list_of_words)-1:
				continue
			#print j,len(list_of_words)
			next_word=list_of_words[j+1]
			bigram_freqs[list_of_unigrams.index(word)][list_of_unigrams.index(next_word)]+=1
	for x in range(len(list_of_unigrams)):
		for y in range(len(list_of_unigrams)):
			if bigram_freqs[x][y]!=0:
				print list_of_unigrams[x],list_of_unigrams[y],bigram_freqs[x][y]
		
	
