class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        #acb + cba = 021 + 210  = 231 = cdb

        # change the length of the smaller word so they are equal
        while len(firstWord) != len(secondWord):
            if len(firstWord) < len(secondWord):
                firstWord = 'a' + firstWord
            else:
                secondWord = 'a' + secondWord
        # add them together
        sum_array = []
        for i in range(len(firstWord)):
            # 2-1 = 1
            num1 = ord(firstWord[i])-ord('a') # 0,2,1
            # print("num1: " + str(num1))
            num2 = ord(secondWord[i])-ord('a') # 2,1,0
            # print("num2: "+ str(num2))
            sum = num1 + num2
            sum_array.append(sum)
        # [2,3,1]
        print(sum_array)
        # sum_array[3,2,1] = 300 + 20 + 1
        final_sum = 0
        exp = len(sum_array) - 1
        for num in sum_array:
            # print(exp)
            real_num = num * 10**exp
            final_sum += real_num
            # print(final_sum)
            exp-=1
            
        
        print(final_sum)
        # convert our target word into an interger and compare
        exp = len(targetWord)-1
        target_arr = []
        for l in targetWord:
            print(l)
            number = ord(l) - ord('a')
            target_arr.append(number)
        
        target_sum = 0
        for num in target_arr:
            real_num = num * 10**exp
            target_sum += real_num
            exp-=1
        
        if target_sum == final_sum:
            return True
        else:
            return False

        # check if the integer values are the same for the sum and target
