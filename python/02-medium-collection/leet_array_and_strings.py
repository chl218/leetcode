from typing import List

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    """Group Anagrams

    Given an array of strings, group anagrams together.

    Example:
        Input:  ["eat", "tea", "tan", "ate", "nat", "bat"],
        Output: [["ate","eat","tea"], ["nat","tan"], ["bat"]]

    Note:
        - All inputs will be in lowercase.
        - The order of your output does not matter.
    """
    lst = []
    dic = {}
    idx = 0
    
    for word in strs:
        key = ''.join(sorted(word))
        
        if key in dic:
            lst[dic[key]].append(word)
        else:
            lst.append([word])
            dic[key] = idx
            idx += 1
            
    return lst