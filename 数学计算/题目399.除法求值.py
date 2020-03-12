# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给出方程式 A / B = k, 其中 A 和 B 均为代表字符串的变量， k 是一个浮点型数字。根据已知方程式求解问题，
      并返回计算结果。如果结果不存在，则返回 -1.0。

      示例 :
        给定 a / b = 2.0, b / c = 3.0
        问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
        返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]

        equations(方程式) = [ ["a", "b"], ["b", "c"] ],
        values(方程式结果) = [2.0, 3.0],
        queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

            我们最终需要的就是要得到a/c的结果，b/a的结果...... 这里a-e是没有边的，所以返回-1
      分析：


      思路：
        建图然后DFS搜索。
        a -> b 这条路的weight 是2.0, b - > c的weight是3.0,
        求a -> c的结果就是求从a出发到c的一条路径，并返回路径上所有weight 的乘积。

'''


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]     以字典的形式来模拟图 和 树
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        graph = defaultdict(set)
        weight = defaultdict()

        for i, equation in enumerate(equations):
            start, end = equation[0], equation[1]
            graph[start].add(end)  # 设置从start到end 的path
            weight[(start, end)] = values[i]  # 给上一行设置的path分配weight
            graph[end].add(start)  # 设置从end到start的path
            weight[(end, start)] = 1.0 / values[i]  # 给上一行设置的path分配weight

        # print weight
        def dfs(start, end, visited):
            if (start, end) in weight:  # 如果可以直接读出结果
                return weight[(start, end)]  # 就直接返回

            if start not in graph or end not in graph:  # 这两个点根本没出现过
                return 0

            if start in visited:  # 已经形成路径环了还没找到结果
                return 0

            visited.add(start)  # 标记一下start来过了
            res = 0

            #正式条件的寻找
            for tmp in graph[start]:  # 遍历所有能从start出发的路径
                res = weight[(start, tmp)] * dfs(tmp, end, visited)
                if res != 0:  # 找到了第一条路，这条路是可行的 结果，就进行保存吧
                    weight[(start, end)] = res  # 把这一条路的weight记录下来
                    break
            visited.remove(start)  # 回溯
            # print res
            return res

        #接下来针对 我们需要查询的结构，进行图的深度遍历，其本质就是在图中进行查找。
        res = []
        for query in queries:
            tmp = dfs(query[0], query[1], set())
            if tmp == 0:  # 如果没找到
                tmp = -1.0
            res.append(tmp)

        return res

#___________________________________    练习1   ______________________________#
# 这应该是一道一般难度的图问题，感觉到了难度，但是绝对可以庖丁解牛来  克服，逐步体系化、图像化思维来突破。
# 这里使用感觉 可以使用自己有点健忘的  图的深度、广度遍历操作来解决吧
'''
   这道题的 对字母的连接关系其实是 除法，因此某种角度来看，可以将除法看做一个关系连线。
   
   这样有了关系结点和 关系连线之后，实际相当于构建了一个图的结构，从而可以在这种图的结构上
   进行深度和广度的遍历即可。
   
'''
# 方法参考于这里https://leetcode-cn.com/problems/evaluate-divismments/ion/co
from collections import defaultdict
#这里的三者  equations是方程式  values是方程式结果   queries则是问题方程式
def fun1_DFS(equations,values,queries):
    #进行图 和 边上权重的定义
    graph=defaultdict(set)
    weight=defaultdict()
    lookup={}

    #首先进行 图的初始构建。   根据方程式建图(构建好了除法关系图，我们以现有的关系构建图)
    for idx,equ in enumerate(equations):
        graph[equ[0]].add(equ[1])
        graph[equ[1]].add(equ[0])

        weight[tuple(equ)]=values[idx]
        weight[(equ[1],equ[0])]=float(1/values[idx])

    #对于上面构建好的图，接下来进行深度的遍历(深度遍历)
    def dfs(start,end,visited):
        #等图中直接就有这个边时，直接输出结果
        if (start,end) in weight:
            return weight[(start,end)]
        #当图中没这个点时
        if start not in graph or end not in graph:
            return 0
        # 当结点曾经访问过
        if start in visited:
            return 0

        #现在开始正常的深度遍历和 存储
        visited.add(start)
        res=0
        for tmp in graph[start]:
            # 当存在这个边时，进行 累计的计算，就像a到c的过程是2*3一样。
            res=(dfs(tmp,end,visited)*weight[(start,tmp)])
            #当深度遍历到一个不是0的解，退出(这里退出时，这个权重其实就是我们的目标)
            if res !=0:
                weight[(start,end)]=res
                break
        visited.remove(start)
        return res

    #接下来是 启动深度遍历的过程，可以类似看为主函数
    res=[]
    for que in queries:
        #用集合 来 存储对于 结点的访问情况
        tmp=dfs(que[0],que[1],set())
        if tmp==0:
            tmp=-1.0
        res.append(tmp)
    return res