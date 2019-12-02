sentence1 = 'row row row your boat gently ...'
sentence2 = 'The quick brown fox jump the fence...'

word_and_counts = dict()
words = sentence2.split()
print(words)
for single_word in words:
	if single_word in word_and_counts:
		word_and_counts[single_word] = word_and_counts[single_word] + 1
	else: 
		word_and_counts[single_word] = 1
	print(single_word)

print(word_and_counts)