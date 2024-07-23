public class Solution {
    public int reverse(int x) {
        // Determine the sign of the number
        int numSign = (x < 0) ? -1 : 1;
        
        // Convert the absolute value of the number to a string
        String str = Integer.toString(Math.abs(x));
        
        // Reverse the string
        String reversedStr = new StringBuilder(str).reverse().toString();
        
        // Convert the string back to an integer
        long newNum;
        try {
            newNum = Long.parseLong(reversedStr);
        } catch (NumberFormatException e) {
            return 0;
        }
        
        // Check for overflow
        if (newNum > Integer.MAX_VALUE) {
            return 0;
        }
        
        // Return the reversed number with the original sign
        return (int) newNum * numSign;
    }
}
