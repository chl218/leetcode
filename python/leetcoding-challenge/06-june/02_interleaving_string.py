"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
s1 and s2.

An interleaving of two strings s and t is a configuration where they are
divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1

The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or
t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:
    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.

https://leetcode.com/problems/interleaving-string/solution/
 
"""


class Solution:

    # O(m*n) space
    def isInterleave1(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        dp = [[True for _ in range(c+1)] for _ in range(r+1)]
        for i in range(1, r+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, c+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, r+1):
            for j in range(1, c+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or \
                    (dp[i][j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1][-1]

    # O(2*n) space
    def isInterleave2(self, s1, s2, s3):
        l1, l2, l3 = len(s1)+1, len(s2)+1, len(s3)+1
        if l1+l2 != l3+1:
            return False
        pre = [True for _ in range(l2)]
        for j in range(1, l2):
            pre[j] = pre[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, l1):
            cur = [pre[0] and s1[i-1] == s3[i-1]] * l2
            for j in range(1, l2):
                cur[j] = (cur[j-1] and s2[j-1] == s3[i+j-1]) or \
                    (pre[j] and s1[i-1] == s3[i+j-1])
            pre = cur[:]
        return pre[-1]

    # O(n) space
    def isInterleave3(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        dp = [True for _ in range(c+1)]
        for j in range(1, c+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, r+1):
            dp[0] = (dp[0] and s1[i-1] == s3[i-1])
            for j in range(1, c+1):
                dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]
                         ) or (dp[j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1]

    # DFS
    def isInterleave4(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        stack, visited = [(0, 0)], set((0, 0))
        while stack:
            x, y = stack.pop()
            if x+y == l:
                return True
            if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
                stack.append((x+1, y))
                visited.add((x+1, y))
            if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
                stack.append((x, y+1))
                visited.add((x, y+1))
        return False

    # BFS
    def isInterleave5(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        queue, visited = [(0, 0)], set((0, 0))
        while queue:
            x, y = queue.pop(0)
            if x+y == l:
                return True
            if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
                queue.append((x+1, y))
                visited.add((x+1, y))
            if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
                queue.append((x, y+1))
                visited.add((x, y+1))
        return False
