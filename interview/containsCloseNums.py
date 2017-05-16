def containsCloseNums(nums, k):
    x = {}
    for i in range(len(nums)):
        if nums[i] not in x.keys():
            x[nums[i]] = []
        x[nums[i]].append(i)

    for a in x.values():
        n = len(a)
        if n > 1:
            for i in range(n):
                for j in range(i, n):
                    if i != j and abs(a[i] - a[j]) <= k:
                        return True

    return False