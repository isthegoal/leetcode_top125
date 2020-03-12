# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
      在坐标内画 n条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。


            示例
                输入: [1,8,6,2,5,4,8,3,7]
                输出: 49

      分析：基本思路就是双指针法，之前思考过这一问题。

      思路：双指针法。
           每次循环二者中高度小的那个指针往中心移动，因为这样可以抵消宽度减小带来的影响，更有可能得到面积更大的矩形。

'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #很好记忆的双指针法，一个是低位指针，一个是高位指针。
        lo, hi = 0, len(height) - 1
        #在每次移动后，都会去统计现在值是否是最大的。
        res = 0
        while (lo < hi):
            #这里思想贼为简单，就是两个指针对应的高度，谁小谁往里面移动【这个是核心思想，也能推猜明白吧】，同时也记录现有情况下的  最大容量面积值。
            if height[lo] > height[hi]:
                area = height[hi] * (hi - lo)
                hi -= 1
            else:
                area = height[lo] * (hi - lo)
                lo += 1
            # 去做统计吧
            res = max(area, res)

        return res
#___________________________________    练习1   ______________________________#
#贼简单的 双指针法，进行容量判别即可。 (注意这里的 要求是比较简单的，是找到构成最大容器的两条线，  两条线这个是重点)
def fun1(height):
    #定义两个指针
    lo,hi=0,len(height)-1
    #统计最大的容量  ,由外往内缩，找最大的  （清晰的思路、逻辑能力和想象力）
    res=0
    while(lo<hi):
        if height[lo]>height[hi]:
            area=height[hi]*(hi-lo)
            hi-=1
        else:
            area=height[lo]*(hi-lo)
            lo+=1
        res=max(area,res)
    return res
