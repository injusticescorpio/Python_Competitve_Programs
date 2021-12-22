alpha = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

s = input().strip()
n = int(input().strip())
scores = set()
ctr=1
for i in range(len(s)):
    score = alpha[s[i]]
    ctr = ctr+1 if (i+1 != len(s) and s[i+1] == s[i]) else 1
    scores.add(score*ctr)

for a0 in range(n):
    x = int(input())
    print("Yes" if x in scores else "No")


