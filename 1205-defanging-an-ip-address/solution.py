class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        for i in address:
            ch=i
            if ch==".":
                ans+="[.]"
            else:
                ans+=ch 
        return ans       
        
