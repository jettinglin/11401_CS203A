class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0)
        return false;
        long long int buffer;
        long long int original = x;
        while(x>0)
        {
            buffer = x%10 + buffer*10;
            x/=10;
        }
        if(buffer==original)
        return true;
        
        return false;

    }
};
