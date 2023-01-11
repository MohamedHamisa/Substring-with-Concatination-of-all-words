            
class Solution:
    def findSubstring(self, s: str, words: List[str]):
        if not words: return []
        k = len(words[0])
        res = []
        
        # [aaa]bbbccc, then a[aab]bbccc, then aa[abb]bccc
        for left in range(k):
            # Init counter
            d = collections.Counter(words)
            
            # For first iteration of left:
            # Iterate through each [aaa]{b}bbccc, then [aaa]bbb{c}cc, then [aaa]bbbccc{}
            for right in range(left + k, len(s) + 1, k):
                # Grab the preceding word: aaa, then bbb, then ccc
                word = s[right - k: right]
                d[word] -= 1

                # If a word is seen that shouldn't have been seen before,
                # Push left all the way up until it hits right
                # Anything we've seen before is skipped
                while d[word] < 0:
                    d[s[left:left + k]] += 1
                    left += k
                    
                # If, however, we don't push left, and we've explored enough
                # that our window is the size of the words we need to find
                if left + k * len(words) == right:
                    res.append(left)
        return res     



            
