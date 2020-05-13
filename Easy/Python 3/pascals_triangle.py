"""

https://leetcode.com/problems/pascals-triangle/

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""

from typing import List


class Solution:

    # Changed to static method
    @staticmethod
    def generate(numRows: int) -> List[List[int]]:

        ans = []

        for i in range(1, numRows+1):
            if i < 3:
                ans.append([1 for _ in range(i)])
            else:
                next_row = []
                prev_row = ans[-1]
                for k in range(len(prev_row) - 1):
                    next_num = prev_row[k] + prev_row[k+1]
                    next_row.append(next_num)
                next_row = [1] + next_row + [1]
                ans.append(next_row)

        return ans


if __name__ == '__main__':

    num_rows = 5

    for row in Solution.generate(num_rows):
        print(row)
