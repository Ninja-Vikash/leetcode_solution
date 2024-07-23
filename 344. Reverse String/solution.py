class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Swap characters at left and right indices
            s[left], s[right] = s[right], s[left]
            
            # Move towards the middle
            left += 1
            right -= 1