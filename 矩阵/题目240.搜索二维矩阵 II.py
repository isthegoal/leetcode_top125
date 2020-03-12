# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
            每行的元素从左到右升序排列。
            每列的元素从上到下升序排列。


            示例:
                现有矩阵 matrix 如下：

                [
                  [1,   4,  7, 11, 15],
                  [2,   5,  8, 12, 19],
                  [3,   6,  9, 16, 22],
                  [10, 13, 14, 17, 24],
                  [18, 21, 23, 26, 30]
                ]
                给定 target = 5，返回 true。
                给定 target = 20，返回 false。


      分析：


      思路：有两个解法吧。
       【1】暴力搜索，直接扫描二维矩阵的全部元素，看能不能找到target。
       【2】根据题意，每一行的第一个数字是这一行最小的数，每一列的最后一个数字是这一列最大的数，所以不妨从矩阵的左下角出发，
        如果target比当前元素小，则说明target肯定不在这一行，因为 每一行的第一个数字是这一行最小的数，
    因此最后一行可以被去掉。如果target比当前元素大，则说明target肯定不在这一列，因为 每一列的最后一个数字是这一列最大的数，
    因此第一列可以被去掉。按照以上步骤依次处理，如果最后矩阵都为空了，还没有找到target，就说明target不存在于matrix中。


'''

#解法一
class Solution1(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False

#解法二
class Solution2(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])

        i, j = m - 1, 0
        while 0 <= i < m and 0 <= j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False

#___________________________________    练习1   ______________________________#
'''
    感觉这就是一道原题吧，根据 矩阵的 位置上的大小比较关系，进行高效大的二维数值上的数字查找。
              [
                  [1,   4,  7, 11, 15],
                  [2,   5,  8, 12, 19], 
                  [3,   6,  9, 16, 22],       右下大于左上
                  [10, 13, 14, 17, 24],
                  [18, 21, 23, 26, 30]
                ]
  
     强行分治法。 从左下角开始寻找，不断缩小探索矩阵，每次移动后，都看作新的矩阵下的左下角。因为左下角的元素是这一行中最小的元素，同时又是这一列中最大的元素。最大的元素。
     比较左下角元素和目标：
        [1]若左下角元素等于目标，则找到
        [2]若左下角元素大于目标，则目标不可能存在于当前矩阵的最后一行，问题规模可以减小为在去掉最后一行的子矩阵中寻找目标
        [3]若左下角元素小于目标，则目标不可能存在于当前矩阵的第一列，问题规模可以减小为在去掉第一列的子矩阵中寻找目标
        [4]若最后矩阵减小为空，则说明不存在

'''
#  matrix 是有一定大小关系的矩阵，target是目标查找值。
def fun1(matrix,target):
    # 获取行数，并进行边界条件判别,0是 矩阵不存在的
    m = len(matrix)
    if m == 0:
        return False

    # 同上，针对列，但是这里必须要错开，因为首先要保证matrix[0] 存在才行。
    n = len(matrix[0])
    if n == 0:
        return False

    # 设定开始于 左上角的坐标位置
    i=m-1
    j=0

    while i>=0 and j<n:
        # 对应 [1]情况
        if matrix[i][j]==target:
            return True
        #对应 [3]情况的，挪动，往右走一步，缩小范围了。
        elif matrix[i][j]<target:
            j+=1
        # 最后对应 【2】情况，往上走一步，搜小范围
        else:
            i-=1

    # 最后如果都找不到，那就false吧
    return False



