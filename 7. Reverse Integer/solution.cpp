#include <iostream>
#include <string>
#include <algorithm>
#include <climits>

class Solution {
public:
    int reverse(int x) {
        // Determine the sign of the number
        int numSign = (x < 0) ? -1 : 1;
        
        // Convert the absolute value of the number to a string
        std::string str = std::to_string(std::abs(x));
        
        // Reverse the string
        std::reverse(str.begin(), str.end());
        
        // Convert the string back to an integer
        long long newNum = std::stoll(str);
        
        // Check for overflow
        if (newNum > INT_MAX) {
            return 0;
        }
        
        // Return the reversed number with the original sign
        return static_cast<int>(newNum) * numSign;
    }
};