"""
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    @staticmethod
    def findSecondMinimumValue(root: TreeNode) -> int:

        tree = []
        tree.append(root)

        values = []

        while (tree):
            curnode = tree.pop(0)
            values.append(curnode.val)

            if curnode.left:
                tree.append(curnode.left)
            if curnode.right:
                tree.append(curnode.right)

        set_of_values = set(values)

        if len(set_of_values) < 2:
            return -1
        else:
            return sorted(list(set_of_values))[1]


if __name__ == '__main__':

    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    print(Solution.findSecondMinimumValue(root))
