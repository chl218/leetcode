from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(self, root):
    """Maximum Depth of Binary Tree

    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the
    root node down to the farthest leaf node.

    Note: A leaf is a node with no children.
    """

    if not root:
        return 0

    return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)


def isValidBST(root: TreeNode) -> bool:
    """Validate Binary Search Tree

    Given a binary tree, determine if it is a valid binary search tree (BST).

    Assume a BST is defined as follows:
        - The left subtree of a node contains only nodes with keys less than the
          node's key.
        - The right subtree of a node contains only nodes with keys greater than
          the node's key.
        - Both the left and right subtrees must also be binary search trees.
    """

    def isValid(root, minNode, maxNode):
        if not root:
            return True

        if minNode and minNode.val >= root.val:
            return False

        if maxNode and maxNode.val <= root.val:
            return False

        return isValid(root.left, minNode, root) and \
               isValid(root.right, root, maxNode)

    return isValid(root, None, None)


 def isSymmetric(root: TreeNode) -> bool:
    """Symmetric Tree
     
    Given a binary tree, check whether it is a mirror of itself (ie, symmetric
    around its center).
    """
    def aux(leftNode, rightNode):
        if not leftNode and not rightNode:
            return True

        if leftNode and rightNode and leftNode.val != rightNode.val or \
            not leftNode and rightNode or \
            not rightNode and leftNode:
            return False

        return aux(leftNode.left, rightNode.right) and\
               aux(leftNode.right, rightNode.left)

    if not root:
        return True

    return aux(root.left, root.right)


def levelOrder(root: TreeNode) -> List[List[int]]:
    """Binary Tree Level Order Traversal

    Given a binary tree, return the level order traversal of its nodes' values.
    (ie, from left to right, level by level).
    """

    if not root:
        return []

    queue = [root]
    res = []
    while queue:
        nextQueue = []
        level = []
        for node in queue:
            level.append(node.val)
            if node.left:
                nextQueue.append(node.left)
            if node.right:
                nextQueue.append(node.right)

        res.append(level)
        queue = nextQueue

    return res


def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    """Convert Sorted Array to Binary Search Tree

    Given an array where elements are sorted in ascending order, convert it to a
    height balanced BST.

    For this problem, a height-balanced binary tree is defined as a binary tree
    in which the depth of the two subtrees of every node never differ by more
    than 1.
    """

    if not nums:
        return None

    mid = len(nums)//2

    lo = nums[:mid]
    hi = nums[mid+1:]

    node       = TreeNode(nums[mid])
    node.left  = self.sortedArrayToBST(lo)
    node.right = self.sortedArrayToBST(hi)

    return node

