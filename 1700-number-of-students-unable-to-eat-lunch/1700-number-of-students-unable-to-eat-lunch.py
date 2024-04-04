class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # sand = [0,0,0], students = [1,1,1], ans= 3 Good
        # students = [0,0], sand = [0,1]
        res = 0
        # 0,1,2,3
        loop = 0
        while (loop < len(sandwiches)):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                loop = 0
            else:
                first = students.pop(0)
                students.append(first)
                loop +=1
        
        return len(sandwiches)

        