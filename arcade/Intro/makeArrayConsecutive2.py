arr = sorted(statues)
res = 0
for i in range(1, len(arr)):
    res += arr[i] - arr[i - 1] - 1

return res