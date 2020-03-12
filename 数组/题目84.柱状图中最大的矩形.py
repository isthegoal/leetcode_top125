# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
            求在该柱状图中，能够勾勒出来的矩形的最大面积。

            例  输入: [2,1,5,6,2,3]
                输出: 10
      分析：

      思路：   可以利用递增栈找到矩形的左右边界。

'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        stack = list()
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[top])

            stack.append(i)
        return res
#___________________________________    练习1   ______________________________#
# 感觉这题 有些最大 储水池的思路，  只不过这里是携带 柱子体积下的计算。
#利用单调栈，这个栈里面只存储递增或者递减的数组（即这个柱状图的下标）
'''
用一个栈stack存储索引。
新的i在入栈前，先查看新的height[i]是否小于height[stack[-1]]：
[1]若大于，i入栈
[2]若小于，弹出栈顶元素index，令height[index]为高，i为右边界，当前栈顶部为左边界。计算其面积并更新最大面积max_area。


思考下过程 ，就能想明白 下面的思路了，很简单的，空间想象下，就用栈即可。

    题解中的一种说明：
    
    在这种方法中，我们维护一个栈。一开始，我们把 -1 放进栈的顶部来表示开始。初始化时，按照从左到右的顺序，我们不断将柱子的序号放进栈中，
    直到遇到相邻柱子呈下降关系，也就是 a[i-1] > a[i] 。现在，我们开始将栈中的序号弹出，直到遇到 stack[j]
    满足a[i]a[stack[j]]≤a[i] 。每次我们弹出下标时，我们用弹出元素作为高形成的最大面积矩形的宽是当前元素
    与 stack[top−1] 之间的那些柱子。也就是当我们弹出 stack[top] 时，记当前元素在原数组中的下标为 i ，当前
    弹出元素为高的最大矩形面积为：
    (i−stack[top−1]−1)×a[stack[top]].
    
    更进一步，当我们到达数组的尾部时，我们将栈中剩余元素全部弹出栈。在弹出每一个元素是，我们用下面的式子来求
    面积：(stack[top]−stack[top−1])×a[stack[top]]，
    其中stack[top]表示刚刚被弹出的元素。因此，我们可以通过每次比较新计算的矩形面积来获得最大的矩形面积。
    

    时间复杂度为O(n)。 n 个数字每个会被压栈弹栈各一次。
'''

def fun1(heights):
    # 这里stack是存储位置索引
    n=len(heights)
    heights=heights+[0]
    stack=[-1]
    max_area=0

    # 开始逐个入栈，并进行一定的判别。这样的弹出会一直进行，一直持续到满足a[stack[j]]≤a[i]
    for i in range(n+1):
        # 情况2，进行弹出高度，并进行计算。
        while heights[i]<heights[stack[-1]]:
            # 我在考虑 这个pop是真弹出来了吗？  pop之后stack[-1] 是不是变了,实验发现：确实变了。 但是无所谓，这里就是用的pop 得到的值计算高度
            h=heights[stack.pop()]
            # 总共宽度 ，  不断统计调整中
            w=i-stack[-1]-1

            max_area=max(max_area,h*w)
        # 情况1 下直接附加。 直接附加的是索引
        stack.append(i)

    return max_area
