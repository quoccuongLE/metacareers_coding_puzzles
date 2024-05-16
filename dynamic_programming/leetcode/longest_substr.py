

def lengthOfLongestSubstring(s: str) -> int:
    longest_substr = current_substr = ''
    r = 0
    while r < len(s):
        if s[r] not in current_substr:
            current_substr = "".join([current_substr, s[r]])
            if len(current_substr) > len(longest_substr):
                longest_substr = current_substr
        else:
            current_substr = "".join([current_substr, s[r]])
            repeat_idx = current_substr.index(s[r])
            current_substr = current_substr[repeat_idx + 1:]
        r += 1
    return len(longest_substr)


res = lengthOfLongestSubstring("pwwkew")
print(res)