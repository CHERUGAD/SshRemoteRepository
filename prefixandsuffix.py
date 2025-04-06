class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1]*n
    
        prefix = 1
        for i in range(n) :
            answer [i] = prefix
            prefix  *= nums[i]
            print(answer)
        
        
        suffix = 1
        for i in range(n-1,-1,-1) :
            answer [i] *= suffix 
            suffix *= nums[i]
            print(answer)
        
        return answer 

sol =  Solution()
print(sol.productExceptSelf([1,2,3,4])) # [24,12,8,6]