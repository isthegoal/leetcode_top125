# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，
      而不是第 k 个不同的元素。

        示例
        输入: [3,2,1,5,6,4] 和k = 2
        输出: 5


      分析：

      思路：  这个题也是 剑指offer原题，直接使用几种方法即可
           （1）直接调python库
           （2）使用堆的方式，这个方法相当不错的，一次所占据的空间更小，比较实用。
           （3）快排 + partition的方式。
'''

#方式一
class Solution1(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse = True)[k-1]

#方式二
class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import *
        heap = []
        heapify(heap)
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]


#方式三
class Solution3(object):
    def findKthLargest(self, nums, k):

        left, right, target = 0, len(nums) - 1, k - 1
        while True:
            pos = self.partition(nums, left, right)
            if pos == target:
                return nums[pos]
            elif pos > k:  # 要往左找
                right = pos - 1
            elif pos < k:  # 要往右找
                left = pos + 1

    def partition(self, nums, left, right):
        import random
        k = random.randint(left, right)
        pivot = nums[k]
        nums[left], nums[k] = nums[k], nums[left]
        index = left

        for i in range(left + 1, right + 1):
            if nums[i] > pivot:
                index += 1
                nums[i], nums[index] = nums[index], nums[i]
        nums[left], nums[index] = nums[index], nums[left]
        return index  # 此时所有index左侧的值都比nums[index]大， 所有右侧的值都比nums[index]小


#___________________________________    练习1   ______________________________#
# 好吧，既然是剑指上的原题，真的是特别简单了， 这里再锻炼一次就使用 快排+partition的方式 找到第k个最大的元素吧
# 快排 + 迭代的方法
def fun1(nums,k):
    # 主控制
    left,right,target=0,len(nums)-1,k-1

    #不断进行查找操作.  非常简单，就是通过partation 方式 多次分治  找到正当排序中的第k个位置
    while True:
        # 快速排序中，产生的排好的位置。pos就是排好确定好的位置
        pos=partation(nums,left,right)
        if pos==target:
            return nums[pos]
        elif pos>k:
            right=pos-1
        else:
            left=pos+1
def partation(nums,left,right):
    # 这里基于随机数的 partation方式，与以往的传统方式有所不同，是一种进化的方法,学习下
    # 这里不用反复的交换，一波即可，  就是目标找到nums[k]应该所处的位置
    import random
    k=random.randint(left,right)
    pivot=nums[k]

    # 把pivot放到最左边
    nums[left], nums[k] = nums[k], nums[left]
    index = left

    # 接下来，从前往后走，并进行换位，让比nums[k]大的逐步换到后面去
    for i in range(left + 1, right + 1):
        if nums[i] > pivot:
            index += 1
            nums[i], nums[index] = nums[index], nums[i]

    #最后再进行一比交换，现在获取的index  就是进行交换的次数，也就是前面有index个数大于pivot
    nums[left], nums[index] = nums[index], nums[left]
    return index
