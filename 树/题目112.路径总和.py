

'''
    题目：

        给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
        说明: 叶子节点是指没有子节点的节点。
        示例:
                给定如下二叉树，以及目标和 sum = 22，

                              5
                             / \
                            4   8
                           /   / \
                          11  13  4
                         /  \      \
                        7    2      1
                返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

'''
#  这里直接使用 递归方法吧，一行搞定   当递归到子树时满足root.val==sum  说明寻找成功
#  时间复杂度 O(N)  空间复杂度最坏为O(N)
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool

        从右往左  看即可
        """
        return False if not root else root.val==sum if not root.left and not root.right else self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)


