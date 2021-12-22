class Graph:
    def __init__(self,dict=None):
        if dict is None:
            dict = {}
        self.dict =dict

    def addEdge(self,vertex,edge):
        self.dict[vertex].append(edge)

    def bfs(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            deque_vertex=queue.pop(0)
            print(deque_vertex)
            for adjacentVertex in self.dict[deque_vertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
        return visited
    def dfs(self,vertex):
        visited=[vertex]
        stack=[vertex]
        while stack:
            popped_vertex=stack.pop()
            print(popped_vertex)
            for adjacentVertex in self.dict[popped_vertex]:
                if adjacentVertex not in visited:
                    stack.append(adjacentVertex)
                    visited.append(adjacentVertex)






# dict1={'a':['b','c'],
#         'b':['a','d','e'],
#         'c':['a','e'],
#         'd':['b','e','f'],
#         'e':['d','f'],
#         'f':['d','e']
#       }

dict1={'a':['b','c'],
        'b':['a','d','e'],
        'c':['a','e'],
        'd':['b','e','f'],
        'e':['d','f','c'],
        'f':['d','e']
      }



graph=Graph(dict1)
print(graph.dict)
#add edge from c to e
graph.addEdge('e','c')
print(graph.dict)
print(graph.bfs("a"))
print(graph.dfs("a"))

