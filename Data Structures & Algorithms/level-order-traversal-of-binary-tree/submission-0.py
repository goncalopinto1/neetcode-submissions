# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res_dict = defaultdict(list)
        queue = deque([])

        queue.appendleft(root)

        level = 0

        while queue:
            for _ in range(len(queue)):

                node = queue.pop()

                if node:
                    res_dict[level].append(node.val)
                    queue.appendleft(node.left)
                    queue.appendleft(node.right)
            level += 1
        
        return [x for x in res_dict.values()]

        
