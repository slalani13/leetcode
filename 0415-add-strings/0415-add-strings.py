import sys
sys.set_int_max_str_digits(0)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #1. inputs are two strings
        #2. create a dictionary which maps letters to numbers
        #3. iterate through string, use length to determine power of 10
        

        map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7":7, "8":8, "9":9, }

        num1_length = len(num1)
        num2_length = len(num2)
        i = 1
        # first number
        fnum = 0
        # second number
        snum = 0
        
        for l in num1:
            number = map[l] * 10 ** (num1_length - i)
            # print("This is the number: ", number)
            i+=1
            fnum += number
            # print("fnum ",fnum)

        
        i = 1
        for l in num2:
            number = map[l] * 10 ** (num2_length - i)
            i+=1
            snum += number
            # print("snum ", snum)
        
        sum = fnum + snum
                     

        return str(sum)
        
        



