fname = input("Enter file name: ")
fh = open(fname)
blanklist= list()
for filetxt in fh:
    list_of_words=filetxt.split()
    for words in list_of_words:
        if words not in blanklist:
            blanklist.append(words)
nowfilledlist= blanklist 
print(sorted(nowfilledlist))
