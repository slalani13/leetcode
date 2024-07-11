class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        l1 = len(firstWord)
        l2 = len(secondWord)
        l3 = len(targetWord)
        firstWordInt = 0
        secondWordInt = 0
        targetWordInt = 0
        for i in range(l1):
            number = ord(firstWord[i]) - ord('a')
            number = number * 10**(l1-i+1)
            firstWordInt += number
        for i in range(l2):
            number = ord(secondWord[i]) - ord('a')
            number = number * 10**(l2-i+1)
            secondWordInt += number
        for i in range(l3):
            number = ord(targetWord[i]) - ord('a')
            number = number * 10**(l3-i+1)
            targetWordInt += number
        if targetWordInt == firstWordInt + secondWordInt:
            return True
        return False
        