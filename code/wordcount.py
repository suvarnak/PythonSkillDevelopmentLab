sentence1 = 'the quick brown fox jumps over the lazy dog.'
sentence2 = 'row hey      row row your boat gently down the stream.'

counts = dict()
words = sentence2.split()
print(words)
for word in words:
		if word in counts:
				counts[word] += 1
		else:
				counts[word] = 1
print(counts)
