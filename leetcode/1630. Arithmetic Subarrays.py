class Solution:

    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) ->list[bool]:
        ans = []
        if len(nums) > 1:
            for i in range(len(l)):
                subarray = nums[l[i]: r[i]+1]
                result = self._checkArithmeticSubarray(subarray)
                ans.append(result)
            return ans
        return False

    def _checkArithmeticSubarray(self, subarray):
        subarray.sort()
        diff = subarray[1] - subarray[0]
        for i in range(1, len(subarray)-1):
            if subarray[i+1] - subarray[i] != diff:
                return False
        return True

 
s = Solution()
print(s.checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]))