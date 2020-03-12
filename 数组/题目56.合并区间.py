# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给出一个区间的集合，请合并所有重叠的区间。

        输入: [[1,3],[2,6],[8,10],[15,18]]
        输出: [[1,6],[8,10],[15,18]]
        解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].


        输入: [[1,4],[4,5]]
        输出: [[1,5]]
        解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

      分析：


      思路：

      先把intervals按照interval.start从小到大的顺序排好序，用left和right 作为当前的左端点和右端点，每次扫描到一个
      新的元素时item，如果item.start比right小，则说明当前的item可以被合并，新的合并区间的右端点应该为item.end和right的最大值，
      如果item.start比right大，则说明item不能被合并，需要将left和right添加到答案里，然后重置为item.start, item.end


'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x.start)
        res = []
        left = intervals[0].start
        right = intervals[0].end
        for item in intervals:
            if item.start <= right:
                right = max(right, item.end)
            else:
                res.append([left, right])
                left = item.start
                right = item.end
        res.append([left, right])

        return res

#___________________________________    练习1   ______________________________#
#  这点可能有点绕，   就是利用多个数组，左右边界的控制来不断的进行数组合并上的判别。
def fun1(intervals):
    #  边界条件，如空时控制
    if not intervals:
        return []

    # 对于  数组按照  其起点值进行排序，获得多个有序的数组。   数组位置上也是有序的那种，从而可以有效做 可合并条件判别。。。
    intervals = sorted(intervals, key=lambda x: x[0])

    # 创建 初始的用于判别的左右边界
    res = []
    left = intervals[0][0]
    right = intervals[0][-1]

    #  核心的，以一个数组开始，进行逐步的判断
    for item in intervals:
        # 可合并条件判别，可合并的情况, 那就贪心继续往下看
        if item[0] <= right:
            right = max(right, item[-1])
        else:
            # 当贪心下来，无法继续往下走时。   进行之前合并的保存和    新的索引位置更新
            res.append([left, right])
            left = item[0]
            right = item[-1]

    res.append([left, right])
    return res