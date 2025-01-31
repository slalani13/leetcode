class Solution:
    def reverseWords(self, s: str) -> str:
        # word_list = ["the", "sky", "is", "blue"]
        # reverse, then join
        s.strip() # remove leading and trailing white space
        word_list = []
        i = 0
        while i < len(s):
            word = ""
            while i<len(s) and s[i] != " ":
                word += s[i]
                i+=1
            word_list.append(word)
            while i<len(s) and s[i] == " ":
                i += 1
        word_list.reverse() 
        res = " ".join(word_list)
        output = res.strip()
        return output
            
            
            
        