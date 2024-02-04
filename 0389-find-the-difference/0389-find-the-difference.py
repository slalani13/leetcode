class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # s='abcd' t='dceba'
        # s = 'cccc' t='ccccd'
        # Create a map of the letter and its count for both s and t
        #Iterate through the map and check to find if key and value matches
        # if not return that key

        string1 = {}
        string2 = {}
        for c in s:
            # Either c is in map or not in map
            if c in string1:
                string1[c] += 1
            else:
                string1[c] = 1
        
        print(string1)

        for c in t:
            # Either c is in map or not in map
            if c in string2:
                string2[c] += 1
            else:
                string2[c] = 1
        
        print(string2)

        for key in string2:
            print(key)
            if key in string1 and string1[key] == string2[key]:
                continue
            elif key in string1 and string1[key] != string2[key]:
                return key
            else:
                return key
        