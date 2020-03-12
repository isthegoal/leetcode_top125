# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

            示例 1:
            输入: nums = [1,1,1,2,2,3], k = 2
            输出: [1,2]

            示例 2:
            输入: nums = [1], k = 1
            输出: [1]

      分析：

      思路：比较经典的思路吧，这类最k的选找，一般都是用最大最小堆的方法。


        在这种情况下， 建立并维护一个size 为k 的最小堆，使得堆顶元素的出现频率是堆中所有元素出现频率中最小的，

        遍历字典，如果一个元素当前出现频率 比 堆顶元素的出现频率都要小，则说明它必不可能是 TOP k 元素；

        否则，将当前元素插入堆中，并pop一次，以保证最小堆的size始终为k。

'''
'''
   使用堆的方式，速度比较快，但是  需要使用python下的堆结构，得熟悉下。
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        from heapq import *
        # time: O(nlogk)
        # space: O(n)
        dic = Counter(nums)  # O(n)
        heap = []
        heapify(heap)
        for key, val in dic.items():  # O(nlogk)
            if len(heap) < k:
                heappush(heap, (val, key))
            else:
                if heap[0][0] < val:
                    heappush(heap, (val, key))
                    heappop(heap)
        # print heap
        res = []
        while heap:  # O(klogk)
            top = heappop(heap)
            res.append(top[1])
        return res

#___________________________________    练习1   ______________________________#
# 其实有些方法看上去很简洁，比如下面这种，但是相对于堆的方式，其时间复杂度是nlog(N)的，因此占用空间过大，因此 更好的方法还是上面这种Nlog(K)的方式
# 下面的思路是非常清晰的，但是时间复杂度占得有点多，O(NlogN))，因为这个排序是快速排序
def fun1(nums,k):
    count_list=dict()
    result=list()

    #进行出现情况的统计
    for i in nums:
        count_list[i]=count_list.get(i,0)+1

    #根据出现情况进行逆序 排列
    t=sorted(count_list.items(),key=lambda l:l[1],reverse=True)

    #按照 排列取值即可
    for i in range(k):
        result.append(t[i][0])

    return result

#第二种方式（打卡时写的）
from collections import Counter
from heapq import *
class Solution1(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = Counter(nums)
        heap = []
        # 创建初始最小堆   堆内每个元素都是（数字：数字出现次数）的形式
        heapify(heap)
        for key, val in dic.items():
            if len(heap) < k:
                heappush(heap, (val, key))
            else:
                if heap[0][0] < val:
                    # 压栈 和弹出栈，如果有更小的来了，就放进去
                    heappush(heap, (val, key))
                    heappop(heap)

        # 将最小堆进行 打印输出.  打印出需要的k个
        res = []
        while heap:
            top = heappop(heap)
            res.append(top[1])
        return res
