# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个二叉树，找出其最大深度。

            二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

            说明: 叶子节点是指没有子节点的节点。

            示例：
            给定二叉树 [3,9,20,null,null,15,7]   返回的最大深度为3
                            3
                           / \
                          9  20
                            /  \
                           15   7
      分析：

      思路：基本思路分为两种吧， 递归和非递归（层次遍历）两种 形式。

'''

# 首先说下 递归法

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))




# 第二种是非递归的迭代方式， 把每个结点及其深度作为一条记录，使用栈来存储记录。
class Solution1:
    """
    迭代法
    """
    def maxDepth(self, root):
        stack = []                                              # 定义一个空栈，栈中的元素是结点及其对应的深度
        if root:                                                # 如果根结点不为空
            stack.append((root, 1))                             # 则将根节点及其对应深度1组成的元组入栈
        max_depth = 0                                           # 初始化最大深度为零
        while stack:                                            # 当栈非空时
            tree_node, cur_depth = stack.pop()                  # 弹出栈顶结点及其对应的深度
            if tree_node:                                       # 如果该结点不为空
                max_depth = max(max_depth, cur_depth)           # 更新当前最大深度，如果该结点深度更大的话
                stack.append((tree_node.left, cur_depth+1))     # 将该结点的左孩子结点及其对应深度压入栈中
                stack.append((tree_node.right, cur_depth+1))    # 将该结点的右孩子结点及其对应深度压入栈中
        return max_depth


#___________________________________    练习1   ______________________________#
#  这里使用递归法， 简直不要太简单。
def fun1(root):
    if root==None:
        return 0
    else:
        #  深度增加    非常简单的计算。
        return 1+max(fun1(root.left),fun1(root.right))



# 非递归方法 是使用栈的方式。   直接压栈，弹栈 做DFS搜索 和深度判别即可。
def fun2(root):
    stack=[]

    if root:
        stack.append((root,1))  # 栈内两个元素，分别是 指针和 深度值

    #最大深度统计
    max_depth=0

    # 一直到栈中没元素吧，不断附加和弹出结点
    while stack:
        # 弹出一个  结点（这里  最后一个压入的先弹出，那每次都是先弹出 右边的孩子，好像也无所谓了，反正都能察觉到了）
        tree_node,cur_depth=stack.pop()
        # 根据结点 情况，做判别， 左右 都进行压入即可，
        if tree_node:
            max_depth=max(max_depth,cur_depth)
            stack.append((tree_node.left,cur_depth+1))
            stack.append((tree_node.right, cur_depth + 1))


    return max_depth
