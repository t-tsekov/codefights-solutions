def productExceptSelf(nums, m):
  prefixProduct = [1]*len(nums)
  suffixProduct = 1    # now this is just a number

  # setup the cumulative product from left and right
  for i in range(1,len(nums)):
    # Need parenthesis, as % has higher precedence than *
    prefixProduct[i] = (prefixProduct[i-1] * nums[i-1]) % m

  total = 0
  for i in range(len(nums)):
    # start at the end, with prefixProduct -1
    # and scan right
    total += (prefixProduct[-1 - i]*suffixProduct) % m
    suffixProduct = (suffixProduct * nums[-1-i]) % m
    # now multiply suffixProduct by the number that
    # was excluded

  return total % m