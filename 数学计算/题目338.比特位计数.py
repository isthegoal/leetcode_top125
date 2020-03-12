# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

        示例 1:
        输入: 2
        输出: [0,1,1]

        示例 2:
        输入: 5
        输出: [0,1,1,2,1,2]

      分析：


      思路：有三种思路吧
      【1】麻瓜思路。从0到num，每个数都按照常规方法（不断除以2）求其二进制中有多少个1
      【2】如果一个数 i 和 i - 1 做与运算，那么 i 的二进制表示形式中的最右边一个 1 会变成0 。根据这个结论可以优化统计
      每个数中 1 的个数的函数getOne。
      【3】在第二种思路的基础上，利用动态规划的思想。
      如果我们已经知道了 i & i -1 这个数字的1的个数cnt，那么根据上面的提到的结论， i 这个数字中 1 的个数就是 cnt + 1。
      所以不难得到状态转移方程： dp[i] = dp[i &  (i - 1)] + 1
'''
#  方法一
class Solution1(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = list()
        for i in range(num + 1):
            res.append(self.getOne(i))

        return res

    def getOne(self, n):
        binary = list()
        while (n >= 2):
            binary.append(n % 2)
            n = n // 2
        binary.append(n)
        # print binary
        return sum(binary)
#  方法二
class Solution2(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = list()
        for i in range(num + 1):
            res.append(self.getOne(i))

        return res

    def getOne(self, n):
        cnt = 0
        while (n):
            cnt += 1
            n = n & (n - 1)
        return cnt
#  方法三
class Solution3(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0 for i in range(num + 1)]
        for i in range(1, num + 1):
            dp[i] = dp[i & (i - 1)] + 1

        return dp

#___________________________________    练习1   ______________________________#
# 一样的，其实直观理解，最简单的就是麻瓜思想，但是比较有趣的，高效的还是 动态规划思想吧，这里用动态规划。
#num是 要进行统计的数字
def fun1(num):
    #定义状态值，每个状态值都是最终目的，对数字包含1个数情况的表示
    dp=[0 for i in range(num+1)]
    # 进行状态转移，这里使用了很好的  位统计的方式i & (i - 1)
    '''
        &是按位与，对应位都为1时该位得1，否则得0。
        所以 i&(i-1) 的作用：将i的二进制表示中的最低位为1的改为0。
    '''
    for i in range(1,num+1):
        #主要利用上面的特性，从而 dp包装下就是 少了一个1 的统计，  所以后面再加个1.
        dp[i]=dp[i&(i-1)]+1

    return dp

