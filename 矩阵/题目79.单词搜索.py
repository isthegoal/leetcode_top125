# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个二维网格和一个单词，找出该单词是否存在于网格中。

      单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
      同一个单元格内的字母不允许被重复使用。

      例如：board =
            [
              ['A','B','C','E'],
              ['S','F','C','S'],
              ['A','D','E','E']
            ]

            给定 word = "ABCCED", 返回 true.
            给定 word = "SEE", 返回 true.
            给定 word = "ABCB", 返回 false.



      分析：


      思路：DFS搜索 + 回溯解决即可。  跟剑指offer上的题目 有所不同

'''


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        if not word:
            return True

        self.res = False
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        def dfs(start, x0, y0):
            if start == len(word) - 1:
                self.res = True
                return
            visited.add((x0, y0))

            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                # print x, y
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited and board[x][y] == word[
                    start + 1] and not self.res:
                    visited.add((x, y))
                    dfs(start + 1, x, y)
                    visited.remove((x, y))

        m, n = len(board), len(board[0])
        # print m * n, len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    dfs(0, i, j)
                    if self.res:
                        return True
        return False

#___________________________________    练习1   ______________________________#
'''
     针对于该题目，下面的思路非常的清晰简单，就是：
         
         首先  从矩阵中找到 要搜索的起点，也就是字母为word[0] 的位置，以该位置开始 进行DFS搜索。
         
         进行DFS搜索过程：
           （1）DFS 三个终止条件判别 。一个成功，两个失败条件
           （2）标记已经走过的位置【标记已经走过的位置，加个' '即可】，然后进行四周的搜索，把匹配成功的去掉word[1:]，继续进行DFS递归搜索。
           （3）在递归完成后， 对标记进行回溯还原，持续的搜索即可。
           
         一直 从 word[0]往下找，成功匹配了字母，就继续往下搜。
         
         时间复杂度为O(Nlog(N))  空间复杂度为O(N)  

'''
class Solution1(object):
    #board 是 二维矩阵，word是要搜索的目标词
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        r, c = len(board), len(board[0])

        ans = []
        # 找到 word[0] 在矩阵中的开始（可以有多个位置），进行DFS的搜索，以该位置为起点，进行 单词的组合搜索...
        for i in range(r):
            for j in range(c):
                # 找到 从 word[0]开始的位置
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word):
                        return True

        return False

    def dfs(self, tmp, i, j, word):
        # dfs搜索成功，搜到了目标词
        if not word:
            return True

        # dfs 搜索失败，停止的两个条件
        if not (i >= 0 and i < len(tmp)) or not (j >= 0 and j < len(tmp[0])):
            return False
        if not tmp[i][j] == word[0]:
            return False

        # 这个置空是为了放置 重新走回来，已经走过的 就不能回来了。  后面加了个' '，所以就算 字母对了，也不会往那走
        tmp[i][j] += ' '
        # 往四个位置 进行伸展，进行合理的DFS存在单词上的搜索
        res = self.dfs(tmp, i + 1, j, word[1:]) or \
              self.dfs(tmp, i - 1, j, word[1:]) or \
              self.dfs(tmp, i, j + 1, word[1:]) or \
              self.dfs(tmp, i, j - 1, word[1:])

        # 回溯操作，把后面加的' '去掉，返回过来，便于其他 合理探索的 位置寻找利用。
        tmp[i][j] = tmp[i][j][:-1]

        # 有一个路径搜索成功，都算可以，用的 或计算。
        return res