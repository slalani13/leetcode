class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # ding, hello
        # swap front and back, move pointer until they are the same index or 
        #front pointer > rear pointer

        rear = len(s)-1
        front = 0
        while front != rear and front < rear:
            # need tmp pointer to save front value
            # print(front)
            # print(s[front])
            tmp = s[front]
            # change front value
            s[front] = s[rear]
            s[rear] = tmp
            front += 1
            rear -= 1