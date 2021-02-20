"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.


Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]

Example 3:

Input: S = "12345"
Output: ["12345"]

Example 4:

Input: S = "0"
Output: ["0"]


Constraints:

   - S will be a string with length between 1 and 12.
   - S will consist only of letters or digits.

"""


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:

        perm = []
        digits = ""

        for i in range(len(S)):
            if S[i].isalpha():
                sub_perm = self.letterCasePermutation(S[i+1:])
                cap = S[i].upper()
                low = S[i].lower()

                if sub_perm:
                    for sub in sub_perm:
                        perm.append(digits + cap + sub)
                        perm.append(digits + low + sub)
                else:
                    perm.append(digits + cap)
                    perm.append(digits + low)

                digits = ""
                break
            else:
                digits += S[i]

        if len(digits) > 0:
            perm.append(digits)

        return perm
