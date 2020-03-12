# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：现在你总共有 n 门课需要选，记为 0 到 n-1。在选修某些课程之前需要一些先修课程。
           例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
           给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

            示例 1:
            输入: 2, [[1,0]]
            输出: true
            解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。

            示例 2:
            输入: 2, [[1,0],[0,1]]
            输出: false
            解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的

      分析：
            这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
            通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
            拓扑排序也可以通过 BFS 完成。

      思路：
        本题需要用拓扑排序解题，
            拓扑排序的流程如下：
            1. 找到一个入度为0的结点
            2. 删除这个节点，并把这个节点相邻的结点的入度 - 1
            重复这两步，直到所有的节点都被删除 或者 找不到更多的入度为0的结点 为止。
'''
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        from collections import deque
        if not prerequisites:  # 没有前置课的要求
            return True

        indegree = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]

        for end, start in prerequisites:
            indegree[end] += 1  # 统计入度
            adj[start].add(end)  # 生成邻接表

        queue = deque()
        for i, x in enumerate(indegree):
            if not x:  # 入度为0的结点入队
                queue.append(i)

        cnt = 0
        while queue:
            cur = queue.popleft()  # cur 出队并删除
            cnt += 1  # 当前的cur满足条件

            for neighbor in adj[cur]:
                indegree[neighbor] -= 1  # 邻居入度- 1
                if not indegree[neighbor]:  # 如果邻居入度变成了0了，就让它入队
                    queue.append(neighbor)

        return cnt == numCourses  # 判断是不是所有的点都删除成功了




#___________________________________    练习1   ______________________________#
'''
    本题可以理解为 判断 课程安排图是否是 有向无环图。
       设定在课程间设置前置条件，但是不能构成任何环路，
    
    基本想法：
       统计每个课被指向次数，初始被指向次数为0的肯定是安全的（不在环上）。
        每被安全课程指向一次，被指次数减一，
        如果被指次数减到0，说明该课程全部指向都来自安全课程，则它也是安全的。
        依此进行队列循环。
        
    
    基本思路：
        （1）统计课程图中每个节点的入度，生成入度图
        （2）使用队列，将入度为0的节点放到队列中
        （3）当队列没空时，将队首结点入队，从课程表中删除节点。
'''
# 这里主要的思路 是  思路是非常简单的， 在图结构中， 进行判别，找到是否环都是安全的。
# 传入课程数 和  现在安排的课程图，每个都是[前置，后续课程]的结构
def fun1(numCourses,prerequisites):
    # 构建入度队列，  临近统计adjacency
    indegrees=[0 for _ in range(numCourses)]
    adjacency=[[] for _ in range(numCourses)]
    queue=[]

    # 针对每个课程，统计入度, 以及 邻接情况连线的统计
    for cur,pre in prerequisites:
        indegrees[cur]+=1
        adjacency[pre].append(cur)

    # 将所有入度为0的课程 进行统计
    for i in range(len(indegrees)):
        if not indegrees[i]:
            queue.append(i)

    #  接下来就是第三步，进行弹出队，以及图上结点的删除
    while queue:
        pre=queue.pop(0)
        numCourses-=1

        #针对所有 入度为0结点的邻接，  进行结点连线的删除
        for cur in adjacency[pre]:
            indegrees[cur]-=1
            #如果删除后，当前连接的点 入度为0，那附加过去
            if not indegrees[cur]:
                queue.append(cur)

    #最后判别下，当不存在结点时，说明没有环的情况
    return not numCourses


