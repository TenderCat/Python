"""
如果a+b+c = 1000,且a^2+b^2=c^2(a,b,c为自然数，如何求出所有的a、b、c可能的组合？

"""

import time
start_time = time.time()
# 枚举法
#for a in range(0,1001):
#    for b in range(0,1001):
#        for c in range(0,1001):
#            if a + b + c == 1000 and a**2 + b**2 == c**2:
#                print("a, b, c:%d, %d, %d" % (a, b, c))
"""
T = 1000 * 1000 * 1000 * 2
T = 2000 * 2000 * 2000 * 2
T = N * N * N * 2
T(n) = N^3 * 2
在计算时间复杂度时：虽然分的越细致越精确，但是更多的是关心趋势（时间的数量级）
因此有ｇ(n) = N^3 表示其趋势，即为大O表示法
简单的说，就是忽略掉所有的参数（ｋ,b)等，剩余的即为大O
"""
for a in range(0,1001):
    for b in range(0,1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a, b, c:%d, %d, %d" % (a, b, c))
end_time = time.time()
print("time:%d" % (end_time-start_time))
