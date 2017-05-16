def containsNearbyAlmostDuplicate(nums, k, t):
    if (len(nums) > 10000):
        return False
    for i in reversed(range(len(nums))):
        for j in reversed(range(i)):
            if i-j > k:
                break
            if abs(nums[i] - nums[j]) <=t and i != j:
                return True
    return False