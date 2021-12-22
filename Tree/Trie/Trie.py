class TrieNode:# Time and space complexity is O(1) 
    def __init__(self):
        self.children={}
        self.endofstring=False
        
class Trie: #Time and complexity is O(n)
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        current=self.root
        for i in word:
            ch=i
            node=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            # print(current.children)
            current=node
        current.endofstring=True
        print("successfully inserted")
    def search(self,word):
        current=self.root
        for i in word:
            node=current.children.get(i)
            if node==None:
                return False
            current=node
        if current.endofstring==True:
            return True
        else:
            return False
def delete_string(root,word,index):
    print(f"index=={index}")
    ch=word[index]
    currentnode=root.children.get(ch)
    print(f"currentnode=={currentnode.children}")
    can_this_node_be_delete=False

    if len(currentnode.children)>1:#case 1 refer video for case
        print(f"case1")
        delete_string(currentnode,word,index+1)
        return False
    if index==len(word)-1:#case 2
        print(f"case2.1")
        if len(currentnode.children)>=1:
            print(f"cases")
            currentnode.endofstring=False
            return False
        else:
            print("case2.2")
            root.children.pop(ch)
            return True
    if currentnode.endofstring==True:
        print("case3")
        delete_string(currentnode,word,index+1)
        return False
    can_this_node_be_delete=delete_string(currentnode,word,index+1)#case 4
    if can_this_node_be_delete==True:
        print("case4")
        root.children.pop(ch)
        return True
    else:
        return False





trie=Trie()
trie.insert("Api")
trie.insert("Apple")
delete_string(trie.root,'Apple',0)
print(trie.search("Apple"))
