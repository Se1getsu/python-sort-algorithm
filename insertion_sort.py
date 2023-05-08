# 挿入ソート
# 平均計算量 O(n²) 最悪計算量 O(n²)


def insertion_sort(seq):
    for i in range(1, len(seq)):
        tmp = seq[i]
        for j in range(i, 0, -1):
            if seq[j-1] <= tmp: break
            seq[j] = seq[j-1]
            j -= 1
        seq[j] = tmp
        print("%4d"%tmp, seq)
    return seq


import random
a = [random.randint(0,100) for _ in range(10)]
print("Input\n%s\n" % a)

insertion_sort(a)

print("Fin")