# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

                输入:
                ["eat", "tea", "tan", "ate", "nat", "bat"]
                ,
                输出:
                [
                  ["ate","eat","tea"],
                  ["nat","tan"],
                  ["bat"]
                ]

                所有输入均为小写字母。
                不考虑答案输出的顺序。

      分析：这里的方法是非常简单的，就是将由相同字母组成的 字符串合到一个数组中去，直接使用创建一个字典的方式就可以搞定。
         字典形式为： {经过 tuple(sorted(word))转换包装过的元组  ：  {所有对应该元组情况的字符串} }

          然后 不断遍历和  收集字符串即可


      思路：
            建立hashmap，key是sorted（s），values是排序后相同的s的list。
            比如： [ “aet” : ["ate","eat","tea"], "ant": ["nat","tan"], "abt" : ["bat"] ]

'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        record = dict()

        for word in strs:
            # 用来作为键值的信息，    首先按照字符特点进行展示吧，这个就可以看做是核心吧，只要设置好进行归属用的键即可.....
            tmp = tuple(sorted(word))
            # print tmp
            if tmp in record:
                record[tmp].append(word)
            else:
                record[tmp] = [word]
        return [val for key, val in record.items()]


#___________________________________    练习1   ______________________________#
# 感觉是一种判别并分合的过程。       将基于相同字母组合、但是相互异位的一些词合在一起,从而返回的是多个列表。
def fun1(strs):
    #  进行  异位数组的查找和收集，  非常简单。     就是键值对的方式即可，键是 字符组合，值是 收集的列表。
    record=dict()

    #  现在往字典中进行  组合收集数据即可
    for word in strs:
        tmp=tuple(sorted(word))

        if tmp in record:
            record[tmp].append(word)
        else:
            record[tmp]=[word]

    #  接下里 针对所有的value  放置在一起
    return [val for key,val in record.items()]

