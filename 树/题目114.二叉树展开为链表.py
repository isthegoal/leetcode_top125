# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个二叉树，原地将它展开为链表。（剑指offer原题）

      例如，给定二叉树
            1
           / \
          2   5
         / \   \
        3   4   6

      将其展开为：
            1
             \
              2
               \
                3
                 \
                  4
                   \
                    5
                     \
                      6

      分析：

      思路：也有两种简单思路吧
           【1】如果不原地的话，开个数组记录前序遍历，再一个个放上去就好
           【2】递归。先把左右子树捋直，然后备份右子树，把捋直的左子树移到右子树的位置上，把左子树置空，
找到现在右子树的末尾，把捋直的原来的右子树接上去。
'''

#  递归的方式  进行对树进行锊平吧
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return root
        # 先把左右子树捋直
        self.flatten(root.left)
        self.flatten(root.right)

        tmp = root.right  # 把捋直的右子树备份一下

        root.right = root.left  # 把捋直的左子树放到右边
        root.left = None  # 记得把左子树置空
        while (root.right):  # 找到现在右子树的最后一个node
            root = root.right
        root.right = tmp  # 把捋直的原来的右子树接上去

#___________________________________    练习1   ______________________________#
#  这里有个很大的点， 是要求原地，因此 不是简单的 新创建结构、再进行附加的方式。

'''
       这里使用递归 锊平 的思路，简单思想分为三步：
        （1）针对根节点，首先锊平左右 子树。
        （2）首先  把 锊平好的左子树（注意，现在锊平好的左子树是 一条线往右的形式）直接附加到 root结点 的右指针上，首先让root的右子树指针 指向这一左子树。
        （3）接下来 把锊平好的右子树 直接附加到 上面得到的队列后面即可.....
        
      由下往上，不断递归着完成整个树的锊平
'''
def fun1(root):
    #  第一步   设定边界 和   由下往上锊平左右子树
    if not root or (not root.left and not root.right):
        return root

    fun1(root.left)
    fun1(root.right)

    # 第二步   把 锊平好的左子树（注意，现在锊平好的左子树是 一条线往右的形式）直接附加到 root结点 的右指针上  （1 2 3 4）
    #  对左子树的备份，之后会直接附加
    tmp=root.right

    root.right=root.left
    root.left=None
    # 开始很重要的   找到 现在的最右下方的位置，准备 右子树的附加
    while root.right:
        root=root.right

    # 第三步， 现在root指向已经走到 4 这个位置， 接下来把 5 6 直接附加到4右边即可
    root.right=tmp


