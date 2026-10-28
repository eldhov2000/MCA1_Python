from more_itertools.more import countable
def word_count(str):
    counts=dict()
    words=str.split()
    for word in words:
     if word in counts:
        counts[word]+=1
     else:
        counts[word]=1

    return counts
print(word_count("the quik brown for jumps i over the lazy dog:"))