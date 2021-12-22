class graph:
    def __init__(self,dict1):
        if dict1 is None:
            dict1 = {}
        else:
            self.dict1 = dict1
    def dfs(self,vertex):
        stack=[vertex]
        visited=[vertex]
        while stack!=[]:
            popped=stack.pop()
            print(popped,end=' ')
            for i in self.dict1[popped]:
                if i not in visited:
                    stack.append(i)
                    visited.append(i)

dict1={
    1:[2,3],
    2:[1,4],
    3:[1,4],
    4:[2,3]
}
g=graph(dict1)
g.dfs(1)
        