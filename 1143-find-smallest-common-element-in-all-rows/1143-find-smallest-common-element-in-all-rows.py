class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        '''
            Given an m x n matrix mat where every row is sorted in strictly increasing order,
            return the smallest common element in all rows
        '''

        '''
            Iterate through the first row, use binary search in each other row to try to find that element
        '''

        for num in mat[0]:
            all_contain = True
            for row in mat[1:]:
                # use binary search to check if row contains num
                index = bisect.bisect_left(row, num)
                if index >= len(row) or row[index] != num:
                    all_contain = False
                    break

            if all_contain:
                return num

        return -1