l=[1,2,3]
p=[]
def insert_operation(data,index):
    c=0
    for i in range(0,len(l)):
        if i==index:
            p.append(data)
            break
        else:
            p.append(l[i])
            c+=1
    print(f"p=={p}")
    for i in range(c,len(l)+1):
        if i==index:
            p.append(data)
            break
        p.append(l[i])
    print(f"p=={p}")

insert_operation(5,3)




