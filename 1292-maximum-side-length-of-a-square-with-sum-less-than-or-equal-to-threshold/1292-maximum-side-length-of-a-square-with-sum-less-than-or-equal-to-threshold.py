class Solution(object):
    def maxSideLength(self, mat, threshold):
        m, n = len(mat) , len(mat[0])

        prefix = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j+1] = (mat [i][j]+ prefix[i][j+1]+ prefix[i + 1][j] - prefix[i][j])
        def exists_square(k):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    total = (prefix[i + k][j+k ] - prefix[i][j+k]-prefix[i+k][j]+prefix[i][j])
                    if total <= threshold:
                        return True

            return False
        left, right = 0, min(m,n)
        ans = 0 
        while left <= right: 
            mid = (left + right) // 2 
            if exists_square(mid):
                ans = mid
                left = mid +1 
            else: 
                right = mid - 1 
        return ans 
        

        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        