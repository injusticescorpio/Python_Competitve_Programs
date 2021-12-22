a=[1,2,3]
for i in range(2):
    a.insert(0,a.pop())
print(a)