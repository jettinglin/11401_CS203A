class Solution {
public:
    int romanToInt(string s) {
        map <char,int> romance = {
            {'I',1},
            {'V',5},
            {'X',10},
            {'L',50},
            {'C',100},
            {'D',500},
            {'M',1000},
        };
        int result = 0;
        for(int i=0;i<s.size();i++)
        {
            if(i+1<s.size()&&romance[s[i]]<romance[s[i+1]])
            result-=romance[s[i]];
            else
            result+=romance[s[i]];
        }
        return result;
    }
};
