# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：
            对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
            返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

            示例 1：
            输入：str1 = "ABCABC", str2 = "ABC"
            输出："ABC"

            示例 2：
            输入：str1 = "ABABAB", str2 = "ABAB"
            输出："AB"

            示例 3：
            输入：str1 = "LEET", str2 = "CODE"
            输出：""
 



      分析：
            简单理解下，目标就是找到S和T都能除尽的  最大公约数X。


            如果二者存在最大公因子，那，不就和求两个数字的最大公因数相似吗？
            那么，只需要求出两个字符串长度的最大公因数，然后返回相同长度的字串（从字符串起始位置开始）不就行了。
            所以啊，我将不存在公因数的字符串给筛出来之后，直接用辗转相除法不就行了吗？

            因此步骤就是：   做字符串筛选，筛选出 不存在公因数的字符串 ——> 对于存在的计算长度的最大公因数即可。——>从而得到公因长度。

      思路：
            本质是求解最大公约数。

            （1）从左向右遍历str1和str2，
            （2）如果str1和str2不等，直接返回“”               # 筛选出 不存在、不构成公因数的字符串
            （3）最终返回str1和str2长度 数字的最大公约数即可 【只要在长度上，获取到最大公约数即可？？？】

       有个疑问
         假如是‘ABAB’和‘ABAB’，结果不应该是'AB'吗？ 明白了，实际上，’AB‘确实是 ‘ABAB’和‘ABAB’的因子，但是‘ABAB’也是‘ABAB’和‘ABAB’的因子。
         而题目要求是找到最大公因子，所以应着这个'最大'，实际上题目要求的结果依然是'ABAB'

        为什么数字的最大公约数 就能代表字母的最大公约是？
           这个你想下就知道了，因为本身是按照一定循环的，有一定因子，所以那个数字求得的最大公因子，必然就是目标字符串的最大公因子，笔画下就知道了。



'''

def gcdOfStrings(str1, str2):
    #  一些条件的获取
    i = j = 0
    m, n = len(str1), len(str2)

    #  第（2）步，直接做str1和str2的逐个判别即可 ，非常简单的判别构成公因数
    if (str1 + str2) != (str2 + str1):
        return ''

    # 第（3）步，实现非常简单的 计算最大公约数的 函数，直接对数字做求取，用的经典的 欧几里得算法 求取数字最大公约数
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)


    return str1[:gcd(m, n)]


#print(gcdOfStrings("ABAB", "ABAB"))


def gcdOfStrings1(str1, str2):
    l1, l2 = len(str1), len(str2)

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    m = gcd(l1, l2)

    if (str1 + str2) == (str2 + str1):
        return str1[:m]
    return ""
print(gcdOfStrings1("ABAB", "ABAB"))
