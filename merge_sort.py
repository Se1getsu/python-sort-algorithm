# マージソート
# 平均計算量 O(nlogn) 最悪計算量 O(nlogn)


def merge_sort(seq):
    if len(seq) <= 1: return seq
    midx = len(seq)//2
    return merge(merge_sort(seq[:midx]), merge_sort(seq[midx:]))

def merge(seq1, seq2):
    res = []
    while seq1 and seq2:
        res.append( seq1.pop(0) if seq1[0] < seq2[0] else seq2.pop(0) )
    return res + seq1 + seq2


import random
a = [random.randint(0,100) for _ in range(10)]
print("Input\n%s\n" % a)

a = merge_sort(a)

print("Result\n%s" % a)