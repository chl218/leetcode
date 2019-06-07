class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(self, root):
    if not root:
        return 0

    return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)


def isValidBST(self, root: TreeNode) -> bool:
    def isValid(root, minNode, maxNode):
        if not root:
            return True

        if minNode and minNode.val >= root.val:
            return False

        if maxNode and maxNode.val <= root.val:
            return False

        return isValid(root.left, minNode, root) and isValid(root.right, root, maxNode)

    return isValid(root, None, None)

