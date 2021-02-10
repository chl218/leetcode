# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is
# changed to the original key plus sum of all keys greater than the original key in BST.
#
# Example 1:
# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
#
# Example 2:
# Input: root = [0,null,1]
# Output: [1,null,1]
#
# Example 3:
# Input: root = [1,0,2]
# Output: [3,3,2]
#
# Example 4:
# Input: root = [3,2,4,1]
# Output: [7,9,4,10]
#
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

      self.val = 0

      def traverse(root: TreeNode):
         if root:
            traverse(root.right)

            root.val += self.val
            self.val = root.val

            traverse(root.left)

      traverse(root)
      return root
