'''

Using regular expression methods
The "re" package provides several methods to actually perform queries on an input string.
re.match()
re.search()
re.findall()
Note: Based on the regular expressions, Python offers two different primitive operations. 
The match method checks for a match only at the beginning of the string 
while search checks for a match anywhere in the string.

'''

import re
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")    





some_text = "Hi there! Python is fun"

patterns = ['software testing', 'programming']
text = 'software testing is fun?'
for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
    if re.search(pattern, text):
        print('found a match!')
else:
    print('no match')

		
email_list = 'johndoe@gmail.com, jane@rediffmail.com, someone@yahoo.co.in'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', email_list)
for email in emails:
    print(email)
