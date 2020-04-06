def solve(ip_arr):
    arr = []
    for i in range(len(ip_arr)):
        arr.append((ip_arr[i][0], ip_arr[i][1], i))
    arr.sort()
    c_end = 0
    j_end = 0
    res_arr = []
    for start, end, idx in arr:
        if start < c_end and start < j_end:
            return "IMPOSSIBLE"
        if start >= c_end:
            res_arr.append(('C', idx))
            c_end = end
        else:
            res_arr.append(('J', idx))
            j_end = end
    res = ''
    for c, idx in sorted(res_arr, key=lambda x: x[1]):
        res += c
    return res


tests = int(input())  
for test in range(1, tests + 1):
    n = int(input())
    ar = []
    for _ in range(n):
        interval = [int(s) for s in input().split(" ")]
        ar.append(interval)
    result = solve(ar)
    print("Case #{}: {}".format(test, result))

