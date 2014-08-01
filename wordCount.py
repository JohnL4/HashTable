#!/usr/bin/python3

import argparse
import re
import sys

from HashTable import HashTable

#text = open("20leagues.txt", "r")
#print(text.read())

parser = argparse.ArgumentParser( "Print frequency of words used in a text file.")
parser.add_argument( 'filenames', nargs='*')

args = parser.parse_args()

counter = 0

ht = HashTable()

# hashCode = ht._hashcode("abc")
# print( "hashed string to: ", hashCode)
# hashCode = ht._hashcode( ht)
# print( "hashed ht to: ", hashCode)

wordcount = 0

def process(line):
    global wordcount
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
            # print( "\"{0}\"\t".format( word), end="")
            wordcount += 1
            if (wordcount % 10000 == 0):
                print( "\t{0} words".format(wordcount), file=sys.stderr)
            if (ht.has(word)):
                ht.put(word, ht.get(word)+1)
            else:
                ht.put(word, 1)
        return len(words) - 1

i = 0
# with open('testtext.txt', 'r') as text:
for filename in args.filenames:
    with open(filename, 'r') as text:
        for line in text:
            counter += process(line.strip())
            #i += 1
            #if i > 100:
            #    break
        # else:
            # No more lines to be read from file
            # print(counter)
            # print()

# print( "Counts:")

for entry in ht.entries():
    if (entry == None):
        pass
    else:
        print( "{0}\t{1}".format(entry.value(), entry.key()))
    
print( "\t{0} words".format( ht.count()))
