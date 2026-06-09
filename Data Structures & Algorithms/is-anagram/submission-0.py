class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            count_s = {}
            count_t = {}
            for ch in s:
                if ch not in count_s:
                    count_s[ch]=1
                else:
                    count_s[ch]+=1
            for ch in t:
                if ch not in count_t:
                    count_t[ch]=1
                else:
                    count_t[ch]+=1
            if count_s==count_t:
                return True
            else:
                return False