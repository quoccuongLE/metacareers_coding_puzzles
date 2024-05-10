

def LIS_recursive(A):
    print(A)
    if len(A) == 1:
        return 1
    if len(A) == 2:
        return 2 if A[0] < A[1] else 1
    else:
        candidates = []
        for k in range(1, len(A)):
            LIS_k = LIS_recursive(A[:k])
            if A[k-1] < A[-1]:
                candidates.append(LIS_k + 1)
            else:
                candidates.append(LIS_k)
        
        return max(candidates)


def LIS_with_memory(A):
    L = [1] * len(A)
    for i in range(1, len(L)):
        # print(f"A[i] = {A[i]}")
        subproblems = [L[k] for k in range(i) if A[k] < A[i]]
        L[i] = 1 + max(subproblems, default=0)
    return max(L, default=0)


if __name__ == "__main__":
    A = [5, 2, 8, 6, 3, 6, 9, 5]
    assert LIS_with_memory(A) == 4

    A = [0, 1, 2, 3, 4, 1, 5]
    assert LIS_with_memory(A) == 6

    A = [0, 2, 1, 5]
    print(LIS_recursive(A))
    assert LIS_recursive(A) == 3

    A = [5, 2, 8, 6, 3, 6, 9, 5]
    res = LIS_recursive(A)
    print(res)
    assert res == 4

