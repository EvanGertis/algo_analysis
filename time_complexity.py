# 1 second = 1000 ms
# 1 minute = 60000 ms 
# 1 hr     = 36*10^5 ms
# 1 day    = 864*10^5 ms
# 1 month  = 26784*10^5 ms
# 1 year   = 315360*10^5 ms
# 1 century = 315360*10^7 ms

############
############
#CONVERSION#

# f^-1(t) = n

import math

t1 = 1000                       # second in ms
t2 = 60000                      # minute in ms
t3 = 36*math.pow(10,5)          # hour in ms
t4 = 864*math.pow(10,5)         # day in ms
t5 = 26784*math.pow(10,5)       # month in ms
t6 = 315360*math.pow(10,5)      # year in ms
t7 = 315360*math.pow(10,7)      # century in ms 

times = [t1, t2, t3, t4, t5, t6, t7]

# log(n) -> 10^(t)
print("log(n)", end = " ")
for t in times:
    try:
        print(math.pow(2,t), end = " ")
    except Exception:
        print("exception", end = " ")

print()

# n^(1/2) -> t^2
print("n^(1/2)", end = " ")
for t in times:
    try:
        print(math.pow(t,2), end = " ")
    except Exception:
        print("exception", end = " ")

print()

# n -> t
print("n", end = " ")
for t in times:
    try:
        print(t, end = " ")
    except Exception:
        print("exception", end = " ")
print()

# TODO fixed point iteration on approximate inverse
# nlog(n) -> 
print("nlog(n)", end = " ")
for t in times:
    try:
        print("TO BE IMPLEMENTED", end = " ")
    except Exception:
        print("exception", end = " ")
print()

# n^2 -> t^(1/2)
print("n^2", end = " ")
for t in times:
    try:
        print(math.pow(t, 0.5), end = " ")
    except Exception:
        print("exception", end = " ")
print()

# n^3 -> t^(1/3)
print("n^3", end = " ")
for t in times:
    try:
        print(math.pow(t, 1/3), end = " ")
    except Exception:
        print("exception", end = " ")
print()

# 2^n -> log(t,2)
print("2^n", end = " ")
for t in times:
    try:
        print(math.log(t, 2), end = " ")
    except Exception:
        print("exception", end = " ")
print()

# n! -> 
print("n!", end = " ")
for t in times:
    try:
        print("TO BE IMPLEMENTED", end = " ")
    except Exception:
        print("exception", end = " ")
print()
