# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。
      你需要让组成和的完全平方数的个数最少。

        示例 1:
        输入: n = 12
        输出: 3
        解释: 12 = 4 + 4 + 4.

        示例 2:
        输入: n = 13
        输出: 2
        解释: 13 = 4 + 9.

      分析：

      思路：依然是一个求最短路径的问题，每一条路径的起点是当前的和，下一个节点是加上一个完全平方数之后的和，
      求从0到n最短的移动步数，所以用BFS处理。

'''
from collections import deque
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 起始点：当前的和
        # 下一层：加上一个完全平方数之后的和
        # 求最短路径用BFS
        record = []
        for i in range(1, int(n ** 0.5) + 1):
            record.append(i * i)
        # print record
        visited = set()
        q = deque()
        q.append([0, 0])
        while (q):
            m, cnt = q.popleft()
            for num in record:
                s = m + num
                if s == n:
                    return cnt + 1
                if s < n and s not in visited:
                    visited.add(s)
                    q.append([s, cnt + 1])

#___________________________________    练习1   ______________________________#
# 下面使用的动态规划法，是我更加喜欢的，思路很直接。
# n是要进行求和得到的目标值
def numSquares1(self, n):
    """
    :type n: int
    :rtype: int
    """
    # 定义状态数组.  每个状态的含义都是 最小的组成数字
    dp=[0]*(n+1)

    #进行状态上的计算转移。就像贝诺蔓塔一样的不断累上算。
    for i in range(1,n+1):
        dp[i]=i #最坏情况是加1，也就是所有1加一起，我们的目标当然是最少比较好
        #尝试更新，减少那种累计数字
        for j in range(1,int(i**0.5)+1):
            dp[i]=min(dp[i],dp[i-j*j]+1)
    return dp[n]


