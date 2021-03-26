holder = 0
wordcount = 0
holder = float(holder)
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        numb= float(line[20:26])
        holder= holder+numb
        wordcount= wordcount + 1

print("Average spam confidence:",holder/wordcount)
