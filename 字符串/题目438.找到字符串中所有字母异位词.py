# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
            字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

           示例 1:
            输入:
            s: "cbaebabacd" p: "abc"
            输出:
            [0, 6]
            解释:
            起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
            起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

      分析：


      思路：使用固定长度的sliding window。带动态规划思想的比较方法，移动时不再比较整个substring，
      而是根据变化的局部来调整。

'''


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = list()
        ls, lp = len(s), len(p)
        if lp > ls:
            return list()

        lo, hi = 0, lp - 1
        s1 = [0 for _ in range(26)]
        s2 = [0 for _ in range(26)]

        for i in range(lp):
            s2[ord(p[i]) - 97] += 1

        for i in range(lp - 1):
            s1[ord(s[i]) - 97] += 1

        for i in range(ls - lp + 1):
            s1[ord(s[i + lp - 1]) - 97] += 1

            if s1 == s2:
                res.append(i)

            s1[ord(s[i]) - 97] -= 1

        return res
#___________________________________    练习1   ______________________________#
#  p是用于寻找异位词的模板
#  这里的解决方法，主要是用到了   字母的ascii码进行排序后的组合比较
def fun1(s,p):
    res=list()
    ls,lp=len(s),len(p)
    if lp>ls:
        return list()

    # 这里s1和s2是对字母的出现情况的统计，s1表示对于 长字符串的字母情况统计，s2是对模板字符串的字幕情况统计。
    lo,hi=0,lp-1
    s1=[0 for _ in range(26)]
    s2=[0 for _ in range(26)]

    # 对于字母的 出现情况统计  （先是初始统计 前  lp个字符的情况，来寻找 完全匹配的异位词）
    for i in range(lp):
        s2[ord(p[i])-97]+=1
    for i in range(lp-1):
        s1[ord(s[i])-97]+=1

    #统计在 lp个字符之后的字符  组合上的出现情况，这里  会累计s1， 将其与模板s2上的出现情况进行对比。
    for i in range(ls-lp+1):
        s1[ord(s[i+lp-1])-97]+=1

        #当出现异位词  完全匹配时
        if s1==s2:
            res.append(i)
        s1[ord(s[i])-97]-=1
    return res