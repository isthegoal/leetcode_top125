# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：汉明距离是使用在数据传输差错控制编码里面的，汉明距离是一个概念，它表示两个（相同长度）字对应位不同的数量，
      我们以d（x,y）表示两个字x,y之间的汉明距离。对两个字符串进行异或运算，并统计结果为1的个数，那么这个数就是汉明距离。

      分析： 定义如下。
      在信息论中，两个等长字符串之间的汉明距离是两个字符串对应位置的不同字符的个数。换句话说，它就是将一个字符串变换成
      另外一个字符串所需要替换的字符个数。例如：
        1011101 与 1001001 之间的汉明距离是 2。
        2143896 与 2233796 之间的汉明距离是 3。
        "toned" 与 "roses" 之间的汉明距离是 3



      思路：

'''
def hammingDistance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))
#___________________________________    练习1   ______________________________#
#这道题，贼简单，非常简单在 是相同长度的比较，  如果不是相同长度的话 ，可能就得使用些 编辑距离的思想了

def fun1(s1,s2):
    s1=str(bin(s1))
    s2 = str(bin(s2))
    # 先边界条件吧    这里使用异常机制，python会通过raise显示地引发异常
    if len(s1)!=len(s2):
        raise ValueError('Error length incorrect')
    # 接下来正式返回  差距长度。    这里会逐个按位置去对比，非常简单，精简的写法
    return sum(el1!=el2 for el1,el2 in zip(s1,s2))

#___________________________________    练习1（矫正）   ______________________________#
#   感觉题目好像跟leetcode不一样哎。
#   两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。给出两个整数 x 和 y，计算它们之间的汉明距离。
'''
        输入: x = 1, y = 4
        
        输出: 2
        
        解释:
        1   (0 0 0 1)
        4   (0 1 0 0)
               ↑   ↑
        
        上面的箭头指出了对应二进制位不同的位置。

'''

def hammingDistance1(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    # 先二进制上的^操作， 如果不一样为1
    n = x ^ y
    cnt = 0
    #  获得n之后，进行不断消除，来看有多少个1，完美
    while n:
        #n&(n-1) 用于消除最右边的1，可以看到将原来的最右边的1变为0了。重复操作，有多少个1，这个操作就可以执行多少次。
        n &= (n - 1)
        cnt += 1

    return cnt
hammingDistance1(1,4)