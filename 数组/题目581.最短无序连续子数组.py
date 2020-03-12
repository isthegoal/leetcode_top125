# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
            你找到的子数组应是最短的，请输出它的长度。

             示例 1:
             输入: [2, 6, 4, 8, 10, 9, 15]
             输出: 5
             解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序

      分析：


      思路：先使用sorted()函数将原列表排序，将排序后的列表与原列表中的数据一一对应，找出左边第一个不同的元素与右边起第
      一个不同的元素，二者之间数据个数即为输出结果。

'''

#   如下是  第一种方法，比较简单的  排序后，进行逐个比较的方法。  思路过于简单
class Solution(object):
    def findUnsortedSubarray(self, nums):

        #使用sorted()函数将原列表排序

        nums_ordered = sorted(nums)
        r = -1
        l = len(nums)

        #很简单   找到左边第一个不同
        for i in range(len(nums)):
            if nums_ordered[i] != nums[i]:
                l = i
                break

        #同时找到  右边第一个不同的地方
        for i in range(len(nums) - 1, 0, -1):
            if nums_ordered[i] != nums[i]:
                r = i
                break

        #二者之间数据个数即为输出结果。
        if r <= l:
            return 0
        else:
            return r - l + 1


#___________________________________    练习1   ______________________________#
# 接下来，试下 不进行预排序的方法。  下面的思路也非常简单，但是比较耗时，2倍的O(N)时间复杂度
class Solution1(object):
    def findUnsortedSubarray(self, nums):
        # 边界条件的设置
        if not nums:
            return 0
        n = len(nums)

        # 正序遍历，根据局部最小值，更新最左端索引。
        max_ = nums[0]
        right = 0
        for i in range(n):
            if nums[i] > max_:
                max_ = nums[i]
            elif nums[i] < max_:
                right = i

        # 逆序遍历，根据局部最大值，更新最右端索引
        min_ = nums[-1]
        left = n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] < min_:
                min_ = nums[i]
            elif nums[i] > min_:
                left = i


        #  按照左右比较的索引，来获取出  目标连续的子数组的长度
        if left >= right:
            return 0
        return right - left + 1


'''
    另一种简单书写的方式：
            1.升序排列数组存入目标数组targ；
            2.将原始数组nums和目标数组targ比对；
            3.将首尾相同的元素删掉，直到有不同；
            4.记住首尾不同元素的位置，切片即可。

        '''
def findUnsortedSubarray(nums):
    #  第一步
    targ=sorted(nums)
    if targ==nums:
        return 0

    # 第二三步，不断比较，找到开始的不同的左右 索引位置
    i,j=0,len(nums)-1
    while nums[i]==targ[i]:
        i=i+1
    while nums[j]==targ[j]:
        j=j-1

    #最后  返回  位置长度
    return len(nums[i:j+1])
