# LeetCode
# 2114
# Maximum Number of Words Found in Sentences

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0
        
        for sentence in sentences:
            if len(sentence.split(' ')) > max_count:
                max_count = len(sentence.split(' '))
        
        return max_count
        