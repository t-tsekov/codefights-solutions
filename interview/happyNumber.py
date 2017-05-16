def happyNumber(n):
    nums = set()
    happy = True
    while n != 1:
        n = sum([int(x)*int(x) for x in str(n)])
        if n in nums:
            happy = False
            break
        else:
            nums.add(n)
    return happy

