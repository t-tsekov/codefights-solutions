def composeRanges(nums):
    res = []
    start = 0
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [str(nums[0])]

    for i in range(len(nums) - 1):

        if nums[i + 1] - nums[i] != 1:
            res.append(make_range(nums[start], nums[i]))
            start = i + 1

    if nums[len(nums) - 2] + 1 != nums[len(nums) - 1]:
        start = len(nums) - 1;

    res.append(make_range(nums[start], nums[len(nums) - 1]))

    return res


def make_range(a, b):
    if a == b:
        return str(a)
    return str(a) + "->" + str(b)