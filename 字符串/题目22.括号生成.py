# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

          例如，给出 n = 3，生成结果为：
                   [
                      "((()))",
                      "(()())",
                      "(())()",
                      "()(())",
                      "()()()"
                    ]

      分析：使用回溯法，现在要知道一个事情，在生成的有效的字符串过程中，左括号 '(' 在前且个数大于右括号 ')' 的个数。
      说白就是，优先生成左括号 '('，不能生成的时候就回溯到前一个位置去生成右括号 ')' ，在生成的过程分别用 left、right 记录左右括号的个数，直至结束。


      思路：回溯+剪枝。
            剪枝原则：
                    放了左括号才能放右括号，left 代表还能放左括号的个数，right 代表还能放右括号的个数。

'''

class Solution:
    #思路 就是  DFS回溯  + 左右括号数量控制 + 边缘限定 即可
    def generateParenthesis(self, n):
        ans = []

        #在接下来的深度 优先回溯中，保持先加（ 后加），然后数量等价即可，这里因为有限制left < n设置，所以生成的数量绝对是等价的。
        def backtrack(s='', left=0, right=0):

            #回溯 时的判别条件， 当 括号数量达到上限时，进行结束即可。 此时的s就是合法的组合。这是DFS的截止判定条件。
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:  # 一直添加左括号
                backtrack(s + '(', left + 1, right)
            if left > right:  # 保证左括号的个数大于右括号的情况下，才能添加右括号
                backtrack(s + ')', left, right + 1)

        backtrack()
        return ans


if __name__ == '__main__':
    n = 3
    solu = Solution()
    print(solu.generateParenthesis(n))


#___________________________________    练习1   ______________________________#
#思路是比较简单的，使用回溯法的 方式  来获得n 个括号对进行组合的结果
def solution1(n):
    ans=[]

    #书写内部 回溯函数                left表示已经有的左括号的数量
    def backtrck(s='',left=0,right=0):
        #当回溯中，括号数量到上限时结束 (就是一次合格的结果生成)
        if len(s)==2*n:
            ans.append(s)
            return

        ###########  下面就是回溯控制，会对所有情况进行组合  ##########
        #首先进行添加左括号 可能性的 附加
        if left<n:
            backtrck(s+'(',left+1,right)
        #其次进行 添加右括号附加的情况
        if left>right:
            backtrck(s+')',left,right+1)

    #启动函数，进行查看
    backtrck()
    return ans