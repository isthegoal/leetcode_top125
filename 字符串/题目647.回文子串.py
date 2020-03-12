# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。【leetcode原题】
            具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

            示例 1:
            输入: "abc"
            输出: 3
            解释: 三个回文子串: "a", "b", "c".

            示例 2:
            输入: "aaa"
            输出: 6
            说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".

      分析：


      思路：主要两种思路吧，这个也是原题，包括动态规划法 和  中心扩散法。
         [1]动态规划法。动态规划，用dp[i][j]记录下s[i : j+1]是否是回文子串，如果是则dp[i][j] = 1, 不是则dp[i][j] = 0。
     注意，如果i - j <= 1，则说明子串长度为0或者1，所以无需考虑dp[i - 1][j +1]。


         [2]中心扩散法。中心扩散法，从长度为1的子串为中心向两边扩散，分别判断以 s[i]为中心的子串和以s[i], s[i+1]为中心
         的子串是不是回文子串。

'''
# 第一种方法
class Solution1(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dp[i][j] 表示s[i:j+1] 是否为回文串
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        res = 0
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j <= 1 or dp[i - 1][j + 1]): #当i - j<=1时 不需要考虑dp[i-1][j+1]
                    dp[i][j] = 1
                    res += 1
        return res


#第二种方法。  中心扩散法
class Solution2(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.res = 0

        def extend(left, right):
            for i in range(len(s)):
                while (left >= 0 and right < len(s) and s[left] == s[right]):
                    self.res += 1
                    left -= 1
                    right += 1

        for i in range(len(s)):
            extend(i, i)
            extend(i, i + 1)

        return self.res

#___________________________________    练习1   ______________________________#
#这里  并不是传统的简单判断是否是回文子串， 而是 进行有多少回文子串的判别。
def fun1(s):
    res = 0

    # 内部的进行回文子串判断的函数
    def extend(left, right, res):
        for i in range(len(s)):

            # 进行单个回文获取的函数，aaa可以扩展出  a  aa aaa  注意这里每次都是双向的同时扩展，左与右。 （可以单步和多步，这里的aa进行统计的方式是 下面的那种获得的（i,i+1））
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                res += 1
                left -= 1
                right += 1
        return res

    # 启动函数，从左往右，相当于新的 进行回文情况的扩展探索。  这里不用考虑重复的问题，反正最少有一个是满足回文的，到扩展失败为止，注意这里有两个
    for i in range(len(s)):
        res = extend(i, i, res)
        res = extend(i, i + 1, res)
    return res

