from typing import Sequence, Union


def remove_one_element(A: Sequence[int], B: Sequence[int], in_A_idx: int) -> Union[Sequence[int], int]:
    if A == B:
        return A, 0
    
    del A[in_A_idx]
    return A, 1


def getLongestCommonSubsequence(A: Sequence[int], B: Sequence[int]) -> Sequence[int]:
    if A == B:
        return A
    
    return


if __name__ == "__main__":

    A = [1, 4, 5, 6, 9, 10, 11]
    B = [6, 4, 5, 9, 11]
    assert getLongestCommonSubsequence(A=A, B=B) == [4, 5, 9, 11]
