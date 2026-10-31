class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #maps char count of each str -> list of anagrams; defaults to list when nothing

        #first get char count of each str
        for word in strs:
            count = [0]*26 #a->z
            for c in word:
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(word)  #only python

        return list(res.values())

        #O(m*n) where m is number of words, n is avg length of each word
        #space complexity is O(m*n) at worst case
        

    

    