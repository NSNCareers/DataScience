import  re

text_to_search = '''
348-763-998
847.498.095
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'^Start') # Finds the Start at the begenning of the sentence
# pattern = re.compile(r'end$') # finds a match at the end 
pattern = re.compile(r'\d\d\d') # Back slash d will match any digit
sentence = 'Start a sentence and then bring it to an end'

matches = pattern.finditer(text_to_search)

for  x in matches:
    print(x)
    