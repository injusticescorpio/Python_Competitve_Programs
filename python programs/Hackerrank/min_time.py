files1=[3,1,5]
core=1
limit=5
file=sorted(files1,reverse=True)
print(file)
i=0
while(i<len(file) and limit!=0):

    if file[i]%core==0:
        file[i]=file[i]//core
    i+=1
    limit-=1
print(file)
print(sum(file))