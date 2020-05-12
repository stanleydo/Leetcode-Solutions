"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    @staticmethod
    def kthSmallest(root: TreeNode, k: int) -> int:

        tree = []
        tree.append(root)

        vals = []

        while tree:
            curnode = tree.pop(0)
            vals.append(curnode.val)

            if curnode.left:
                tree.append(curnode.left)
            if curnode.right:
                tree.append(curnode.right)

        set_of_vals = set(vals)
        sort_to_list = sorted(list(set_of_vals))

        return sort_to_list[k-1]


if __name__ == '__main__':

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(1)

    print(Solution.kthSmallest(root, 1))
