# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


###############################################################################
def maxDepthBFS(root):
    if not root:
        return 0

    level = 0
    q=deque([root])
    while q:
        initial_size=len(q)
        for i in range(initial_size):
            node=q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level+=1

    return level


###############################################################################
def maxDepthDFS(root):
    max_depth=0
    stack=[]
    if root:
        stack.append([root,1])

    while stack:
        node, depth = stack.pop()
        if node:
            if node.left:
                stack.append([node.left,depth+1])
            if node.right:
                stack.append([node.right,depth+1])
            max_depth=max(depth, max_depth)

    return max_depth


###############################################################################
def maxDepthRecursive(root):
        if not root:
            return 0

        return 1+max(maxDepthRecursive(root.left), maxDepthRecursive(root.right))
