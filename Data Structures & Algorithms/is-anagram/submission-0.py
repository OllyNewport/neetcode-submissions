class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False

        for x in range(len(s)):
            if s[x] in s_dict:
                s_dict[s[x]] += 1
            else:
                s_dict[s[x]] = 1

        for x in range(len(t)):
            if t[x] in t_dict:
                t_dict[t[x]] += 1
            else:
                t_dict[t[x]] = 1

        if s_dict == t_dict:
            return True
        else:
            return False