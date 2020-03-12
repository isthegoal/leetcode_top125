'''

    题目：
        给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
        说明:?叶子节点是指没有子节点的节点。

            示例:
            给定如下二叉树，以及目标和?sum = 22，

                          5
                         / \
                        4   8
                       /   / \
                      11  13  4
                     /  \    / \
                    7    2  5   1
            返回:
            [
               [5,4,11,2],
               [5,8,4,5]
            ]
    思路：
         这里需要收集路径，我感觉就用dfs做深度遍历，同时做路径的收集即可。


'''
class Solution:
    def __init__(self):
        self.cur_path = []
        self.res = []

    def pathSum(self, root, sum):
        if not root:
            return []
        self.cur_path.append(root.val)
        sum -= root.val
        if not root.left and not root.right:  # 是叶子节点
            if sum == 0:
                print("当前路径：", self.cur_path)
                self.res.append(self.cur_path[:])
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        self.cur_path.pop()
        return self.res


#___________________________________    练习1    ______________________________#
# 非常简单的一道题吧， 就是DFS遍历，再进行 路径的收集，和  112题的思路基本一致。
cur_path=[]
res=[] # 存储成功的路径
def fun1(root,sum):
    #  边界条件，表示当前不是节点，那么直接返回作为DFS停止位置即可
    if not root:
        return []

    # 正常情况下，做调整
    cur_path.append(root.val)
    sum-=root.val

    #针对是叶子节点的情况,那就判别是否是有效路径
    if not root.left and not root.right:
        if sum==0:
            # 进行成功路径的附加
            res.append(cur_path[:])

    # 最后进行 递归的遍历，并记得在  遍历的最后  做还原即可
    fun1(root.left,sum)
    fun1(root.right,sum)
    cur_path.pop()

    # 最后将现在已经收集的路径  做返回即可
    return res
