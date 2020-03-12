# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

            '.' 匹配任意单个字符
            '*' 匹配零个或多个前面的那一个元素
            所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

            输入:
            s = "aa"
            p = "a"
            输出: false
            解释: "a" 无法匹配 "aa" 整个字符串

            s = "ab"
            p = ".*"
            输出: true
            解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

      分析：这里是需要用 p去匹配s,而其p内的字符是特殊含义的正则字符。


      思路：使用动态规划的方式，在递归中加入了备忘录。
         https://leetcode-cn.com/problems/regular-expression-matching/solution/ji-yu-guan-fang-ti-jie-gen-xiang-xi-de-jiang-jie-b/
'''


#   解法一. 递归解法
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #递归的结束条件，当p和s都为空时候，匹配完成
        if not p:
            return not s

        #第一层考虑， 是考虑首字母的合法性，首字母 是完全匹配的或者是  . 这个特殊符号均可。
        match = s and p[0] in [s[0], "."]

        #第二层考虑，主要是对*符号的考虑
        if len(p) > 1 and p[1] == "*":
            # 这里就是利用到*号的特性进行递归，
            return self.isMatch(s, p[2:]) or (match and  self.isMatch(s[1:], p))

        return match and self.isMatch(s[1:], p[1:])


#___________________________________    练习1   (这个理清楚还是有难度的) ______________________________#
def match1(s,p): #p是正则模板，s是用于匹配的字母
    #可行的  完全匹配的结束条件判别
    if not p:
        return not s
    # 这里是针对于较为特殊的首字母进行考虑。
    match=s and p[0] in [s[0],'.']

    #  特殊的针对于*利用上的思考，因为*号是一种绝对的匹配吧，
    if len(p)>1 and p[1]=='*':
        return match1(s,p[2:]) or (match and match1(s[1:],p)) #这个不好理解，是本问题解法的核心所在  (and含义是两者相等 1 and 2为1，1 and 0 为0)


    # 针对于非首字母进行思考
    return match and match1(s[1:],p[1:])


