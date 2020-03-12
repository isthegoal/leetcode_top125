# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，
      为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

        示例 1:
        输入: [[0, 30],[5, 10],[15, 20]]
        输出: 2

        示例 2:
        输入: [[7,10],[2,4]]
        输出: 1


      分析：


      思路：根据输入的intervals数组，我希望能知道每个时刻 i 需要用多少个会议室 record[i]，
      这样我返回所需的最大值即可，
      这道题类似于作区间加法，在开会的时候区间内加一，所以利用前缀和数组来计算。对于每个interval，
      将它开始的时刻 record[begin] + 1， 结束的时刻 record[end] - 1，然后利用前缀和计算整个区间。
'''

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        if not intervals[0]:
            return 1
        intervals = sorted(intervals, key=lambda x: x[1])
        record = [0 for _ in range(intervals[-1][1] + 1)]

        for interval in intervals:
            # print record
            begin, end = interval[0], interval[1]
            record[begin] += 1
            record[end] -= 1

        for i, x in enumerate(record):
            if i > 0:
                record[i] += record[i - 1]
        return max(record)

#___________________________________    练习1   ______________________________#
# 这道题还是非常简单的，主要是计算重合情况。 做下统计即可
def fun1(intervals):
    # 边界条件
    if not intervals:
        return 0
    if not intervals[0]:
        return 1

    # 首先进行初始的排序    根据结束时间来排序
    intervals=sorted(intervals,key=lambda x:x[1])
    # 获取 所有范围时间点上的  房间安排初始设定
    record=[0 for _ in range(intervals[-1][1]+1)]


    # 进行时间点 安排情况的统计吧
    for interval in intervals:
        # 分别根据起始、终止时间点进行附加
        begin,end=interval[0],interval[1]
        # 这是个关键，起始时说明 占用，end时表示解除占用
        record[begin]+=1
        record[end]-=1

    # 最后直接做从起点开始的  累加统计即可.  这里会对每个时间点都记性统计，长度很长，但是因为有之前的+1  -1操作，这种统计是绝对有效的
    for i,x in enumerate(record):
        if i>0:
            record[i]+=record[i-1]

    return max(record)

fun1([[7,10],[2,4]])