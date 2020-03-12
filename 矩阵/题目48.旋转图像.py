# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个 n × n 的二维矩阵表示一个图像。将图像顺时针旋转 90 度。
      你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

      例1
      给定 matrix =
        [
          [1,2,3],
          [4,5,6],
          [7,8,9]
        ],

      原地旋转输入矩阵，使其变为:
        [
          [7,4,1],
          [8,5,2],
          [9,6,3]
        ]


      分析：


      思路：

            先转置再左右对称翻转。
            比如：
            输入为：[
              [1,2,3],
              [4,5,6],
              [7,8,9]
            ],
            转置可以得到:[
            [1,4,7],
            [2,5,8],
            [3,6,9],
            ]
            再对每一行进行翻转，即可得到答案:[
            [7,4,1],
            [8,5,2],
            [9,6,3],
            ]

'''


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 先转置再左右对称翻转
        if not matrix or not matrix[0]:
            return matrix
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            for i in range(n // 2):
                row[i], row[n - 1 - i] = row[n - 1 - i], row[i]

        return matrix

#___________________________________    练习1   ______________________________#
'''
      这里有个主要的问题 是进行  90度旋转时，只能从本身形式上进行调整，而不能使用其他的结构。
      
      这里基本的思路是  旋转的过程 不能一步而就，而是进行两步的过程。
          第一步：转置。
          第二步：左右对称翻转。
      可参考最上面的形式变换  来理解上面的两步骤。
'''
def fun1(matrix):
    # 边界条件：  对矩阵的判别
    if not matrix or not matrix[0]:
        return matrix

    # 获取的n是 行数也是 列数
    n=len(matrix)

    #  第一步: 进行转置操作吧,操作比较简答， 直接 轴的交换即可
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    # 第二步： 进行 对称翻转操作，很简单，针对于每一行row 进行交换吧 。   这里i序号是列内
    for row in matrix:
        for i in range(n//2):
            row[i],row[n-1-i]=row[n-1-i],row[i]

    #最后就是  两步操作的结果，非常简单
    return matrix

