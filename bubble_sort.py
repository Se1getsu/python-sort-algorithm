# バブルソート
# 平均計算量 O(n²) 最悪計算量 O(n²)


def bubble_sort(seq):
    for i in range(len(seq)):
        if i: print(seq)
        for j in range(len(seq)-i-1):
            seq[j], seq[j+1] = min(seq[j], seq[j+1]), max(seq[j], seq[j+1])


import random
a = [random.randint(0,100) for _ in range(10)]
print("Input\n%s\n" % a)

bubble_sort(a)

print("Fin")