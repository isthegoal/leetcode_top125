'''
      题目：给定一个二叉树，返回所有从根节点到叶子节点的路径。
           说明: 叶子节点是指没有子节点的节点。

                输入:

                   1
                 /   \
                2     3
                 \
                  5

                输出: ["1->2->5", "1->3"]

                解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3


      分析：
            前序遍历，根-->左子树-->右子树
            中序遍历，左子树-->根-->右子树
            后序遍历，左子树-->右子树-->根
            前序/后序+中序能够确定一个完整的树结构，因为前序/后序的根在第一位/最后一位，这样在中序中找到对应的根节点，以此递归，具体的题见leetCode105、106
            广度优先遍历（Breadth FirstSearch，BFS,实际上就是逐层查找，又叫层次遍历，宽度优先搜索或横向优先搜索）
            深度优先遍历（Depth First Search，DFS，主要有三种子方法，前中后序遍历）
            这里使用DFS方法。


      思路：  直接DFS递归解决所有

         递归模板题。
         先访问根节点，再判断分别左右子树。
         如果是叶子节点，就保存到 ans 中，如果不是就加入到 path 中，继续访问直到到达叶子节点为止。

'''
#直接DFS递归解决所有       如果是叶子节点，就保存到 ans 中，如果不是就加入到 path 中，继续访问直到到达叶子节点为止
# 时间复杂度为 O(N)，空间复杂度为最优为O(log(N))  其深度
def fun1(root):
    if not root:
        return []

    #进行  遍历结果的收集   和 启动dfs搜索吧
    ans=[]
    dfs(root,ans,''+str(root.val))


def dfs(root,ans,path):
    # 如果已经遍历到终点的话，  就附加路径吧  （递归的一个终止处吧）
    if root.left==None and root.right==None:
        ans.append(path)

    #  针对左子树的处理情况，进行左走和 新的位置的附加判别
    if root.left!=None:
        dfs(root.left,ans,path+'->'+str(root.left.val))
    # 同理针对  右子树行走的也是这样。
    if root.right!=None:
        dfs(root.right,ans,path+'->'+str(root.right.val))



#___________________________________    练习1   ______________________________#
#   这里非常典型的DFS搜索解决问题
# 搜索开始函数
def fun2(root):
    if not root:
        return []

    ans=[]

    # 三个重要的信息，   结点位置，收集的路径，已经走的字符路径
    dfs1(root,ans,''+str(root.val))

def dfs1(root,ans,path):
    #  对成功构成路径的判别
    if root.left==None  and  root.right==None:
        ans.append(path)

    #  dfs的对左子树遍历处理部分
    if root.left!=None:
        dfs(root.left,ans,path+'->'+str(root.left.val))
    #继续的 dfs 右子树的探索
    if root.right!=None:
        dfs(root.right,ans,path+'->'+str(root.right.val))

    # 这里dfs是不需要还原的，不会产生 厚的累积，所以无影响。

