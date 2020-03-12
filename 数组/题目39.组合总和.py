# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个无重复元素的数组candidates和一个目标数target ，找出candidates中所有可以使数字和为 target 的组合。
           candidates 中的数字可以无限制重复被选取。

           输入: candidates = [2,3,6,7], target = 7
           所求解集为:[[7],[2,2,3]]

           输入: candidates = [2,3,5], target = 8,
           所求解集为:[[2,2,2,2],[2,3,3],[3,5]]

      分析：一道很明确的DFS题。用target减candidates，若为0则push到res中，然后继续遍历。
          但是这里有个问题，是单个数可以用多次，这就有点不一样了，下次还可以用自身，所以这里DFS时内置的是candidates[i:]


      思路：

'''
# 第一种  我觉得只要写出来这一种就够了.....
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        self.DFS(candidates, [], target,result)
        return result
    def DFS(self,candidates, path, target,result):
        if sum(path)>target:
            return

        #这是DFS的边界控制条件，当 路径和等于目标时，说明这个路径是我们所需要的。直接附加到结果即可。
        if sum(path) == target:
            result.append(path[:])
            return
       # print(result)

        #相同的套路，对DFS下的所有路径进行遍历呗，进行往path路径上的附加。
        for i in range(len(candidates)):
            #如果dfs的是candidates的话，就是全排列
            #如果从index开始的数组，即下一次dfs是从他自己开始，就是去重复的数组，就是前边考虑过的数，不再考虑了
            #如果从index+1开始的话，就是没有重复数字的去重数组
            path.append(candidates[i])
            self.DFS(candidates[i:], path,target,result)
            path.pop()




#    第二种有剪枝操作的写法    这样的方式可以剔除一些无效的方式，效率会更高一些。
class Solution1:
    def combinationSum(self, candidates, target: int):
        size = len(candidates)
        if size == 0:
            return []

        # 剪枝的前提是数组元素排序
        # 深度深的边不能比深度浅的边还小
        # 要排序的理由：1、前面用过的数后面不能再用；2、下一层边上的数不能小于上一层边上的数。
        candidates.sort()
        # 在遍历的过程中记录路径，一般而言它是一个栈
        path = []
        res = []
        # 注意要传入 size ，在 range 中， size 取不到
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    def __dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        if target == 0:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 path.copy()
            res.append(path[:])

        for index in range(begin, size):
            residue = target - candidates[index]
            #“剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
            if residue < 0:
                break
            path.append(candidates[index])
            # 因为下一层不能比上一层还小，起始索引还从 index 开始
            self.__dfs(candidates, index, size, path, res, residue)
            path.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution1()
    result = solution.combinationSum(candidates, target)
    print(result)


#___________________________________    练习1   ______________________________#
#  题目意思是 非常好理解的，  就是  找到 数组组合  的和 为target。   将这样的组合放到数组中。
#这里 使用的方法就是 递归法
'''
递归函数 dfs(candidates,sublist,target,last)，其中sublist记录当前满足条件的子数组，last为当前子数组的最后一个元素。

剪枝操作1：目标值小于元素数组的最小元素，则无需继续遍历

剪枝操作2：当前元素大于目标值，则后续元素一定大于目标值（数组已排序），不会满足条件，无需继续遍历

剪枝操作3：若当前数值小于当前sublist的最后一个元素，则继续遍历，防止出现重复解决方案，如[2,2,3],[3,2,2]

     可以把整个寻找过程，利用自己的想象力  想象成 树的搜索的过程。
     并在搜索过程中，进行一些树上的剪枝操作，减少一些不必要的枝叶查询。（不断进行结点下的dfs操作）
     
     这题很考验： 对图的掌握，空间想象能力和 思考上考虑的完整性。
     
'''
#  使用到的数组， 还有目标值target
def fun1(candidates,target):
    res=[]
    if len(candidates)<=0:
        return res

    #首先进行了一次排序
    candidates.sort()

    #进行深度回溯遍历
    dfs(res,candidates,[],target,0)

    return res

def dfs(res,candidates,sublist,target,last):
    '''
    这里其实就是一种 深度的遍历搜索，   就是找到那一条路径，能够使得结点之和为target

    res：路径的存储
    candidates：候选的数据值列表
    sublist 是现在进行筛选、候选的路径
    target 是目标和
    last 是 上一个行走的值 （主要用于放置找到重复的组合）

    '''
    #截止 条件，和满足时，进行路径的收存和退出。
    if target==0:
        res.append(sublist)

    #第一次剪枝操作  . 对于剪枝操作1的条件
    if target<candidates[0]:
        return

    # 对于每个候选的做判别
    for num in candidates:
        #剪枝操作2
        if num > target:
            return
        #剪枝操作3，用于放置出现重复方案：如[2,2,3],[3,2,2]，不太了解， 如果num比较小的话，那往往是应该判别过的，因为我们每次都是
        # 完全的遍历 查找。
        if num < last:
            continue

        # 非常好的判别思路，就是在num基础上，往下去探索，找到能够组合为 target-num的路径。   sublist+[num]存储已经走的路径
        dfs(res,candidates,sublist+[num],target-num,num)

















