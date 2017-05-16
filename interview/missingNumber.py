def missingNumber(arr):
   s = [i for i in range(len(arr)+1)]
   for x in arr:
      s.remove(x)
   return s[0]