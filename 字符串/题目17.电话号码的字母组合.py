# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个仅包含数字 2-9 的字符串，返回电话按键上 所有它能表示的字母组合。

      输入："23"
      输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

      分析：

      思路：   线性扫描，读取k+1个数时，把前k个数的所有子集都新加入一个k+1，形成含有这个k+1的所有子集，再把它们放入result。
              对于每个数字的每个字符来说，把它加到目前已有的每个解里去， 暴力求解。

              这道题暴力解起来是相当简单的。  就是每次进行完全的候选呗，贼简单。
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        #这里注意res表示  已有的前置可选组合。
        res = []

        #对于所有的字符  进行暴力的拼接组合。
        for digit in digits:
            temp = []
            n = int(digit)
            #对于新的 按键上的字母，进行组合上的候选附加 append. 组成新的item + char，附加到temp中
            for char in mapping[n]:
                # print char
                if not res:
                    temp.append(char)
                else:
                    for item in res:
                        temp.append(item + char)
            res = temp
            # print res

        return res

#___________________________________    练习1   ______________________________#
#  思路 比较简单，进行不但的暴力的组合拼接到  temp中去。    进行多个数字形式上的遍历拼接。
# 时间复杂度为O(3^N),空间复杂度为O(3^N)
def letter_comb(digits):
    mapping={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
    # 用于收纳的数组
    res=[]

    #对于所有字符  进行暴力的所有情况的拼接组合
    for digit in digits:
        n=int(digit)
        temp=[]
        #对于键盘上的每个字符进行  组合上的附加，附加放置在temp中
        for char in mapping[n]:
            if not res:
                temp.append(char)
            else:
                # 注意 这里 res只会  在完成一个 整数字 遍历后才 进行保存的。 所以单数字上不会有自我重合
                for item in res:#(这里比较有意思的组合，是将该字符与  之前已经拼接好的字符组合到一起去。形成在该按键下新的拼接)
                    temp.append(item+char)
        res=temp

    return res
