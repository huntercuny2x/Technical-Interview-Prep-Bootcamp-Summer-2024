def lowestCommonAncestor(root, p, q):
    while True:
        if root.val > p.val and root.val > q.val:
            root = root.left

        elif root.val < p.val and root.val < q.val:
            root = root.right

        else:
            return root
