import string

def designerPdfViewer(h, word):
    d={}
    for i,j in zip(string.ascii_lowercase,h):
        d[i]=j
    print(d)
    prod=1
    maximum=0
    for i in word:
        if maximum<d[i]:
            maximum=d[i]

    print(len(word)*maximum)
h=list(map(int,input().split(' ')))
word=input()
designerPdfViewer(h, word)

