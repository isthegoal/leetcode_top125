# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：根据一棵树的前序遍历与中序遍历构造二叉树。

      例如，给出 前序遍历 preorder = [3,9,20,15,7]
                中序遍历 inorder = [9,3,15,20,7]
                返回如下的二叉树：
                            3
                           / \
                          9  20
                            /  \
                           15   7


      分析：


      思路：使用迭代方法深度构建即可

   首先根据前序遍历的定义可以知道，preorder这个数组的第一个元素preorder[0]一定是root，再根据中序遍历的定义，
   在inorder这个数组里，root前面的元素都属于root的左子树，root后面的元素都属于右子树，
   从这一步得到了left_inorder和right_inorder，接下来我们只需要把root在inorder里的位置index = inorder.index(preorder[0])查找出来，
   就可以知道其左子树和右子树的长度，然后再回到preorder，root后面先是左子树，然后是右子树，因为上一步我们已经知道了它们的长度，
   所以可以得到left_preorder和left_preorder，然后递归不就完事了。


'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        left_inorder = inorder[: inorder.index(root.val)]
        right_inorder = inorder[inorder.index(root.val) + 1:]

        l_left = len(left_inorder)
        left_preorder = preorder[1:l_left + 1]
        right_preorder = preorder[l_left + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root



'''
  这里是剑指中的原题：
     就是一般的   数据结构的问题，利用 前序遍历结果  和  中序遍历结果来确定一棵树

     思路：前序的第一个元素是根结点的值，在中序中找到该值，中序中该值的左边的元素是根结点的左子树，右边是右子树，然后递归的处理左边和右边

     根本思想还是 利用树的性质做  递归，很简单的递归【不断延伸完成树的构建】
'''
class TreeNode1():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def construct_tree(preorder=None,inorder=None):

    # 首先是递归截止条件
    if not preorder or not inorder:
        return None

    #根据  先序遍历的位置找到 根节点。
    index=inorder.index(preorder[0])
    left=inorder[0:index]
    right=inorder[index+1:]

    #创建节点树   (不断嵌入搭建好整个树，注意  一个树下前序和中序的长度肯定是一致的)
    root=TreeNode(preorder[0])
    root.left=construct_tree(preorder[1:1+len(left)],left)
    root.right=construct_tree(preorder[-len(right)],right)
    return root
#___________________________________    练习1   ______________________________#
#  这个是比较  有趣的， 考研中 经常会用到的题吧，根据前中序遍历列表  来进行二叉树的构建,还原出原二叉树。
#  传递前序  和  中序 序列。
#   先找到的根节点索引   不断切分左右子树 进行整体构建
#   时间复杂度为O(N) 空间复杂度为O(N)
class Solution1(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 边界条件
        if not preorder:
            return None

        # 先根据 先序和中序序列  找到根节点位置
        index=inorder.index(preorder[0])
        # 根据找到的根节点索引   切分左右子树
        left=inorder[:index]
        right=inorder[index+1:]

        #根据   左右子树  来创建节点树吧.     分别创建根节点 和 左右节点指向，从而完成整个树的搭建
        root=TreeNode(preorder[0])
        # 这里左右子树的指向   分别是根节点切分后的  递归需要传递的前序和 中序序列.....
        root.left=self.buildTree(preorder[1:1+index],left)
        root.right=self.buildTree(preorder[index+1:],right)

        # 不断的递归和回溯，完整整个树的所有工作。
        return root


