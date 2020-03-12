# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个二叉树，返回它的中序 遍历。

      示例:

            输入: [1,null,2,3]
               1
                \
                 2
                /
               3

            输出: [1,3,2]

      分析：


      思路：  非常简单常规的问题，一般就两种思路，一种是递归的思路，另一种是使用栈和队列的形式来辅助实现。

'''


#首先是  简单的递归形式
def inorder(root):
    if not root.left and not root.right:
        return

    inorder(root.left)
    print(root.val)
    inorder(root.right)

# 非递归打印方式      还是使用栈的方法吧    感觉就是  如果还能往左走就一直往左走，  否则 就打印本身，弹出栈并尝试往右走
def inorder2(root):
    stack=[]
    pos=root

    #大环境， 如果栈中有元素，就可以一直往下走
    while pos is not None or  len(stack)>0:
        # 如果指向的不是空结点
        if pos is not None:
            stack.append(pos)
            pos=pos.left
        # 如果指向的是空结点时，那就弹出上一个位置，并进行打印 以及往右看
        else:
            pos=stack.pop()
            print(pos.val)
            pos=pos.right

#___________________________________    练习1   ______________________________#
#   这里  使用栈的方式进行   实现中序遍历吧，很简单的题。  （下面的非递归的栈思路，是非常常见的实现思路）
def fun1(root):
    # 创建栈
    stack=[]
    pos=root

    #  进行栈的压入和弹出   以及遍历设定  （重要条件是栈不能为空）
    while pos is not None  or len(stack)>0:
        #  当可以访问时， 左分支优先压栈，但不进行实际访问
        if pos is not None:
            stack.append(pos)
            pos=pos.left
        # 当需要弹出时, 弹出信息，进行遍历  并做 右分支访问
        else:
            pos=stack.pop()

            # 进行访问吧
            print(pos.val)

            #最后右指定吧，
            pos=pos.right
