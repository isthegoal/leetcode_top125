# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

          例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
            满足要求的三元组集合为：
            [
              [-1, 0, 1],
              [-1, -1, 2]
            ]

      分析：


      思路：
          1.将数组排序
          2.定义三个指针，i，j，k。遍历i，那么这个问题就可以转化为在i之后的数组中寻找nums[j]+nums[k]+nums[i]=0

'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 非常简单的思路，固定a,用双指针在排序数组里找两数之和为-a
        nums.sort()#先进行了一波排序吧
        l = len(nums)
        res = []
        for i, a in enumerate(nums):
            if i == 0 or nums[i] > nums[i - 1]:
                #感觉这下面的是核心吧， 使用双指针的方式，针对值a,  进行另两个数的查找

                # 开始双指针 left和right指针，这里使用前后向的双指针进行前后向 查找，这里注意一个是在已知数的后一个，一个是在最后面往前。
                left, right = i + 1, len(nums) - 1
                while (left < right):

                    #这好像就是  快排中partation中的思路，只不过改成了三数和为0的限定。
                    s = a + nums[left] + nums[right]
                    if s == 0:
                        tmp = [a, nums[left], nums[right]]
                        res.append(tmp)
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
                    # 针对和大小进行  左右方向上的移动，毕竟是有序的，可以这样干。
                    elif s < 0:
                        left += 1
                    elif s > 0:
                        right -= 1
        return res

#___________________________________    练习1   ______________________________#
#寻找满足三数 和的0，的三个数组合，找到这样的数组列表。     思路很简单就是固定一个数a，然后 进行二分查找找到-a
def fun1(nums):
    nums.sort()
    res=[]
    #对于 nums中的每个数进行查找    以-a为目标做查找
    for i,a in enumerate(nums):
        if i==0 or nums[i]>nums[i-1]:
            #内部的二分查找，找到 和为-a
            left,right=i+1,len(nums)-1
            while(left<right):
                #快排的查询
                s=a+nums[left]+nums[right]
                # 找到合适的位置时，进行调整
                if s==0:
                    tmp=[a,nums[left],nums[right]]
                    res.append(tmp)

                    # 进行位置的移动查找
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while right>left and nums[right]==nums[right+1]:
                        right-=1
                #较小时，右移    根据现有情况做左右移动
                elif s<0:
                    left+=1
                #反之
                elif s>0:
                    right-=1
    #最后收集好的集合
    return res


