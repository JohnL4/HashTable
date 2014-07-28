#!/usr/bin/python3

import re
from HashTable import HashTable

#text = open("20leagues.txt", "r")
#print(text.read())

counter = 0

ht = HashTable()

def process(line):
    if re.match(r"CHAPTER [IVXLCDM]+$", line):
        return 0
    elif re.match(r"PART [A-Z]+$", line):
        return 0
    elif re.match(r"\n+", line):
        return 0
    else:
        #Split strings like this:
        #   he said "argh (my leg hurts!)," and then he left -- never to return
        words = re.split(r"[.!()\"',:?\-\n ]+", line)
        for word in words:
            ht.put(word, 0)
        return len(words) - 1

i = 0
with open('testtext.txt', 'r') as text:
    for line in text:
        counter += process(line)
        #i += 1
        #if i > 100:
        #    break
    else:
        # No more lines to be read from file
        print(counter)
