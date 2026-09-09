class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = s.lower()
        cleaned = ''.join(char for char in s.lower() if char.isalnum())
        j = len(cleaned) - 1

        for i in range(len(cleaned)):
            if cleaned[i] == cleaned[j]:
                j -= 1
            else:
                return False
        return True
            

        