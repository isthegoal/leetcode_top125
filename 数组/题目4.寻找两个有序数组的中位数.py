# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：  给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。   （剑指offer64题）
             请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
             你可以假设 nums1 和 nums2 不会同时为空。

                nums1 = [1, 2]
                nums2 = [3, 4]
                则中位数是 (2 + 3)/2 = 2.5

      分析：这里可以使用堆的方式，也能对时间复杂度有较好的保障。 【好吧，其实这就是剑指offer上的原题，直接大小堆的思路就行了，注意做对应放置和调整】

      思路：用一个大顶堆和一个小顶堆来维护数据，每次每个数进来，先把它丢进小顶堆，然后把小顶堆的堆顶丢进大顶堆，
           调整两个堆，使得size 差最大为1。这么搞的好处在于，小顶堆是数据流里前一半大的数，大顶堆是数据流里后一半的大的数，
            而且小顶堆的size一定 >= 大顶堆的size，小顶堆的堆顶M是小顶堆里最小的数，大顶堆的堆顶N是大顶堆里最大的数，
            如果两个堆的size相同，那么中位数就是return (M + N) / 2.0否则，return M / 1.0。注意python没有大顶堆，所以放进大顶堆的数乘了-1， 取出来的时候也要记得 * -1。

            维护小顶堆的数都  小于大顶堆。
'''

from heapq import *
class MedianFinder(object):
    # 维护两个堆，一个大顶堆，一个小顶堆，小顶堆里的数比大顶堆里的数都要大，
    # 如果有两个潜在的中位数（两个堆size相同），数据流的中位数就是两个堆顶之和除以2
    # 如果只有一个中位数，就看size更小的那个堆的堆顶
    # 如果新进来的数比小顶堆的数要小，就把它插入大顶堆
    # 如果新进来的数比小顶堆的数要大，就把它插入小顶堆
    # 调整两个堆，使得size 差最大为1
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_h = list()
        self.min_h = list()
        heapify(self.max_h)
        heapify(self.min_h)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None

        最为核心的加入堆时 的 堆调整工作。

        每次每个数进来，先把它丢进小顶堆，然后把小顶堆的堆顶丢进大顶堆，调整两个堆，使得size 差最大为1。
        """
        heappush(self.min_h, num)
        heappush(self.max_h, -heappop(self.min_h))

        #这里较为重要的，如果两个长度大于1时， 就需要进一步的调整了。 都是把大顶堆的数推到小顶堆。
        if len(self.max_h) > len(self.min_h):
            heappush(self.min_h, -heappop(self.max_h))

    #直接按照构建好的两个 堆 获取出中位数即可。
    def findMedian(self):
        """
        :rtype: float

        这里分为 最后的总数是奇数个还是  偶数个。
        如果是奇数，那就是第一个小堆的顶端即可，如果是偶数个，那就是  两个堆顶的中位数。
        """
        max_len = len(self.max_h)
        min_len = len(self.min_h)
        if max_len == min_len:  # 有两个候选中位数
            return (self.min_h[0] + -self.max_h[0]) / 2.
        else:  # 小顶堆的size 一定 >= 大顶堆的size，所以答案就是小顶堆的堆顶
            return self.min_h[0] / 1.

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mf = MedianFinder()
        for num in nums1:
            mf.addNum(num)
        for num in nums2:
            mf.addNum(num)
        return mf.findMedian()


#___________________________________    练习1   ______________________________#
# 这里使用二分查找法（类似于快速排序的思路），另一种时间复杂度也是O(log(m + n))的方式
def findMedianSort(nums1,nums2):
    m=len(nums1)
    n=len(nums2)
    k=(m+n)/2  #这个是找特殊位置.   这里的k就是需要的中位数

    #针对偶数和奇数的处理方式 （进行二分查找的起点）
    if (m+n)%2==0:
        return (findk(nums1,nums2,k)+findk(nums1,nums2,k-1))/2
    else:
        return findk(nums1,nums2,k)

#进行而分析啊，指定位置k的查找 (这里有一点是两个有序的数组)
def findk(n1,n2,k):
    if len(n1)>len(n2):
        return findk(n1,n2,k)
    if len(n1)==0:
        return n2[k]

    # 位置为 1序号的情况，也就是只查找一个，这就简单的判别即可
    if k==1:
        if n1[0]<n2[0]:
            if len(n1)>1:
                return min(n1[1],n2[0])
            else:
                return n2[0]
        else:
            if len(n2)>1:
                return min(n1[0],n2[1])
            else:
                return n1[0]
    if k==0:
        return min(n1[0],n2[0])

    #接下来是正常的二分查找的处理 (然后依据这种二分进行新的探索)
    '''
    比较绕脑的一点：
    
        考虑二分查找时的情况，我们希望找到第一个数组中前p个元素和第二个数组中前q个元素，我们想要的最终结果是：p+q等于k-1，
        这样第p+1个元素或者第q+1个元素就是我们要找的第k个元素。通过二分法将问题规模缩小，假设p=k//2-1，则q=k-p-1，且p+q=k-1。
        如果第一个数组第p个元素小于第二个数组第q个元素，我们不确定二数组第q个元素是大了还是小了，但一数组的前p个元素肯定都小于目标，
        所以我们将第一个数组前p个元素全部抛弃，形成一个较短的新数组。然后，用新数组替代原先的第一个数组，再找其中的第k-p个元素，依次递归。
        同理，如果第一个数组第p个元素大于第二个数组第q个元素，我们则抛弃第二个数组的前q个元素。当递归遇到k=1时，或者第p个元素=第q个元素时，
        结束递归。

    '''
    p=min(k//2-1,len(n1)-1)
    q=k-p-1
    #很有趣的，逐步比较大小方式的查找判别。
    if (n1[p]<n2[p]):
        return findk(n1[p+1:],n2,k-p-1)
    elif(n1[p]>n2[p]):
        return findk(n1,n2[q+1:],k-q-1)
    else:
        return n1[p]


