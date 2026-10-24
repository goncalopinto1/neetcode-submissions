
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque, defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        created = defaultdict(list)
        queue = deque([])

        if not node:
            return None
            
        # criar copia do node de entrada
        novo = Node(node.val)
        created[node.val] = novo
        queue.appendleft(node) # na queue vao os originais

        while len(queue) > 0:
            val = queue.pop()
            v = val.val
            n = val.neighbors

            for neighbor in n:
                if neighbor.val not in created:
                    new = Node(neighbor.val)
                    created[neighbor.val] = new
                    created[v].neighbors.append(new)
                    queue.appendleft(neighbor)
                else:
                    created[v].neighbors.append(created[neighbor.val])
                
        
        return novo

