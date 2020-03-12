# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

        例如 给定二叉树: [3,9,20,null,null,15,7],
                3
               / \
              9  20
                /  \
               15   7
            其层次遍历结果：
            [
              [3],
              [9,20],
              [15,7]
            ]



      分析：


      思路：
         简单直接的思路是使用BFS的方法，处理每一层的时候记录下一层的节点，并把当前这一层每个节点的值记录到结果里。

         此外就是使用队列的方式，进行遍历，也是非常常用的方式。

'''


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        node = [root]
        result = list(list())
        self.generate(node, result)
        return result

    def generate(self, node, result):
        next_layer_node = []
        current_layer_result = []

        for node in node:
            if node.left:
                next_layer_node.append(node.left)
            if node.right:
                next_layer_node.append(node.right)
            current_layer_result.append(node.val)

        result.append(current_layer_result)
        if len(next_layer_node) == 0:
            return

        self.generate(next_layer_node, result)


#这里是  利用辅助工具，使用队列的方式。
class Solution1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        res = []
        while queue:
            next_queue = []
            layer = []
            for node in queue:
                if node:
                    layer.append(node.val)
                    next_queue += [node.left, node.right]
            queue = next_queue[:]
            if layer:
                res.append(layer[:])
        return res

#___________________________________    练习1   ______________________________#
# 这里层次遍历，分为递归方法 和  非递归方法两种， 但是最为直观 且好理解的就是  非递归方法，这里使用队列的方式来实现把，很easy

#  这里有个特点，就是 题目中 每层是放在一个数组中的， 所以看样子  必须是按照每个layer合在一起了，因此 上面的队列写法是必须的
def fun1(root):
    # 创建 队列，用于承载每一层
    queue=[root]
    res=[]

    # 进行队列的压入和弹出.   这里每个queue存储单层的所有节点信息
    while queue:
        #  进行下一队列和 下一层上节点的收集   两者各有含义，一个是指针，另一个是具体指
        next_queue=[]
        layer=[]

        # 对于当前队列，进行层上遍历吧
        for node in queue:
            if node:
                # layer 和 next_queue 附加信息， 其中layer 附加的是 要遍历的值， next_queue 是指向下层的孩子。
                layer.append(node.val)
                next_queue+=[node.left,node.right]

        # 将收集的 队列 进行 含义替换吧
        queue=next_queue[:]
        # 对层遍历结果 做 附加
        if layer:
            res.append(layer[:])

    # 返回。
    return res

