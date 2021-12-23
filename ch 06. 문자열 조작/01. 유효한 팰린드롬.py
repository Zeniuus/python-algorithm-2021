import re


def is_palindrome(s: str) -> bool:
    target_chars = [c.lower() for c in re.sub('[^a-zA-Z0-9]', '', s) if c.isalnum()]
    target_chars_len = len(target_chars)
    for i in range(target_chars_len // 2):
        if target_chars[i] != target_chars[target_chars_len - 1 - i]:
            return False
    return True


print(is_palindrome('A man, a plan, a canal: Panama'))
print(is_palindrome('race a car'))
