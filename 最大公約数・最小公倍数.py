from functools import reduce
from math import gcd

# 2つの整数の最大公約数 O(logn)
print(gcd)

# 3つ以上の整数の最大公約数 list
def gcd_list(num_list: list) -> int:
    return reduce(gcd, num_list)

# 2つの整数の最小公倍数 O(logn)
def lcm(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)

#　3つ以上の整数の最小公倍数
def lcm_list(num_list: list):
    return reduce(lcm, num_list, 1)
