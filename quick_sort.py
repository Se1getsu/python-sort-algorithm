# クイックソート
# 平均計算量 O(nlogn) 最悪計算量 O(n²)


# 基準値の計算
def getPivot(seq, first, end):
    x, y, z = seq[first], seq[end], seq[(first+end)//2]
    return max(min(x,y), min(max(x,y),z)) # x,y,zの中央値


# 基準値を決め、値の入れ替えを行いながら その基準値より 小さいグループ と 大きいグループ で分け、
# その境目のインデックスを戻り値とする。
def partition(seq, first, end):
    p = getPivot(seq, first, end)
    print(p)

    while 1:
	
        while seq[first] < p: first += 1
        while seq[end]   > p: end -= 1
		
        if first > end:
            return first
        else:
            seq[first], seq[end] = seq[end], seq[first]
            first += 1
            end -= 1


def quick_sort(seq):
    __quick_sort(seq, 0, len(seq)-1)

def __quick_sort(seq, first, end):
    if first >= end: return
    p = partition(seq, first, end)
    print(seq[first:p], seq[p:end+1])
    __quick_sort(seq, first, p-1)
    __quick_sort(seq, p, end)


import random
a = [random.randint(0,100) for _ in range(10)]
print("Input\n%s\n" % a)

quick_sort(a)

print("\nResult\n%s" % a)