# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

       你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
       给定 nums = [2, 7, 11, 15], target = 9
       因为 nums[0] + nums[1] = 2 + 7 = 9
       所以返回 [0, 1]

      分析：这道题思路相当的简单，直接使用哈希表就可以了， 把差值当做字典的键，把  索引当做键对应的值。
              特别熟悉和清晰的思路。


'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, item in enumerate(nums):
            if hashmap.has_key(target - item):
                return hashmap[target-item],index
            hashmap[item] = index

#___________________________________    练习1   ______________________________#
#非常简单的两数 之和，太熟悉的一道题了
def fun1(nums,target):
    #字典
    hashmap={}
    #进行遍历吧.  这里的关键 是寻找每个值 和目标值的差值
    for index,item in enumerate(nums):
        #找到这个差值，匹配，就说明找到了。每个hashma下放的是索引
        if hashmap.has_key(target-item):
            return hashmap[target-item],index
        hashmap[item]=index
