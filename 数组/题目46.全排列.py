# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个没有重复数字的序列，返回其所有可能的全排列。

             输入: [1,2,3]
                输出:
                [
                  [1,2,3],
                  [1,3,2],
                  [2,1,3],
                  [2,3,1],
                  [3,1,2],
                  [3,2,1]
                ]

    分析：其实还是一种DFS（又称回溯法）的思想方式。不同的是，已经用过的元素不能再用，可用tmp.find或者visited标记来
    使用过的元素。
      这里就用回溯法，123,132，213，231，下一次递归的就是上一次除了本身的所有数，结束条件为nums为空


      思路：  书写DFS回溯的方式得到结果。  贼简单的DFS方式即可

'''

class Solution:
    #主函数，这里会启动DFS的 组合搜索
    def permute(self, nums):
        result=[]
        l=len(nums)
        self.DFS(nums,[],result,l)
        return result
    #
    def DFS(self,nums,path,result,l):
        #这是  拼接成功的  标识，当拼接成功时，说明是一个成功的 DFS遍历得到的结果。 path中存储中的当做真实的拼接来用即可。
        if len(nums)==0:
            result.append(path[:])
            return

        #这里是针对数组 进行拼接角度的DFS遍历
        for i in range(len(nums)):
            path.append(nums[i])
            self.DFS(nums[:i]+nums[i+1:],path,result,l)

            #DFS最核心的一点是 一定要进行还原，这样才能轻量化，path内的信息才是每次构建时所需要的。
            path.pop()
#___________________________________    练习1   ______________________________#
# 这题题意 和解法都是较为简单的方式。
#  一般这种字母拼接判断的问题，解决方法其实就是  使用树的判别即可，通常是基于DFS的方式

#全排序主函数
def fun1(nums):
    #result为 成功拼接容器，l作为长度的判别，用途不大，   nums作为可利用的收集使用
    result=[]
    l=len(nums)
    DFS(nums,[],result,l)
    return result

#较为精进的  深度遍历   合适组合结果收集
def DFS(nums,path,result,l):
    #收集成功判断
    if len(nums)==0:
        result.append(path[:])
        return

    #针对于数据   进行进一步的拼接DFS 判别  (这里nums其实是不断缩减的，已经用过的，就不会再次使用)
    for i in range(len(nums)):
        #路径轨迹的附加
        path.append(nums[i])
        DFS(nums[:i]+nums[i+1:],path,result,l)

        #在DFS递归最后，进行一定的还原
        path.pop()
