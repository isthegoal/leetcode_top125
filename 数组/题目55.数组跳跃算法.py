# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给一个list，数组中的每个值表示在当前位置最多能向前面跳几步，判断给出的数组是否否存在一种跳法跳到最后。

      注意点：
        所有的数字都是正数
        跳的步数可以比当前的值小

            例1
            Input: [2,3,1,1,4]
            Output: true
            Explanation: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。

            例2
            Input: [3,2,1,0,4]
            Output: false
            Explanation: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ，
            所以你永远不可能到达最后一个位置。


      分析：能否跳跃到最后一个位置的关键是跳跃的时候能否避开位置在1到n-2（n为数组长度）之间且值为0的点，
      所以此问题可转化为求1到n-2之间值为0点的前面是否存在能够避开该点的值。


      思路：
      如果所有元素都不为0， 那么一定可以跳到最后；
      从后往前遍历，如果遇到nums[i] = 0，就找i前面的元素j，使nums[j] > i - j。如果找不到，则不可能跳到num[i+1]

      直接的贪婪算法即可
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cover = 0
        for i,x in enumerate(nums):
            if cover >= len(nums)-1:
                return True
            if cover >= i:
                cover=max(cover,nums[i]+i)
        return False

#___________________________________    练习1   ______________________________#
#  根据指定的数组，在位置上可以控制最多可以往前跳跃的长度。              让判断给出的数组是否否存在一种跳法跳到最后。
def fun1(nums):
    if len(nums) == 1:
        return True

    max_Jump = 0  # 记录当前能到达的最大的位置
    for i in range(len(nums) - 1):
        if i > max_Jump:  # 如果当前能到达的最大的位置的都到达不了，那么就结束了
            return False

        max_Jump = max((i + nums[i]), max_Jump)  # 当前最大的位置可能是之前能跳到的最大的位置，也可能是当前最大的能跳到的位置

        if max_Jump >= len(nums) - 1:  # 能跳到最后，成功
            return True

    return False
