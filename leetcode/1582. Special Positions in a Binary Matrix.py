class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ans = 0
        for i in range(len(mat)):
            if sum([1 for k in mat[i] if k == 1]) == 1:
                col_num = mat[i].index(1)
                if sum([1 for i in range(len(mat)) if mat[i][col_num] == 1]) == 1:
                    ans += 1
        return ans
