# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

            说明：解集不能包含重复的子集。

            例如 输入: nums = [1,2,3]
                输出:
                  [
                      [3],
                      [1],
                      [2],
                      [1,2,3],
                      [1,3],
                      [2,3],
                      [1,2],
                      []
                  ]

      分析：
      思路：可以使用两种基本方式吧，回溯法或者 线性搜索法。
        【1】回溯法。对于每个数字考虑放它或者不放它。
        【2】线性扫描，读取k+1个数时，把前k个数的所有子集都新加入一个k+1，形成含有这个k+1的所有子集，再把它们放入result。
'''

########    第一种.回溯的方式    ##########
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, tmp = [], []

        def generate(nums, n):
            res.append(tmp[:])

            if n == len(nums):
                return
            for i in range(n, len(nums)):
                tmp.append(nums[i])
                n += 1
                generate(nums, n)
                tmp.pop()

        generate(nums, 0)
        return res

########    第二种.线性搜索的方式    ##########
class Solution1(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            for i in result[:]:
                item = i[:]
                item.append(num)
                result.append(item[:])
        return result

#___________________________________    练习1   ______________________________#
# 传输 nums作为  字符集合
#  这里使用线性搜索 并 收集的方法，进行如下的操作
def fun1(nums):
    #
    result=[[]]
    for num in nums:
        '''
           这里  arr[:]的效果是什么样的呢：  
              [1,2,3]  的  [:]  效果就是         1 2 3   跟正常的没区别
              但是这下面好像有空集合
        '''
        for i in result[:]:
            #item  是进行 多重的逐个附加上的尝试，三种的添加方式，可以较好地保证，而且能够避重
            print(i)
            item=i[:]
            item.append(num)
            result.append(item[:])
    return result