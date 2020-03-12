# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

            输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
            输出: 3
            解释:  节点 5 和节点 1 的最近公共祖先是节点 3。

            输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
            输出: 5
            解释: 节点 5 和节点 4 的最近公共祖先是节点 5。

            说明:
                所有节点的值都是唯一的。
                p、q 为不同节点且均存在于给定的二叉树中

      分析：

      思路：递归，如果当前节点就是p或q，说明当前节点就是最近的祖先，如果当前节点不是p或p，就试着从左右子树里找pq。
            如果pq分别在一左一右被找到，那么当前节点还是最近的祖先返回root就好了，否则，返回它们都在的那一边。

'''

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)

            if left and right:  # 一个在左子树，一个在右子树
                return root
            elif left:  # 都在左子树
                return left
            elif right:  # 都在右子树
                return right
            else:
                return

#___________________________________    练习1   ______________________________#
'''
    之前做过二叉搜索树的  最近公共祖先，这题要跟那题不一样，因为没有大小比值上的关系。
    因此这里 针对于普通二叉树上的  祖先查找，方法应该是 针对于指针  来进行判别。【但是思路要 更加难些】
    其实下面的解法，还不太明确，感觉,实在不好理解，就画图思考下。

    
    左子树或自己含p 就返回p，右子树或自己含q就返回q，左右子树返回一p一q则返回自己，如果某子树返回了答案（另一子树必然返回None），
    则返回答案，剩下就是两个子树都返回空，则返回空。 经过逻辑化简：
        【1】先分析自己，自己是p,q,None中的一者，自然返回自己。
        【2】然后分析左右子树的返回值，如果其中一个是None，则返回另一个，作为传递，无论是传递最终的答案，还是传递p和q。
        【3】如果左右子树返回p和q，当然返回root。 Python中的None即C/C++/Java 中的Null/null
'''
def fun1(root,p,q):
    #  一.边界情况，如果 root指向为空，  或者指到了p、q,就 进行边界停止
    if not root or root==p or root==q:
        return root

    else:
        # 首先获得左右 指针寻找上的情况
        left=fun1(root.left,p,q)
        right=fun1(root.right,p,q)

        # 二.进行三步的判别，如果个在左子树，一个在右子树
        if left and right:
            return root
        # 三.都在左子树
        elif left:
            return left
        # 都在右子树
        elif right:
            return right
        else:
            return
