class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1)
        perm = {}
        for x in s1:
            if x in perm:
                perm[x] += 1
            else:
                perm[x] = 1
        
        for l in range(len(s2)):
            current = s2[l:r]
            check = {}
            for x in current:
                if x in check:
                    check[x] += 1
                else:
                    check[x] = 1

            if check == perm:
                return True

            r += 1

        return False            