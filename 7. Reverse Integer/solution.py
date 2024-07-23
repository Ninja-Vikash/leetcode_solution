class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign of the number
        numSign = -1 if x < 0 else 1
        
        # Convert the absolute value of the number to a string
        str_x = str(abs(x))
        
        # Reverse the string
        reversed_str_x = str_x[::-1]
        
        # Convert the string back to an integer
        newNum = int(reversed_str_x)
        
        # Check for overflow
        if newNum > 2**31 - 1:
            return 0
        
        # Return the reversed number with the original sign
        return newNum * numSign