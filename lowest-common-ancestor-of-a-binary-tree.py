# http://www.cnblogs.com/grandyang/p/4641968.html


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
	# note: if only one node exists in the subtree at root, the lowestCommonAncestor returns that node
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root == p or root == q:
            return root

# 注意，lowestCommonAncestor函数在这里还有另一个功能，那就是如果p和q只有一个在左子树，函数也返回找到的结点，
# 尽管这个结点并不是lowestCommonAncestor
        nodeInLeftTree = self.lowestCommonAncestor(root.left, p, q)
        nodeInRightTree = self.lowestCommonAncestor(root.right, p, q)

        if nodeInLeftTree and nodeInRightTree:
            return root
        if nodeInLeftTree:
            return nodeInLeftTree
        else:
            return nodeInRightTree


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root == p or root == q:
            return root

        nodeInLeftTree = self.lowestCommonAncestor(root.left, p, q)
        nodeInRightTree = self.lowestCommonAncestor(root.right, p, q)

        if nodeInLeftTree and (nodeInLeftTree != p and nodeInLeftTree != q):
            return nodeInLeftTree

        if nodeInLeftTree and nodeInRightTree:
            return root
        if nodeInLeftTree:
            return nodeInLeftTree
        else:
            return nodeInRightTree

