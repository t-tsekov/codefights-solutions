def singleNumber(nums):
    x = 0
    for i in nums:
        x = x ^ i
    return x
