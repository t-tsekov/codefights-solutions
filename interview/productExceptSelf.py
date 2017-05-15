def productExceptSelf(nums, m):
  prefixProduct = [1]*len(nums)
  suffixProduct = 1    # now this is just a number

  for i in range(1,len(nums)):
    prefixProduct[i] = (prefixProduct[i-1] * nums[i-1]) % m

  total = 0
  for i in range(len(nums)):
    total += (prefixProduct[-1 - i]*suffixProduct) % m
    suffixProduct = (suffixProduct * nums[-1-i]) % m

  return total % m