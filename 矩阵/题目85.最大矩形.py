# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
            示例:
                输入:
                [
                  ["1","0","1","0","0"],
                  ["1","0","1","1","1"],
                  ["1","1","1","1","1"],
                  ["1","0","0","1","0"]
                ]
                输出: 6

      分析：


      思路：   遍历每一行，在垂直放下进行相加，变成一维数组，利用84题的解法进行求解最大值

'''


class Solution(object):
    '''
    hard题，有点难，我选择看了youtube视频，学习可靠的方法。


    方法四：动态规划 - 每个点的最大高度直觉想象一个算法，对于每个点我们会通过以下步骤计算一个矩形：
不断向上方遍历，直到遇到“0”，以此找到矩形的最大高度。向左右两边扩展，直到无法容纳矩形最大高度。
例如，找到黄色点对应的矩形：

   我们知道，最大矩形必为用这种方式构建的矩形之一。
    给定一个最大矩形，其高为 h，左边界 l右边界 r,在矩形的底边，区间 [l, r]内必然存在一点，其上连续1的个数（高度）<=h。若该点存在，
    则由于边界内的高度必能容纳h，以上述方法定义的矩形会向上延伸到高度h，再左右扩展到边界 [l, r] ，于是该矩形就是最大矩形。
    若不存在这样的点，则由于[l, r]内所有的高度均大于h，可以通过延伸高度来生成更大的矩形，因此该矩形不可能最大。
    综上，对于每个点，只需要计算h， l，和 r - 矩形的高，左边界和右边界。
    使用动态规划，我们可以在线性时间内用上一行每个点的 h，l，和 r 计算出下一行每个点的的h，l，和r。

算法
        给定一行 matrix[i]，我们通过定义三个数组height，left，和 right来记录每个点的h，l，和 r。height[j] 对应matrix[i][j]的高，以此类推。
    问题转化为如何更新每个数组。Height:这个比较容易。 h 的定义是从该点出发连续的1的个数。我们从方法二中已经学会了在一行中计算的方法:
    row[j] = row[j - 1] + 1 if row[j] == '1'只需要一点改动即可:new_height[j] = old_height[j] + 1 if row[j] == '1' else 0

    Left:
        考虑哪些因素会导致矩形左边界的改变。由于当前行之上的全部0已经考虑在当前版本的left中，唯一能影响left就是在当前行遇到0。
    因此我们可以定义:new_left[j] = max(old_left[j], cur_left),cur_left是我们遇到的最右边的0的序号加1。当我们将矩形向左 “扩展” ，
    我们知道，不能超过该点，否则会遇到0。

    Right:
        我们可以沿用 left 的思路，定义:new_right[j] = min(old_right[j], cur_right),cur_right 是我们遇到的最左边的0的序号。简便起见，
        我们不把 cur_right 减去1 (就像我们给cur_left加上1那样) ，这样我们就可以用height[j] * (right[j] - left[j]) 而非height[j] * (right[j] + 1 - left[j])来计算矩形面积。
       这意味着， 严格地说 ，矩形的底边由半开半闭区间[l, r) 决定，而非闭区间 [l, r]，且 right比右边界大1。尽管不这样做算法也可以正确运行，但这样会让计算看起来更简洁。
       注意，为了正确的记录 cur_right，我们需要从右向左迭代。因此，更新right时需要从右向左。一旦left，right，和 height数组能够正确更新，我们就只需要计算每个矩形的面积。
       由于我们知道矩形 j的边界和高，可以简单地用height[j] * (right[j] - left[j])来计算面积，若j的面积 大于max_area，则更新之。


    时间复杂度 : O(NM)。每次对于N的迭代我们会对M迭代常数次。

    空间复杂度 : O(M）， M 是我们保留的额外数组的长度。

    如下是  DP动态规划方法，速度是相当快的。   看官方讲解中，有动态图展示   https://leetcode-cn.com/problems/maximal-rectangle/solution/zui-da-ju-xing-by-leetcode/

        【1】用height_j记录第i行为底,第j列高度是多少.

        【2】用left_j记录第i行为底, 第j列左边第一个小于height_j[j]的位置

        【3】用right_j记录第i行为底, 第j列右边第一个小于height_j[j]的位置


    '''
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        # 构建多重 状态载体
        m, n = len(matrix), len(matrix[0])
        left = [0] * n
        right = [n] * n
        height = [0] * n
        maxArea = 0

        for i in range(m):
            curleft = 0
            curright = n
            # 第一重动态规划情况的 设定。
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] = height[j] + 1
                else:
                    height[j] = 0

            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], curleft)
                else:
                    left[j] = 0
                    curleft = j + 1

            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curright)
                else:
                    right[j] = n
                    curright = j

            for j in range(n):
                maxArea = max(maxArea, height[j] * (right[j] - left[j]))

        return maxArea


#___________________________________    练习1   ______________________________#
'''
    矩形的面积等于h * w，分别找出h和w即可
                [
                  ["1","0","1","0","0"],
                  ["1","0","1","1","1"],
                  ["1","1","1","1","1"],
                  ["1","0","0","1","0"]
                ]

    1.计算h。针对于每一行分别计算h,
        row[i]是matrix的第i行，每行有n列，例如示例中，n=5,到达第i行时,
            当row[i][j] == '0' 时(其中0<=j<n)，h[j] = 0   （会抹杀前几层的累加）
            当row[i][j] == '1' 时(其中0<=j<n)，h[j] = row[i-1]的h[j] + 1
        例如，i = 2时，h = [3, 1, 3, 2, 2]，每一行都要求出h，一共求4组. 
        
    2.  对于单独行， 进行 直方图最大矩形面积   算法，会借助栈计算得到 最大矩阵面积。
        像极了84题：柱状图中最大的矩形.
        
    
    简单说：  就是从第二行开始都单独以 当前行为底，看做一个直方图， 来分别进行 直方图最大矩形面积 算法的计算。
              共进行 行数-1 次计算，从而统计除最大的 可行的矩阵面积。
              
    一直有个疑惑： 单独以某行为基底 作为直方图可以理解， 但是 有个问题是 会有悬浮，就是这个直方图中可能某个bar是 最上方才为1，而进行最大矩阵的计算需要 完整的组成矩形。
    所以我在思考，这个为题没影响吧，直接看做直方图的话，是跟 柱状图的样子稍微有区别的。
          解答：  原因在于这行代码 height[i] = height[i]+1 if row[i]=='1' else 0【核心】。 重点标记在于 else 0 。看到没，对于不符合直方图形状的会进行重置。
                 也就是 对于 最后一行，值为0的位置，默认有断层，看其他地方可以构成直方图的即可。  为0的都是断层，只在单高度上有效吧。
          

'''
class Solution1:
    def maximalRectangle(self, matrix):
        # 边界条件
        if not matrix or not matrix[0]:
            return 0
        # 初始定义变量。  列数n    转换的直方图高度数组height    统计的最大面积max_area
        n = len(matrix[0])
        height = [0] * (n+1)
        max_area = 0

        #  针对于 每一行，分别构建 直方图。
        for row in matrix:
            # （疑问在这里，为什么可以这样转换，原因是  else 0）计算出 单独当前直方图上的高度数组，比如 第三行，计算的结果就是  [3, 1, 3, 2, 2] 。 也是从第1行 第2行 的height累加过来的...
            for i in range(n):
                height[i] = height[i]+1 if row[i]=='1' else 0

            #############################       下面思路是计算直方图最大矩形面积的算法      ###########################
            #  接下来就是 题目84的思路了（直方图中的最大的矩阵的思路），针对于单独的直方图，进行内部最大面积的查找计算。
            # 找出所有h和w的组合    使用栈的结构，来获取 H，进行而在h的基础上，得到w
            stack = [-1]

            # 进行列数次，从左往右 查找
            for j in range(n + 1):
                while height[j] < height[stack[-1]]:
                    # 找出 h 和 w的集合，进而能求出 h*w 。 从而能比较出max
                    h = height[stack.pop()]
                    w = j - 1 - stack[-1]
                    max_area = max(max_area, h * w)

                stack.append(j)

        # 最后对多行做统计 的结果，获得即可
        return max_area



