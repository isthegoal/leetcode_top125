# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i]
      之外其余各元素的乘积。

         示例:
         输入:
         [1,2,3,4]

         输出:
         [24,12,8,6]

         不要使用除法，且在 O(n) 时间复杂度内完成此题。

      分析：

      思路：有两种思路吧。

      【1】第一种思路：不能用除法，那只能用乘法统计其他元素的乘积了，一共扫两趟，
      第一趟从左往右走，开一个数组叫left记录除第一个元素外，其他每个元素的所有左边元素的乘积，left[0] = 1
   比如对于[1,2,3,4]，我们有left = [1,1, 2, 6]，类似的，第二趟从右往左走，开right数组记录所有右边元素的乘积right[-1]=1
    比如对于[1,2,3,4]，我们有right = [24, 12, 4, 1]最后把left和right对位相乘，就是需要的结果。
      【2】学习子答案，O(1）的空间就可以实现。

'''

#方法一
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            nums[i] = left[i] * right[i]
        return nums

#方案二
class Solution1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]
        return res


#___________________________________    练习1   ______________________________#
#  这里打算使用 走两边的方法， 用两个数组 记录 左右数字的乘积,很简单res 先表示左乘，然后再乘右乘，就得到结果了
#  时间复杂度为O(N)，空间复杂度为O(N),直接存储的是结果
def fun1(nums):

    #  进行左乘,res每个位置保存它左侧所有元素的乘积
    res=[1]*len(nums)
    for i in range(1,len(nums)):
        res[i]=res[i-1]*nums[i-1]

    # 重置乘积k=1，用来保存元素右边的乘积和
    tmp=1

    #从右向左遍历，遍历区间(n,0],不断这样 获取右积
    for i in range(len(nums)-1,-1,-1):
        # 表示将当前位置的左积乘以右积。       下面两行前后放置也是有含义的，有个差位
        res[i]*=tmp
        tmp*=nums[i]

    # 这里的res 就是所有位置对应的的左积 和右积   的乘积，且没有乘本身....
    return res


