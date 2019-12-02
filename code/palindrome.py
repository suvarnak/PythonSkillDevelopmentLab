
word = input("Enter the word to be checked for palindrome")
word_list = [char for char in word] 
reverse_word = list(word_list)
reverse_word.reverse()
print(word_list)
print(reverse_word)
if(word_list == reverse_word):
	print("Palindrome!!!!")
else:
	print("Not a Palindrome!!!!")
