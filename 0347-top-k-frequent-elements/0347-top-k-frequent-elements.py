import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        mydict = defaultdict(lambda: 0)
        #key is number, value is count
        for n in nums:
            mydict[n] += 1
    
        print(mydict)
        
        for key,value in mydict.items():
            item = [value,key]
            print(item)
            heapq.heappush(heap,item)
        
        # heapq.heapify(heap)
        heap.sort()
        print(heap)
        
        # sorted
        # j=-1
        res = []
        for i in range(len(heap)-1,len(heap)-k-1,-1):
            res.append(heap[i][1])
            
        
        return res


        

        

        