class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #mm it's cnfussing for me 
        # we got an issue with the ordering here 
        # we can use the Fn. sorted() to get rid of this parametar here 
        # return sorted(s) == sorted(t) -> that would be the easy one to do 
        # The Dictionary Soultion 
        count_s = {}
        count_t = {} 
        for char in s: 
            if char not in count_s:
                count_s[char] = 1 
            else: 
                count_s[char] += 1 
        for char in t: 
            if char not in count_t:
                count_t[char] = 1 
            else: 
                count_t[char] += 1

        return count_s == count_t 