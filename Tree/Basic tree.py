#create basic tree
class Tree:
    def __init__(self,data,children=[]):
        self.data = data
        self.children=children

    def __str__(self,level=0):
        r=' '*level+str(self.data)+"\n"
        # # r=self.data
        # print(f"r=={r} and level=={level}")
        # print(f"self.children=={self.children}")
        for child in self.children:
            r+=child.__str__(level+1)
        return r
    def print(self,level=0):
        r = ' '*level+ str(self.data) + "\n"
        for child in self.children:
            r+=child.print(level+1)
        return r
        
    def add_child(self,TreeNode):
        self.children.append(TreeNode)


tree=Tree('Drinks',[])
cold=Tree('Cold',[])
hot=Tree('Hot',[])
tree.add_child(cold)
tree.add_child(hot)
# print(tree)
#children of Hot node
tea=Tree('Tea',[])
coffee=Tree('coffee',[])
soup=Tree('soup',[])
#children of Cold node
pepsi=Tree('Pepsi',[])
redbull=Tree('Redbull',[])
coca_cola=Tree('Coca_cola',[])
hot.add_child(tea)
hot.add_child(coffee)
hot.add_child(soup)

cold.add_child(pepsi)
cold.add_child(redbull)
cold.add_child(coca_cola)

print(tree)
print('###')
print(tree.print())