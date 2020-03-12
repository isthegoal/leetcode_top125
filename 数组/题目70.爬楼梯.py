# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

           示例：
                输入： 2
                输出： 2
                解释： 有两种方法可以爬到楼顶。分别是：
                    1.  1 阶 + 1 阶
                    2.  2 阶

           示例 2：
                输入： 3
                输出： 3
                解释： 有三种方法可以爬到楼顶。分别是：
                1.  1 阶 + 1 阶 + 1 阶
                2.  1 阶 + 2 阶
                3.  2 阶 + 1 阶

      分析：


      思路：直接可以看做斐波那契数列，使用动态规划法解决即可

'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return [1, 2][n - 1]
        first = 1
        second = 2
        cnt = 2
        while cnt < n:
            cnt += 1
            cur = first + second
            if cnt == n:
                return cur
            first = second
            second = cur

#___________________________________    练习1   ______________________________#
#   感觉 这就是简单的 斐波那契数的问题。
#   从前往后爬爬爬，统计即可
def fun1(n):
    # 边界条件
    if n==1:
        return 1
    if n==2:
        return 2

    #初始阶梯定义
    first=1
    second=2

    #进行塔上 走的次数上的更新
    for i in range(3,n+1):
        #这就是  斐波那契数的规律，考虑了所有的情况了
        third=first+second
        first=second
        second=third

    return second


