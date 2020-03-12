# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
           序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

            示例 1：

            输入：target = 9
            输出：[[2,3,4],[4,5]]
            示例 2：

            输入：target = 15
            输出：[[1,2,3,4,5],[4,5,6],[7,8]]
             

            限制：1 <= target <= 10^5

      分析： 比较有趣，根据数值n 来计算，  和为n的 子序列。 （在1-n内部找子序列）


      思路：  这里比较简单是 要求连续序列，所以直接窗口就好。

            感觉 最简单的 双层循环的方式就能解决，可是那个时间复杂度有点大偶。
            然后相当的思路，就是直观下 滑动窗口的方法，肯定能解决该问题。
'''

#这里使用 滑动数组的方式。
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        # 使用滑动窗口法吧

        # 首先  定义多个意义的进行 收集的数组。    res是目标子数组的收集     ls用于容纳滑动窗口，承载扩展的效果。
        res = list()
        ls = list()
        sum = 0

        #  针对窗口 进行滑动。  核心：  如果窗口内和 大于target 就 左收缩。   反着就右扩张。
        for i in range(1, target):

            #  进行需要左收缩操作的判别， 总和上的缩减
            while sum > target:
                sum -= ls[0]
                del ls[0]
            #  当窗口满足条件
            if sum == target:
                res.append(ls[:])

            # 滑动窗口右扩张，并进行 信息的收入。
            sum += i
            ls.append(i)

        # 本题最后返回的就是 收集的合格数值列表。
        return res