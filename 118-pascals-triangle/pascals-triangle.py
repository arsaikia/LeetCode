class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for rowIdx in range(numRows):
            # For each row, 1st and last elements are 1
            # default all elements to 1
            row = [1 for __ in range(rowIdx + 1)]

            # from row idx 2 onward, build elements by summing top row elements
            for idx in range(1, len(row) - 1):
                row[idx] = triangle[rowIdx - 1][idx - 1] + triangle[rowIdx - 1][idx]
            
            triangle.append(row)
        
        return triangle


        