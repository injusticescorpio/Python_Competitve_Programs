li={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,
    'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
s=input()
rev=s[::-1]
res=[rev[i] for i in range(len(s)//2)]
res1=[s[i] for i in range(len(s)//2)]
print(res)
print(res1)
c=0
for i in range(len(res)):
    c+=li[res[i]]-li[res1[i]]
print(c)