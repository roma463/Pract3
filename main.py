from File import xy 
import re


new_phrase = ''
for letter in xy[0]:
    if letter in 'AEIOUаоуыэею':
        new_phrase += letter.upper()
    else:
        new_phrase += letter.lower()

ouf = open(xy[1], "w")
ouf.write(new_phrase)
ouf.close