class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        def bst(q):
            i, j = 0, len(items) - 1
            max_beauty = 0

            while i <= j:
                mid = (i + j) // 2
                if items[mid][0] > q:
                    j = mid - 1
                else:
                    max_beauty = max(max_beauty, items[mid][1])
                    i = mid + 1

            return max_beauty

        items.sort(key = lambda x : x[0])

        max_beauty = items[0][1]
        for i in range(len(items)):
            max_beauty = max(max_beauty, items[i][1])
            items[i][1] = max_beauty
        
        res = []
        for q in queries:
            res.append(bst(q))

        return res

