# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

      示例:
      输入: [0,1,0,2,1,0,1,3,2,1,2,1]
      输出: 6  （看图会更清晰）

      分析：

      思路：对于数组中的每个元素，我们找出下雨后水能达到的最高位置，等于两边最大高度的较小值减去当前高度的值。

      
      每个位置上积水的高度，应该等于min（左边最高的柱子高度，右边最高的柱子高度）-这个位置上的柱子高度。
     【1】所以先从左往右遍历把left_max数组生成，left_max[i]代表 height[i] 及其左侧最高的柱子高度。
     【2】同理生成right_max。
     【3】然后再遍历一次对于每个位置计算min(left_max[i], right_max[i]) - height[i]就好了  【为什么这样的计算 能代表，这是个核心。】

'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #这三个数组的含义至关重要，分别是左边最大、右边最大、在此位置上的可储水情况
        left_max = [0 for _ in height]
        right_max = [0 for _ in height]
        water = [0 for _ in height]

        # 对应于第一步，从左往右，用来生成 left_max
        for i in range(len(height)):
            if i - 1 >= 0:
                left_max[i] = max(left_max[i - 1], height[i])
            else:
                left_max[i] = height[i]

        # 对应第二步，从右往左，用于生成right_max
        for i in range(len(height) - 1, -1, -1):
            if i < len(height) - 1:
                right_max[i] = max(right_max[i + 1], height[i])
            else:
                right_max[i] = height[i]

        # 第三步是 对于每个位置都计算 min(left_max[i], right_max[i]) - height[i]），作为需要的目标
        for i in range(len(height)):
            tmp = min(left_max[i], right_max[i]) - height[i]
            if tmp > 0:
                water[i] = tmp
        # print height
        # print water
        # print left_max
        # print right_max
        return sum(water)


#___________________________________    练习1   ______________________________#
# 计算接雨水，这个很明显的，第一直接，就是  双指针法就行     这个跟呈最多水  有些不同
'''
  这里也是大致使用   
      每个位置上积水的高度，应该等于min（左边最高的柱子高度，右边最高的柱子高度）-这个位置上的柱子高度。
      这个是最基本的思路，要想明白，想清楚，是这样子的。 {明白了，自己看下储水图 就知道了，真正存水的是 柱子之间，而不是柱子本身，看一下储水图，就明白了，需要这样的坐看和右看，再做决定。}
     【1】所以先从左往右遍历把left_max数组生成，left_max[i]代表 height[i] 及其左侧最高的柱子高度。
     【2】同理生成right_max。
     【3】然后再遍历一次对于每个位置计算min(left_max[i], right_max[i]) - height[i]就好了
'''
#  储水池   数组height。  可以从中得知储水情况
def fun1(height):
    # 这三个数组的含义至关重要，分别是左边最大、右边最大、在此位置上的可储水情况   (这里想明白为什么要  创建这三个数组是个主要的点)
    #分别的表示 从左往右  和 从右往左调整趋势 的统计
    left_max = [0 for _ in height]
    right_max = [0 for _ in height]
    water = [0 for _ in height]

    #
    # 对应于第一步，从左往右，用来生成 left_max
    for i in range(len(height)):
        if i - 1 >= 0:
            left_max[i] = max(left_max[i - 1], height[i])
        else:
            left_max[i] = height[i]
    # 对应于第二步，生成右侧的最大值， 从右到左过来的观察。  right_max
    for i in range(len(height) - 1, -1, -1):
        if i < len(height) - 1:
            right_max[i] = max(right_max[i + 1], height[i])
        else:
            right_max[i] = height[i]
    # 最后得到每个位置的  高度，此外   因为宽度是1，所以直接就按高度算就行了。

    for i in range(len(height)):
        tmp = min(left_max[i], right_max[i]) - height[i]
        if tmp > 0:
            water[i] = tmp

    return sum(water)





