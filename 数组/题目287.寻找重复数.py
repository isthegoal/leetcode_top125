# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
      假设只有一个重复的整数，找出这个重复的数。

         示例 1:
         输入: [1,3,4,2,2]
         输出: 2

         示例 2:
         输入: [3,1,3,4,2]
         输出: 3

         说明：
            不能更改原数组（假设数组是只读的）。
            只能使用额外的 O(1) 的空间。
            时间复杂度小于 O(n2) 。
            数组中只有一个重复的数字，但它可能不止重复出现一次。

      分析：


      思路：思路非常多，这里我使用两种吧，标记法和双指针法。
      【1】标记法，把每个元素的值当做指向下个元素的下标指针，因为有重复的元素，所以必然有至少两个元素的值相同，因此它们会指向同一个元素，
     所以可以从下标为i = 0的元素开始，依次访问对应的元素nums[i]，然后把nums[i]变成相反数，
     如果第一次访问，那么访问到的元素就是正数，
     如果不是第一次访问，那么访问到的元素就是负数, 代表i 就是重复的数，在下一次循环前更新 i 为nums[i]。
     注意这种方法修改了nums，虽然可以过OJ，但是不符合要求。

      【2】双指针法，把每个元素的值当做指向下个元素的下标指针，问题即可转化为链表的求环问题，
      分别设定一个快指针fast，一个慢指针slow，快指针一次走两步，慢指针一次走一步， 如果快慢指针重合了，就代表有环，
     此时，如果把fast重置为0，fast和slow每次走一步，那么它们下一次相遇的那个点就是环的起点。
'''
#标记法

class Solution1(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while (1):
            val = nums[i]
            if val > 0:
                nums[i] = -1 * nums[i]
                i = val
            else:
                return i

#双指针法
class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        slow, fast = 0, 0
        while (1):
            slow = nums[slow]
            fast = nums[nums[fast]]
            # print slow, fast
            if slow == fast:  # loop exists
                fast = 0
                while (nums[slow] != nums[fast]):
                    slow = nums[slow]
                    fast = nums[fast]
                    # print slow, fast
                return nums[fast]


#___________________________________    练习1   ______________________________#
#  这道题  极其简单，主要转换成链表上的求环问题进行求解，               把每个元素的值当做指向下个元素的下标指针
#  现在使用方法来找到环结点，训练环结点，就是最为常用的如下思路：
'''
分别设定一个快指针fast，一个慢指针slow，
     [1]快指针一次走两步，慢指针一次走一步， 如果快慢指针重合了，就代表有环，
     [2]此时，如果把fast重置为0，fast和slow每次走一步，那么它们下一次相遇的那个点就是环的起点。
    begin 吧.....
'''
#  空间复杂度为O(1)   时间复杂度为O(N)
def fun1(nums):
    slow,fast=0,0
    while 1:
        #获取  快慢指针 所指向的索引位置.   走一次和走两次的区别
        slow=nums[slow]
        fast=nums[nums[fast]]

        #当出现重合后
        if slow==fast:
            # 第二步骤了
            fast=0
            while(nums[slow]!=nums[fast]):
                # 接下来每次走一步吧
                slow=nums[slow]
                fast=nums[fast]

            #这就是最后知道重合的点，返回即可
            return nums[fast]