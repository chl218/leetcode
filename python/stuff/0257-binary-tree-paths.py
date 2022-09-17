"""
257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.



Example 1:

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:

Input: root = [1]
Output: ["1"]



Constraints:

    The number of nodes in the tree is in the range [1, 100].
    -100 <= Node.val <= 100


"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.path(root,'',res)
        return res

    def path(self,root,string,res):
        string += str(root.val)
        if root.left:
            self.path(root.left,string+'->',res)

        if root.right:
            self.path(root.right,string+'->',res)

        if not root.left and not root.right:
            res.append(string)