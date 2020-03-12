# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
                输入: "abcabcbb"
                输出: 3
                解释: 因为无重复字符的最长子串是 "abc"

      分析：这里涉及到最长字串的问题，其实摆明的思路就是 使用双指针法， 这里打算使用双指针+ 滑动窗口的方式。


      思路：
         用双指针法 +  sliding window解题，start， end可以夹出一个window。
         用end线性遍历每个数组，用record记录下每个字母出现的最新的下标。
         当遇到一个新元素char在record里没有记录时，代表它没有跟window里的字母重复。
         如果在record里有记录，说明start需要刷新， 取当前start和record[char]里的最大值作为新的start即可。


'''
# 非常简单的一题，双指针 + 字典即可
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 这里字典的含义是核心，记录每个字母最后一次出现的下标,key是字母，val是下标
        record = dict()
        #res 表示对现有最大距离情况的保存。
        res, start = 0, 0
        for end in range(len(s)):
            #当单词之前出现过的话， 那么就需要重新标识下start起点位置了，
            if s[end] in record:
                start = max(start, record[s[end]] + 1)
            #不管之前见过 还是没见过，都需要更新字典了。
            record[s[end]] = end #刷新最新下标

            #这里end是截止到现有位置， 而start则表示 无重复的位置起点。   这两个的差值很good，就表示距离。
            res = max(res, end - start + 1)  #刷新res
        return res





#___________________________________    练习1    ______________________________#
'''
    思路特别直观简单，就是统一起点的两个指针，不但比较进行滑动即可
'''
def lls(s):
    res,start=0,0
    #进行 字母比较的字典库,  这里字典的含义是理解 本题的核心：    记录了 每个字母最后一次出现的下标  key是字母  value是下标
    record=dict()

    for end in range(len(s)):

        #主要就这一步，贼简单
        if s[end] in record:
            start=max(start,record[s[end]]+1) #如果之前已经出现过，就让前范围  往前挪一步。   但是如果重复的在start前面 既不理睬了呗

        record[s[end]]=end

        #最后返回比较的最大值即可
        res=max(res,end-start+1)
    return res

