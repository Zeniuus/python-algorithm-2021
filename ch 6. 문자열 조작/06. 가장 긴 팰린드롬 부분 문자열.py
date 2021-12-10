from util import print_result


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        result = s[0]

        for left_center in range(len(s)):
            curr_longest = find_longest_odd_length_palindrome(s, left_center)
            if len(curr_longest) > len(result):
                result = curr_longest

        for left_center in range(len(s) - 1):
            curr_longest = find_longest_even_length_palindrome(s, left_center)
            if len(curr_longest) > len(result):
                result = curr_longest

        return result


def find_longest_odd_length_palindrome(s: str, center: int) -> str:
    prev = ''
    max_i = min(center, len(s) - center - 1)
    for i in range(max_i + 1):
        target = s[center - i:center + i + 1]
        if not is_palindrome(target):
            return prev
        else:
            prev = target

    return s[center - max_i:center + max_i + 1]


def find_longest_even_length_palindrome(s: str, left_center: int) -> str:
    prev = ''
    max_i = min(left_center, len(s) - left_center - 2)
    for i in range(max_i + 1):
        target = s[left_center - i:left_center + i + 2]
        if not is_palindrome(target):
            print(target, prev)
            return prev
        else:
            prev = target

    return s[left_center - max_i:left_center + max_i + 2]


def is_palindrome(s: str):
    return s == s[::-1]


print_result(Solution(),
             inputs=["babad"],
             expected="bab")
