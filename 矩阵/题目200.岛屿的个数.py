# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或
      垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

        例如输入:
        11110
        11010
        11000
        00000

        输出: 1

      分析：

      思路：
         一种直接的思路是用DFS + visited数组保存去过的点。
         另一种是较为经典的DFS+染色法的思想。扫描输入，如果扫到“1”，就先把它变成“0”，然后递归地把跟它相连的点都变成“0”，
        此题坑点在于LeetCode网站上输出会自动变成u"1", 解决办法是不要和“1”比，而是和“1”.encode("utf-8")做匹配。

'''


# -*- coding: utf-8 -*-
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1".encode('utf-8'):
                    print(i, j)
                    island += 1
                    self.checkNearbyIsland(grid, i, j)
                    # print island
        return island

    def checkNearbyIsland(self, grid, i, j):
        rows = len(grid)
        columns = len(grid[0])
        print(i, j)
        if i > rows - 1 or j > columns - 1 or i < 0 or j < 0 or grid[i][j] == "0".encode('utf-8'):
            return

        if grid[i][j] == "1".encode('utf-8'):
            grid[i][j] = "0"
            # print grid
            self.checkNearbyIsland(grid, i + 1, j)
            self.checkNearbyIsland(grid, i, j + 1)
            self.checkNearbyIsland(grid, i - 1, j)
            self.checkNearbyIsland(grid, i, j - 1)


'''
   方法一.深度优先遍历DFS
   1.目标是找到矩阵中 “岛屿的数量” ，上下左右相连的 1 都被认为是连续岛屿。
   2.dfs方法： 设目前指针指向一个岛屿中的某一点 (i, j)，寻找包括此点的岛屿边界。
        (1)从 (i, j) 向此点的上下左右 (i+1,j),(i-1,j),(i,j+1),(i,j-1) 做深度搜索。
        (2)终止条件：
            (i, j) 越过矩阵边界;
            grid[i][j] == 0，代表此分支已越过岛屿边界。
        (3)搜索岛屿的同时，执行 grid[i][j] = '0'，即将岛屿所有节点删除，以免之后重复搜索相同岛屿。
   3.主循环：
        (1)遍历整个矩阵，当遇到 grid[i][j] == '1' 时，从此点开始做深度优先搜索 dfs，岛屿数 count + 1 且在深度优先搜索中删除此岛屿。
   4.最终返回岛屿数 count 即可。

'''
class Solution1:
    def numIslands(self, grid: [[str]]) -> int:
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count
#___________________________________    练习1   ______________________________#
#  这里是找到  被水域阻断的 岛屿的数量， 使用DFS方法进行解决。
'''
    基本思路：   就是针对每个可能点，启动DFS岛屿探索操作。对于每个可能点操作：
                      一方面对四周做DFS扩展，同时对于遍历到的 为1位置，设置成0，从而 一次大得DFS其实就把整个岛屿都染成0。 count+1
                      
                      然后再 针对染好的网格，再进行 一次大得DFS操作，重新查找潜在岛屿并染色，持续多次大的DFS，从而得到最终结果。

'''
def fun1(grid):
    count=0

    #针对  网格中的每个位置，都进行dfs搜索
    for i in range(len(grid)):
        for j in range(len(grid)):
            #当是可以探索的 陆地是，进行dfs操作  。 这里在走到一个陆地上时，其实就会把这整个岛屿都会变成'0'标记，所以这里 count累加的就是独立岛屿数量（这个是理解的核心）
            if grid[i][j]=='1':
                dfs(grid,i,j)
                count+=1

    return count

# 内部 DFS探索操作
def dfs(grid,i,j):
    # dfs的三个截止条件。     i 和  j在边界内，同时如果是水区，那就结束搜索吧。
    if not 0<=i<len(grid)   or   not 0<=j<len(grid[0])    or    grid[i][j]=='0':
        return

    # 对已经行走过的，设置0，放置重复的行走 （就需要这样的操作，因为不会还原，就可以从一个 岛屿点开始，就能蔓延得将整个岛屿都变成'0'，从而count+=1操作在每个岛屿中，只会加一次）
    grid[i][j]='0'

    #往四周  进行dfs搜索操作吧   。   这里也匹配岛屿的定义，以这个探索单位 看没有相近的陆地  那就是岛屿了（可以画下dfs的蔓延图 就能明白了，很简单）
    dfs(grid, i + 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i - 1, j)
    dfs(grid, i, j - 1)



