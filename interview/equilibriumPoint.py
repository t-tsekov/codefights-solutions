def equilibriumPoint(arr):
    s = sum(arr)
    cur_sum = 0
    for i in range(len(arr)):
        if s - cur_sum - arr[i] == cur_sum:
            return i+1
        cur_sum += arr[i]
    return -1

