class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m: Dict[str, int] = {} # char: index
        l = 0
        m_l = 0

        for r in range(len(s)):
            if s[r] in m:
                l = max(m[s[r]] + 1, l) # move our window over since we saw a repeated char
            m[s[r]] = r # map the last time we saw this
            m_l = max(m_l, r - l + 1) # subtract how far to the right we got
        return m_l
