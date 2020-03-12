# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
      你可以假设数组是非空的，并且给定的数组总是存在众数。

        示例 1:
        输入: [3,2,3]
        输出: 3

        示例 2:
        输入: [2,2,1,1,1,2,2]
        输出: 2

      分析：


      思路：按照题目要求，把数组排序后中间那个数就是众数。

'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) / 2]

#___________________________________    练习1   ______________________________#
def fun1(nums):
    nums.sort()
    return nums[len(nums)/2]
