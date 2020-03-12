# coding: utf-8           使用学习生长法进行思考，  认真开始分析，  题不在多，在于精

'''
      题目：给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

              注意:
                每个数组中的元素不会超过 100
                数组的大小不会超过 200

              示例 1:
                输入: [1, 5, 11, 5]
                输出: true
                解释: 数组可以分割成 [1, 5, 5] 和 [11].

      分析：

      思路：动态规划搞定就行。
      一个背包的题目，背包容量为数组中元素和的一半＋１，这样只要看是否有元素可以正好填满背包即可．但是每个元素只能用一次
      ，所以在尝试放一个元素的时候还要避免他对尝试放其他位置时对自己的影响．所以在尝试放一个元素到背包的时候需要从容量
      最大的位置开始，如果（当前位置－当前元素大小）位置可以通过放置之前的元素达到，则当前位置也可以通过放置当前元素正
      好达到这个位置．状态转移方程为：dp[i] = dp[i] || dp[i - nums[k]];


'''


'''
   需要改造java代码
   
        class Solution {
        public:
            bool canPartition(vector<int>& nums) {
                int sum = accumulate(nums.begin(), nums.end(), 0);  
                if(sum&1) return false;  
                vector<int> dp(sum/2+1, 0);  
                dp[0] = 1;
                for(int i = 0; i < nums.size(); i++)  
                {  
                    for(int j = sum/2; j >= nums[i]; j--)  
                        dp[j] = dp[j] || dp[j-nums[i]];  
                }  
                return dp[sum/2];  
            }
        };

'''


#___________________________________    练习1   ______________________________#
'''
    本题可以看做  0-1背包问题的转化：相当于判断一个数组能否填满容量为sum（nums）//2的背包，可以转为dp问题；

    dp[i][j]表示nums[:i+1]能否填满容量为j的问题
    转移方程：dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[j]] if j>=nums[j] #这里表示当容量j可以装得下nums[j]
=dp[i-1][j]
    边界条件：遍历一次 for k in range(target+1):if nums[0]==k:dp[0][k]=True

    这里 看做背包问题，使用动态规划解法求解吧
'''
def fun1(nums):
    #  边界条件限定，必须是总和为偶数
    target=sum(nums)
    if target%2==1:
        return False

    #初始状态创建，dp[i][j]表示nums[:i+1]能否填满容量为j的问题
    target=target//2
    n=len(nums)
    dp=[[False]*(target+1) for _ in range(n)]

    # 初始状态设定(一种边界条件).  这里是对应可以填满的情况. nums[0] 可以填满对应为k背包的情况
    for k in range(target+1):
        if nums[0]==k:
            dp[0][k]=True

    # 在状态初始化后，进行正式的状态转移变换。（这个转移过程要理解）            i是可利用的数组范围，j是指定的背包容量
    for i in range(1,n):
        for j in range(1,target+1):
            if j>=nums[i]:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i]]   #dp[i-1][j-nums[i]]是关键
            else:
                dp[i][j]=dp[i-1][j]

    # 最后 后去分割的终点，表示  用所有去填满的情况，这里的填满是target,就是被除2后的
    return dp[-1][-1]
