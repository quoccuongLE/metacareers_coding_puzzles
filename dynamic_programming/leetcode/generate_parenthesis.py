from typing import List


def generateParenthesis(n: int) -> List[str]:
    if n == 1:
        return ["()"]

    def concatLeft(str1, str2) -> List[str]:
        return ["".join([str1, x]) for x in str2]

    def generate(left_store, right_store) -> List[str]:
        if len(left_store) == 0:
            return [right_store]
        if len(right_store) == 0:
            return [left_store]
        mix = []
        case_1 = generate(left_store[1:], right_store)
        mix.extend(concatLeft("(", case_1))
        if len(left_store) <=len(right_store):
            case_2 = generate(left_store, right_store[1:])
            mix.extend(concatLeft(")", case_2))
        return mix

    left_store = ''.join(['(' for _ in range(n-1)])
    right_store = ''.join([')' for _ in range(n-1)])
    substr = generate(left_store, right_store)
    res = ["".join(["(", x, ")"]) for x in substr]
    return res

res = generateParenthesis(3)
assert ["((()))","(()())","(())()","()(())","()()()"] == res
