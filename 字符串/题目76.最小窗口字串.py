# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

      示例：
        输入: S = “ADOBECODEBANC”, T = “ABC”
        输出: “BANC”

      分析：这题也是可以看做字符数组吧，然后可以针对数组，使用双指针法进行解决。
             这里的核心就是对 窗口的左扩展 和右扩展的过程。首先右扩展，扩展到可行解后， 然后左缩，同时记录最小长度值。
                最后继续让左指针左走从而破坏 可行情况，然后同步的让右指针右移，从新找到可行解。
                不断  持续到right到头即可。

      思路（极其简单的思路方式）：
           可以使用如下四步的方法：
            1.初始，left指针和right指针都指向S的第一个元素.
            2.将 right指针右移，扩张窗口，直到得到一个可行窗口，亦即包含t的全部字母的窗口。
            3.得到可行的窗口后，将left指针逐个右移，若得到的窗口依然可行，则更新最小窗口大小。
            4.	若窗口不再可行，则跳转至 2。

'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # 第一步，将  要寻找的被包含信息存放到字典中
        dic = {}
        for i in t:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1

        #  定义好指针和变量
        start = 0
        minlen = len(s)
        cnt = 0
        result = ""
        for i in range(len(s)):

            # 一个启动条件，当现在走到的字符在  目标字符 中时，我们再进行考虑。  这里for的遍历其实就相当于一种right的右移。
            if (s[i] in t):
                dic[s[i]] -= 1
                #对出现情况进行统计，在这个范围内有合适的累计
                if dic[s[i]] >= 0:
                    cnt += 1

                #核心的，当我们发现现在是合法合理时，就可以考虑  对于left和right指针进行左移和右移的问题，先left左移，一直到不满足条件为止吧
                while (cnt == len(t)):

                    # 重要的 当找到新的最小窗口时，思考进行结果的保存
                    if (i - start + 1) <= minlen:
                        minlen = i - start + 1
                        result = s[start:i + 1]

                    #进行start和end的调整，让start往前缩
                    start += 1
                    if s[start - 1] in t:
                        dic[s[start - 1]] += 1
                        if dic[s[start - 1]] > 0:
                            cnt -= 1
        return result
#___________________________________    练习1   ______________________________#
import collections
#找到包含另一个 字符串的  最小字串。   基本方法就是所谓的双指针套路  (核心是遵从上面所说的四个步骤)。
def fun1(s,t):#s 是用于寻找的长字符，t是 用于比对的模板字符。
    res=''
    #这里含义上，left和right是两个指针、minLen是匹配窗口最小长度、cnt表示现有匹配长度（cnt的含义是在s[left, right]区间内，和t的相等的字符个数统计）。
    left,right,cnt,minLen=0,0,0,float('inf')
    #一种容器，collections模块包含了除list、dict、和tuple之外的容器数据类型，如counter、defaultdict、deque、namedtuple、orderdict,一种字典形式吧
    #这里  defaultdict是一个使用int类型初始化的字典，Counter是一个简单的键值对的容器。  这里容器的键值对表示 字母在窗口中的包含信息，1为包含 0为不包含。
    tcount=collections.Counter(t)
    scount=collections.defaultdict(int)

    #进行指针的游走和探索。       首先是right的右移
    while right<len(s):
        scount[s[right]]+=1

        #如果right指针右移过程中，都是合适的包含t字符时， 那就继续往右扩张
        if s[right] in tcount and scount[s[right]]<=tcount[s[right]]:
            cnt+=1

        #当 现在的扩张得到可行的窗口时，尝试进行最小窗口的更新，以及left左移的尝试。
        while left<=right and cnt==len(t):
            if minLen>right-left+1:
                minLen=right-left+1
                res=s[left:right+1]
            scount[s[left]]-=1
            #当有不满足 合法窗口条件时，那就退出左移即可。
            if s[left] in tcount and scount[s[left]]<tcount[s[left]]:
                cnt-=1
            left+=1
        right+=1
    return res





