"""
To find the maxSubArray break the problem down into smaller problems. We are looking for the largest sum
contingous array in a given array. Brute force method would be to check the addition of the first item, then
first and second, and then continously, this would be O(n^3). The optimal solution is to start at index 1, check
if the current number is higher than the sum of the current and last number, if the current number is higher, we keep 
the number and restart the longest array calc, if sum is higher, we sum up the values and continue to the next. We update 
the array in place since at every iteration, it doesnt matter about the original array was, only the decision of the previous 
iteration. Once the array has been updated, we get the max of the array
"""
def maxSubArray(self, nums: List[int]) -> int:
    for item in range(1,len(nums)):
        if nums[item] > (nums[item] + nums[item-1]):
            nums[item] = nums[item]
        else:
            nums[item] += nums[item-1]
    return max(nums)

if __name__ == "__main__":
    maxSubArray([-2,1,-3,4,-1,2,1,-5,4])