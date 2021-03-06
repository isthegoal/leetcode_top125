
'''
      题目：排排坐，分糖果。

            我们买了一些糖果 candies，打算把它们分给排好队的 n = num_people 个小朋友。
            给第一个小朋友 1 颗糖果，第二个小朋友 2 颗，依此类推，直到给最后一个小朋友 n?颗糖果。
            然后，我们再回到队伍的起点，给第一个小朋友 n?+ 1 颗糖果，第二个小朋友 n?+ 2 颗，依此类推，直到给最后一个小朋友 2 * n?颗糖果。
            重复上述过程（每次都比上一次多给出一颗糖果，当到达队伍终点后再次从队伍起点开始），直到我们分完所有的糖果。注意，
            就算我们手中的剩下糖果数不够（不比前一次发出的糖果多），这些糖果也会全部发给当前的小朋友。
            返回一个长度为 num_people、元素之和为 candies 的数组，以表示糖果的最终分发情况（即 ans[i] 表示第 i 个小朋友分到的糖果数）。

?

            示例 1：

                输入：candies = 7, num_people = 4
                输出：[1,2,3,1]
                解释：
                第一次，ans[0] += 1，数组变为 [1,0,0,0]。
                第二次，ans[1] += 2，数组变为 [1,2,0,0]。
                第三次，ans[2] += 3，数组变为 [1,2,3,0]。
                第四次，ans[3] += 1（因为此时只剩下 1 颗糖果），最终数组变为 [1,2,3,1]。


      分析：

      思路：  一道easy题，是非常简单，不断写循环，并进行糖果的判别和克扣就可以，正儿八经的思维方法。  没使用额外空间
'''
#___________________________________    练习1   ______________________________#
class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        #  非常简单的逻辑推算题

        # 初始的 分配数量定义
        re = [0 for i in range(num_people)]
        cur = 1

        # 直到没糖果为止，这里进行不但的附加。
        while candies:
            for i in range(num_people):
                # 当能支撑分配时，开始进行不断地循环的 re[i] 上糖果的附加。
                if candies >= cur:
                    re[i] += cur
                    candies -= cur
                # 这个else 就是表示糖果不足够合理的 分配时，  进行退出即可，是截止条件
                else:
                    re[i] += candies
                    candies = 0
                cur += 1
        return re