# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

            示例:
            输入: [0,1,0,3,12]
            输出: [1,3,12,0,0]

            说明:
            必须在原数组上操作，不能拷贝额外的数组。
            尽量减少操作次数。

      分析：


      思路：类似LeetCode-80. 删除排序数组中的重复项 II， 用i 代表处理后数组的元素下标，
      当遇到不是0的元素的时候就把这个元素放到处理后数组的 下标为 i 的位置上去。

'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


#___________________________________    练习1   ______________________________#
# 感觉这题题意 非常简单，直接 不断交换即可, 但是要保持原来的非0相对排序
# 这里主要使用了一种处理后 数组的思想，i就表示合格的处理后位置 ，思路很简单，就是对0值无为，只处理非0往前挪，然后其实最后几个就是0
def fun1(nums):
    i=0
    for j in range(len(nums)):
        # 直接对非0进行挪到该在的位置上处理。
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1

    return nums
