def f(s):
    prev = 0
    # curHeight = 0
    res = ''
    for i in range(len(s)):
        num = int(s[i])
        diff = num - prev
        if diff == 0:
            res += s[i]
        elif diff > 0:
            res += diff * '(' + s[i]
        else:
            res += (-diff) * ')' + s[i]
        prev = num
    if prev > 0:
        res += prev * ')'
    return res

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
T = int(input())  # read a line with a single integer
for t in range(1, T + 1):
    s = raw_input()
    res = f(s)
    print("Case #{}: {}".format(t, res))


