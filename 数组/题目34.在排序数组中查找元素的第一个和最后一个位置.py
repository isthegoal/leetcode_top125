# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
            你的算法时间复杂度必须是 O(log n) 级别。
            如果数组中不存在目标值，返回 [-1, -1]

            输入: nums = [5,7,7,8,8,10], target = 8
            输出: [3,4]

            输入: nums = [5,7,7,8,8,10], target = 6
            输出: [-1,-1]

      分析：
      这题贼简单，有之前看到过思路，就是进行了三次二分查找。
      【1】第一次二分查找相当于边缘限定，用于确定这个数是否在  数组中，如果不在的话，那就不需要后面的了。
     其实python中的if i in [12,32，23...N]语句就能实现查找，但是这种方式的时间复杂度我认为是一种遍历方式的O(N),
     所以还是二分查找判别的方式更为高效，直接在O(logN)时间复杂度就能搞定了

      【2】第二次二分查找是进行 重复数字情况的左边界上的查找，找到target，但是左侧不是。
       (hi >= 1 and nums[hi - 1] != target) or hi == 0
      【3】第三次二分查找是进行 重复数字情况的右边界上的查找。找到target,但是右侧不是。
      (lo <= len(nums) - 2 and nums[lo + 1] != target) or lo == len(nums) - 1


      思路：首先确定存不存在，所以用一次二分查找来判断。
  找到之后再用第二次二分查找往左边找左边界，找到的条件是 已经找到下标为0了 或者 找到某个target，它的左边不是target。
  同理进行第三次二分查找，找右边界，找到的条件是 已经找到len(nums) - 1了 或者 找到某个target，它的右边不是target。


'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(nums) - 1
        # 第一步 找到目标数字所在的位置 midtarget，但是这个位置不一定是边界，但是可以作为进行边界查找时的依据
        while (lo <= hi):
            mid = (lo + hi) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        if lo > hi:  # 不存在
            return [-1, -1]



        midtarget = mid

        #第二步，进行 左边目标  数字位置 leftpos的查找。在（0，mid）范围内找左边界
        lo, hi = 0, mid
        leftpos = 0
        while (lo <= hi):
            # print lo, hi
            if (hi >= 1 and nums[hi - 1] != target) or hi == 0:  # 找到左边界或者找到头了
                leftpos = hi
                break
            mid = (lo + hi) // 2

            #下面的挪动细节，树主要体现左边界查找和右边界查找区分的核心。
            if nums[mid] == target:
                hi = mid
            elif nums[mid] < target:
                lo = mid + 1

        #第三步，在左边目标数字的基础上进行rightpos的查找，在（mid，len(nums)）范围内找右边界
        rightpos = 0
        lo, hi = midtarget, len(nums) - 1
        while (lo <= hi):
            if (lo <= len(nums) - 2 and nums[lo + 1] != target) or lo == len(nums) - 1:  # 找到右边界或者找到头了
                rightpos = lo
                break

            mid = (lo + hi + 1) // 2
            if nums[mid] == target:
                lo = mid
            elif nums[mid] > target:
                hi = mid - 1

        return [leftpos, rightpos]

#___________________________________    练习1   ______________________________#
#好吧，简单的三次二分查找.   首先找到 数字在 数组中的查找，  之后进行数字左边界的查找，  最后进行数字右边界的查找。
def fun1(nums,target):
    # 第一次二分查找，  确定了初步位置 mid点。
    lo, hi = 0, len(nums) - 1
    # 第一步 找到目标数字所在的位置 midtarget，但是这个位置不一定是边界，但是可以作为进行边界查找时的依据
    while (lo <= hi):
        mid = (lo + hi) // 2
        if nums[mid] == target:
            break
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    if lo > hi:  # 不存在
        return [-1, -1]

    midtarget = mid

    #以 mid点为基石，进行第二次二分查找     左查找，来找到左边 第一个值为target的点为左边界。
    lo, hi = 0, mid
    leftpos = 0
    while (lo <= hi):
        # print lo, hi    这里是主要的判断点，找到合适的左侧位置即可【也就是再左一步都不是target点】
        if (hi >= 1 and nums[hi - 1] != target) or hi == 0:  # 找到左边界或者找到头了
            leftpos = hi
            break
        mid = (lo + hi) // 2

        # 下面的挪动细节，树主要体现左边界查找和右边界查找区分的核心。
        if nums[mid] == target:
            hi = mid
        elif nums[mid] < target:
            lo = mid + 1

    #第三次 二分查找。     从右边往左找 到  第一个值为target的点
    rightpos = 0
    lo, hi = midtarget, len(nums) - 1
    while (lo <= hi):
        if (lo <= len(nums) - 2 and nums[lo + 1] != target) or lo == len(nums) - 1:  # 找到右边界或者找到头了
            rightpos = lo
            break

        mid = (lo + hi + 1) // 2
        if nums[mid] == target:
            lo = mid
        elif nums[mid] > target:
            hi = mid - 1

    # 获得了 左右边界，it's  over
    return [leftpos, rightpos]

