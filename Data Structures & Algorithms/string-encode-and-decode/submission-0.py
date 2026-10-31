class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s))) #special delimeter
            res.append("#")
            res.append(s)

        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j=i #find position of #
            while s[j] != "#":
                j+=1
            length=int(s[i:j]) #get length of the string
            #now move index past j
            i = j+1
            j=i+length
            res.append(s[i:j])
            i=j
        return res