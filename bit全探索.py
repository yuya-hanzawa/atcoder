# O(n*2^n)
n=int(input())

for i in range(2**n): #nは隙間の数
    # 何かしらの処理
    l=[]
    # i を利用して、j番目のスイッチがオンかどうかチェックする。  
    for j in range(n):
        if ((i >> j) & 1):
            l.append(0)
        else:
            l.append(1)  

# bitの練習
# https://atcoder.jp/contests/abc014/tasks/abc014_2

# bit全探索の練習
# https://atcoder.jp/contests/abc128/tasks/abc128_c
