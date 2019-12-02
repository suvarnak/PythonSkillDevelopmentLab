'''
A regular expression in a programming language is a special text string used for
 describing a search pattern.
It is extremely useful for extracting information from text such as code, email ids, files,
 logs etc.
'''

import re
some_text = "Hi there! Python is fun"
r1 = re.findall(r"^\w+",some_text) 
print(r1)
r1 = re.findall(r"^\w+","text dds") 
print(r1)



#Example of \s expression in re.split function
r2= re.split(r"\s",some_text)
print(r2)

r3= re.split(r"s",some_text)
print(r3)

r4 = re.findall(r"[abc]","agdhfdcfvgff")
print(r4)	# prints ['a', 'c']