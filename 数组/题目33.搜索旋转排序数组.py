# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：假设按照升序排序的数组在预先未知的某个点上进行了旋转。
            ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
            搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
            你可以假设数组中不存在重复的元素。你的算法时间复杂度必须是 O(log n) 级别。

            例如
               输入: nums = [4,5,6,7,0,1,2], target = 0
               输出: 4

               输入: nums = [4,5,6,7,0,1,2], target = 3
               输出: -1

      分析：这里有个很明白的点 是  这个数组的特性是  对 原增序数组进行旋转的，有个轴的级跳。
            针对这样的数组来找到  目标值对应的索引。



      思路：
          将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。此时有序部分用二分法查找。
          无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环.

           对应在实现时。
           （1）先用二分查找找到旋转的分界点，比如[4,5,6,7,0,1,2]的7， 特点是这一位比后一位大。
           （2）找到之后数组就分成了两段单调递增的区间，将target跟nums[0]比较之后可以判断出target落在哪段区间上，
        然后就是普通的二分查找。


        思路贼简单，就是进行了两次的二分查找。 第一次二分方式找到  旋转位置。
                                           第二次二分查找是 在旋转划分后找到的空间中进行目标的二分搜索。

'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        # 第一步，找到旋转的分界点， 这里很明显也是使用二分法进行边界查找
        lo, hi = 0, len(nums) - 1
        while (lo <= hi):
            mid = (lo + hi) // 2
            # print mid, nums[mid]
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                break
            if nums[mid] < nums[-1]:
                hi = mid - 1
            elif nums[mid] >= nums[0]:
                lo = mid + 1

        # 对找到的辩解，进行新的操作,看目标归属哪个部分
        if lo > hi:  # 没有旋转
            lo, hi = 0, len(nums) - 1
        else:
            if target >= nums[0]:
                lo, hi = 0, mid
            else:
                lo, hi = mid + 1, len(nums) - 1

        #第二步，针对找到区间进行第二步的 二分查找，从中找到目标数。
        while (lo <= hi):
            # print lo, hi
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1

#___________________________________    练习1   ______________________________#
#针对扭曲数组，  找到指定值的位置索引
#思路非常简单： 方法是做了两次二分查找 和一次位置归属的获得，  一次找到扭曲的分开升降序的转折点。  第二次是 在扭曲空间内再进行查找
def fun(nums,target):
    if not nums:
        return -1
    if len(nums)==1:
        return 0 if nums[0]==target else -1

    # 开始第一次二分查找
    lo, hi = 0, len(nums) - 1
    while (lo <= hi):
        mid = (lo + hi) // 2
        # 找到发生 降序的位置，就是我们的目标 （这个是 注意的点）
        if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
            break
        if nums[mid] < nums[-1]:
            hi = mid - 1
        elif nums[mid] >= nums[0]:
            lo = mid + 1

    # 接下来 看看target的归属吧
    if lo > hi:  # 没有旋转
        lo, hi = 0, len(nums) - 1
    else:
        if target >= nums[0]:
            lo, hi = 0, mid
        else:
            lo, hi = mid + 1, len(nums) - 1

    # 接下来 开始第二次二分查找
    while (lo <= hi):
        # print lo, hi
        mid = (lo + hi) // 2  #找到了位置，结束
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1
