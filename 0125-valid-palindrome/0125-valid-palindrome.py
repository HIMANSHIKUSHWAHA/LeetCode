class Solution:
    def isPalindrome(self, s: str) -> bool:
        nospace=''.join(char for char in s.lower() if char.isalnum())
        rev=nospace[::-1]
        return rev==nospace
