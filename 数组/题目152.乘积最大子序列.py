# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

            示例 1:
            输入: [2,3,-2,4]
            输出: 6
            子数组 [2,3] 有最大乘积 6。

            示例 2:
            输入: [-2,0,-1]
            输出: 0
            解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

      分析：

      思路：  基础的dpmax用来表示乘积最大的子序列的乘积，
            比较特殊的地方在于，因为是算乘积而且没有限定输入的范围，所以需要考虑负数的情况。
            所以要额外开一个dpmin表示乘积最小的子序列的乘积。
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dpmax = [0 for _ in range(l)]
        dpmin = [0 for _ in range(l)]

        dpmax[0] = nums[0]
        dpmin[0] = nums[0]
        for i in range(1, l):
            dpmax[i] = max(nums[i], max(nums[i] * dpmax[i - 1], nums[i] * dpmin[i - 1]))
            dpmin[i] = min(nums[i], min(nums[i] * dpmax[i - 1], nums[i] * dpmin[i - 1]))

        return max(dpmax)

#___________________________________    练习1   ______________________________#
# 这种题，很直接 干动态规划，干状态 定义 和状态转换.   只不过这里要考虑正的最大和负的最小，两个情况都得做好储备。
#   动态规划其实就是有记忆的递归
def fun1(nums):

    l=len(nums)

    #两个 方向的动态规划，正的最大和负的最小的考虑。  那么对于正的最小的情况呢，算了，正负号都应该考虑在内了,下面的定义和转换就够了。状态是当前次序下的最大和最小
    dpmax=[0 for _ in range(l)]
    dpmin=[0 for _ in range(l)]
    dpmax[0]=nums[0]
    dpmin[0]=nums[0]

    #核心的状态转移计算吧，还是比较简单的转移的
    for i in range(1,l):
        dpmax[i]=max(nums[i],max(nums[i]*dpmax[i-1],nums[i]*dpmin[i-1]))
        dpmin[i]=min(nums[i],min(nums[i]*dpmax[i-1],nums[i]*dpmin[i-1]))

    return max(dpmax)
