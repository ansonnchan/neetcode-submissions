class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we could sort the array
        #frequency counter -> key is number, value is the values
        #return 
        res = []
        freq_map = defaultdict(int)
        for num in nums:
                freq_map[num]+=1
       
        freq_list = []
        for num in freq_map:
            freq_list.append((freq_map[num],num))
        freq_list.sort(reverse=True)
        for i in range(k):
            res.append(freq_list[i][1])
        
        return res
