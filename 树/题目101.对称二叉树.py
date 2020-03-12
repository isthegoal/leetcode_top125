# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个二叉树，检查它是否是镜像对称的。(剑指offer原题)

            例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
                1
               / \
              2   2
             / \ / \
            3  4 4  3

       但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的（所以我们需要把为null的情况进行单独的记性考虑）:
                1
               / \
              2   2
               \   \
               3    3

      分析：

      思路：主要有两种思路吧，分别是  递归和  迭代两种方式。
            【1】第一种是 使用层次遍历的方式，层序遍历找出来，判断每一层是不是回文数组。
            注意：跟普通的层序遍历不一样的地方在于：如果是空结点，也要把None添加到层序遍历的结果数组里。
            【2】第二种方式是 递归方式，核心思想是 将  两个node一左一右地对比是不是一样。

'''

#    层次遍历 并 判断回文串的方式
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        queue = [root]

        while (queue):
            next_queue = list()
            layer = list()
            for node in queue:
                if not node:
                    layer.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)

                layer.append(node.val)

            if layer != layer[::-1]:
                return False
            queue = next_queue

        return True


#    第二种是递归左右判别的方式
class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)

        return check(root, root)

#___________________________________    练习1   ______________________________#
# 这里使用  非递归的方法吧，层次遍历后，判别得到的序列是否是回文.  使用两个层次存储队列  来 记录 层次遍历的结果
def fun1(root):
    queue=[root]

    while(queue):
        # 对当前层  和下一层上的收集
        next_queue=list()
        layer=list()

        #对于每个单层， 进行下一层的结点  层次遍历  回文性判别
        for node in queue:
            if not node:
                layer.append(None)
                continue
            # 非空结点时，对下一层的 正常的附加
            next_queue.append(node.left)
            next_queue.append(node.right)
            #当前层上的收集
            layer.append(node.val)
        #当前 回文判别
        if layer!= layer[::-1]:
            return False
        # 替换
        queue=next_queue
    return True




