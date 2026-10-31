class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #want overarching loop to go through words
        #we can check if anagram by using counter or sort them 

        #in this case, sorting is O(nlogn), and we do it m times
        #where m is the length of the array giving us O(m*nlogn)

        res = []
        sorted_array = []
        #sort each word
        for word in strs:
            sorted_array.append(sorted(word))
        
        # track which sorted words we've encountered
        seen = {}

        for i, word in enumerate(strs):
            key = tuple(sorted_array[i])

            if key not in seen:
                seen[key] = len(res)
                res.append([word])
            else:
                res[seen[key]].append(word)

        return res

            


    

        