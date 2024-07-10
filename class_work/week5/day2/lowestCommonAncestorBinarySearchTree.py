def lowestCommonAncestor(root, p, q):
    if root is None:
        return None

    if root.val == p.val or root.val == q.val:
        return root

    left_lca = lowestCommonAncestor(root.left, p, q)
    right_lca = lowestCommonAncestor(root.right, p, q)
    print(left_lca, right_lca)

    if left_lca and right_lca:
        return root

    return left_lca or right_lca