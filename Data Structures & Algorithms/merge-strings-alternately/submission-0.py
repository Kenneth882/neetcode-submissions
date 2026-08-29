class Solution(object):
    def mergeAlternately(self, word1, word2):
        new_str = []
        i = 0
        len1, len2 = len(word1), len(word2)

    
        while i < len1 or i < len2:
            if i < len1:
                new_str.append(word1[i])
            if i < len2:
                new_str.append(word2[i])
            i += 1

        return ''.join(new_str)
