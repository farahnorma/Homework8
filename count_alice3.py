# Norma
# H8-1: count_alice3.py:
#   Starting code => based on code from in-class L8-3
from collections import Counter
FILENAME = 'alice.txt'
fvar = open (FILENAME, 'r') # open file for reading
allwords = [] # accumulate the words in this list
for aline in fvar:
    aline = aline.lower()
    aline = aline.replace('--', ' ')
    for punct in '!"#$%&()*+,./:;<=>?@[]^_{|}~':
        aline = aline.replace(punct, ' ')
    words = aline.split() # splits the line on whitespace (blanks, '\n', '\t')

    allwords.extend(words) # add all words in this line to allwords

new_allwords = [] # accumulate the words in this list
for aline in allwords:
    aline = aline.lower()

    if len(aline) ==1:
        aline = aline.replace("'", " ")
    elif aline[:1] is "'" or aline[-1:] is "'":
            aline = aline.replace("'", ' ')
            aline = aline.replace("tis", "'tis")
    words = aline.split() # splits the line on whitespace (blanks, '\n', '\t')
    new_allwords.extend(words)


new_allwords.sort()
print (new_allwords)
print(Counter(new_allwords))
# sort the final word list


# Now use a dictionary to count each word in new_allwords...
# Start with the code from HTT12 Exercise 3 - but note our overall approach
# is different with respect to punctuation...

counts = {} # initialize counting dictionary to empt
if aline.isalpha():
    if aline in counts:
        counts[aline] = counts[aline] + 1
    else:
        counts[aline] = 1

new_allwords = counts.keys()
sorted(new_allwords)
out = open('alice_words.txt', 'w')

for word in new_allwords:
    out.write(word + " " + str(counts[word]))
    out.write('\n')




fvar.close()


