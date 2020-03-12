# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
              你可以对一个单词进行如下三种操作：
               （1） 插入一个字符
               （2） 删除一个字符
               （3） 替换一个字符

        示例 1:
            输入: word1 = "horse", word2 = "ros"
            输出: 3
            解释:
            horse -> rorse (将 'h' 替换为 'r')
            rorse -> rose (删除 'r')
            rose -> ros (删除 'e')

        示例 2:
            输入: word1 = "intention", word2 = "execution"
            输出: 5
            解释:
            intention -> inention (删除 't')
            inention -> enention (将 'i' 替换为 'e')
            enention -> exention (将 'n' 替换为 'x')
            exention -> exection (将 'n' 替换为 'c')
            exection -> execution (插入 'u')


      分析：

      思路：  经典DP问题，用动态规划求解即可，维护一个编辑表，用dp[i][j]表示word1[:i + 1], word2[:j + 1]这个子问题的最短编辑距离解
                 二维矩阵dp，注意当word1[i-1]==word2[j-1]时，dp[i][j]=dp[i-1][j-1]， 一种较为特殊的直接赋值方式，相等了那就不用编辑呗

                【1】使用dp[i][j]用来表示字符串1的0~i-1、字符串2的0~j-1的最小编辑距离；
                【2】我们可以知道边界情况：dp[i][0] = i、dp[0][j]=j；
                【3】同时对于两个字符串的子串，都能分为最后一个字符相等或者不等的情况：
                【4】如果words[i-1] == words[j-1]：dp[i][j] = dp[i-1][j-1]；也就是说当前的编辑距离和位置i和j的字符无关；
                【5】如果words[i-1] != words[j-1]：则存在三种可能的操作：
                    * 向word1插入：dp[i][j] = dp[i][j-1] + 1;
                    * 从word1删除：dp[i][j] = dp[i-1][j] + 1;
                    * 替换word1元素：dp[i][j] = dp[i-1][j-1] + 1;

              对于边界情况，i=0代表word1为空，故由word1插入j个字符可转化为word2，即dp[0][j] = j。同理，dp[i][0] = i
              根据递推关系，这里不需要维护这个二维数组，只需要维护一行或者一列即可。

            我们实际上是可以抽象成一个  矩阵形式，进行思考。

            这里直接的思路是维护一个 编辑表，维度是m*n维度的。

'''
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 用dp[i][j]表示word1[:i + 1], word2[:j + 1]这个问题的解
        m, n = len(word1), len(word2)

        #核心的二维状态数组，   大小为(m+1)*(n+1)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        #对 编辑矩阵  上的状态进行初始化， 可以直接设定的边缘部分，可以确定的。 注意这里从0开始，是因为考虑了字符为空的情况，从空转向其他肯定是完全附加或删除的。
        for i in range(m + 1):
            dp[i][0] = i

        for i in range(n + 1):
            dp[0][i] = i

        # 获取矩阵上的 非边界元素 等信息。   这里i是对word1单词上产生的定位，  j是对word2单词上产生的定位。 对应可以两种操作吧，一种是对角直接赋值，一种是三种操作的考虑。
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果两个word上对应位置相同，那么就不需要编辑，将之前少一个字符对应的边际距离直接拿出来即可。
                #注意这里  从数值下标到 矩阵上会有一种错位，这里数组上的i-1定位实际应该对应于矩阵上的i定位，应为数组是从0位置开始的，而矩阵中0位置表示没有
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                #比较重要的， 我们在这里是需要进行一次编辑的，所以把 进行三种编辑操作，所可以操作最小的编辑情况拿过来计算即可
                #对应（5）中的三个操作   后面的分别对应于 在word1上插入一个、 替换一个、在word2上删除一个。这里不考虑删除方式，因为删除可以看做
                #另一个数组上的插入方式。
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])  # 分别对应插入，替换

        #最后返回的【m】【n】就是完成目标编辑所需要的  最后的最优的编辑次数。
        return dp[m][n]

#___________________________________    练习1   ______________________________#
# 非常典型的一种 动态规划的问题， 我们这里是 设定好 状态的指定  和状态的迁移改变即可
def fun1(word1,word2):
    m,n=len(word1),len(word2)
    #创建出状态形式   (这里是从编辑矩阵角度创建，表示各种形式的改变，我们是需要计算获取这些状态的)
    dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
    #初始的设定
    for i in range(m+1):
        dp[i][0]=i
    for i in range(n+1):
        dp[0][i]=i

    #最重要的第三部分，针对于状态矩阵 进行状态的迁移和改变
    for i in range(1,m+1):
        for j in range(1,n+1):
            #第一种情况
            if word1[i-1]==word2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])  #重要的每个位置上的弥补迁移。 分为三种情况考虑，分别是 插入一个、删除一个、替换一个（针对于目标，我们只需要最小的编辑情况方式即可）
    return dp[m][n]#最右下角是终极的  目标位置

