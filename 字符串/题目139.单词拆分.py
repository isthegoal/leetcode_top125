# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中
      出现的单词。

         说明：拆分时可以重复使用字典中的单词。    你可以假设字典中没有重复的单词。
         示例 1：
            输入: s = "leetcode", wordDict = ["leet", "code"]
            输出: true
            解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。


      分析：


      思路：动态规划，用一个数组record记录切割字符串s时下刀的下标。
           每次刷新最远可以拆分的下标，最后判断一下是不是整个字符串都可以被拆分。

'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        record = [0]  # 一开始从开头开始找

        for j in range(len(s) + 1):
            for i in record:  # 在之前每一种找法的基础上找
                if s[i: j] in wordDict:  # 找到一种可行的分法，说明最远可以拆分到j
                    record.append(j)
                    break
        # print record
        return record[-1] == len(s)
