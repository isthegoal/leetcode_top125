'''

    题目：给出一个完全二叉树，求出该树的节点个数。

    完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干
    位置。若最底层为第 h 层，则该层包含 1~ 2的h次方 个节点。


'''

# 这题应该利用完全二叉树的 性质 来进行结点统计，直接递归统计，会被面试官怼的

'''
   选用 二分判别的方法，时间复杂度O(log(N)*log(N)),空间复杂度为O(log(N)),维护递归栈
  
回顾一下满二叉的节点个数怎么计算，如果满二叉树的层数为h，则总节点数为：2^h - 1.
那么我们来对root节点的左右子树进行高度统计，分别记为left和right,有以下两种结果：

left == right。这说明，左子树一定是满二叉树，因为节点已经填充到右子树了，左子树必定已经填满了。
所以左子树的节点总数我们可以直接得到，是2^left - 1，加上当前这个root节点，则正好是2^left。再对右子树进行递归统计。
left != right。说明此时最后一层不满，但倒数第二层已经满了，可以直接得到右子树的节点个数。
同理，右子树节点+root节点，总数为2^right。再对左子树进行递归查找。
关于如何计算二叉树的层数，可以利用下面的递归来算，当然对于完全二叉树，
可以利用其特点，不用递归直接算，具体请参考最后的完整代码。

'''

class Solution(object):
    def countNodes(self, root):
        if root==None:
            return 0
        # 计算高度
        left=self.getdepth(root.left)
        right=self.getdepth(root.right)

        #进行 left==right上的判别处理
        if left==right:
            # 左子树为 满二叉树
            return self.countNodes(root.right)+(1<<left)
        else:
            # 没有右侧，所以可以直接计算出右子树的 结点数量
            return self.countNodes(root.left)+(1<<right)

    # 获取深度
    def getdepth(self, root):
        depth = 0
        while root:
            depth += 1
            root = root.left

        return depth

