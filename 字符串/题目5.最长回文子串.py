# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

            输入: "babad"
            输出: "bab"
            注意: "aba" 也是一个有效答案。


            输入: "cbbd"
            输出: "bb"

      分析： 比较好的思路是中心扩散法。分别做奇数和偶数两种情况遍历，中心向两端散开比较，获得最后substr。
             【1】中心扩散法：遍历所有的字符，遍历每个字符时，分两种情况，奇数个串（left=right），偶数个（right=left+1），

             分别做奇数和偶数两种情况遍历，中心向两端散开比较，获得最后substr。

             【2】动态规划法，s[l,r](二维，表示l到r之间是否为回文)s[l,r]=(s[l]s==s[r])and (s[l+1][r-1] or r - l <= 2)即s【l，r】为回文字符串，
             当且仅当s[l]==s[r]，并且其内部往前缩一步也是回文，或者l-1和r+1之间没有元素或者只有一个元素。

      思路：
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
            整体思路特别简单，就是以   一个字符为中心位置，  进行双向的扩展遍历。
            
            但是扩展时候需要考虑两个情况，
        
        '''
        max_l = 0
        res = ""

        #尝试遍历 以 所有字符为中心   进行遍历的效果。
        for i in range(0, len(s)):
            # 以s[i] 为中心向左右扩散   （考虑 奇数的情况left=right）， 这里目标就是获得最大的差距值  right - left + 1
            left, right = i, i
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                #当我们发现  不再具有中心扩散时 回文属性时，进行停止，统计现有最长情况吧。
                if max_l < right - left + 1:
                    max_l = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1

            # 以s[i],s[i+1]为中心向左右扩散（考虑 偶数的情况right=left+1）
            left, right = i, i + 1
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if max_l < right - left + 1:
                    max_l = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1
        return res


#___________________________________    练习1    ______________________________#
def fun1(s):
    # 首先是初始的全局定义，要收获的目标
    max_l=0
    res=''

    #从每个位置开始    进行两种情况的遍历， 分别是 奇数思考情况下的遍历   和  偶数思考情况下的遍历 (但是总感觉这个方法好冗余啊)
    for i in range(0,len(s)):

        #第一种 是奇数情况
        left,right=i,i
        while (left>=0 and right<len(s) and s[left]==s[right]):
            if max_l<right-left+1:
                max_l=right-left+1
                res=s[right:left+1]
            #对游标进行移动
            left-=1
            right+=1

        #第二种是偶数的情况
        left,right=i,i+1
        while (left>=0 and right<len(s) and s[left]==s[right]):
            if max_l<right-left+1:
                max_l=right-left+1
                res=s[right:left+1]
            #对游标进行移动
            left-=1
            right+=1
    return res


