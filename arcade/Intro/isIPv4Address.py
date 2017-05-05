def isIPv4Address(inputString):
    try:
        nums = inputString.split(".")
        if len(nums) != 4:
            return False
        for n in nums:
            if int(n) < 0 or int(n) > 255:
                return False
    except:
        return False

    return True