def solve(x, y, s, t):
    time = 0
    for i in s:

        if i == "N":
            y += 1
            
        elif i == "S":
            y -= 1
            
        elif i == "E":
            x += 1
            
        else:
            x -= 1
        time += 1           
        if time-1 == abs(x)+abs(y) or time == abs(x)+abs(y):
            print("Case #{}: {}".format(t, time))
            return 

        
        
        
    print("Case #{}: {}".format(t, "IMPOSSIBLE"))

tests = int(input())
for t in range(tests):
    x, y, s = input().split()
    x = int(x)
    f = 0
    y = int(y)
    solve(x, y, s, t+1)


