class Solution {
public:
    string ans = "1";
    void rle(string s , int count)
    {
        ans.clear();
        if(s.size() == 1)
        {
            count--;
            ans = "11";
        }
        else
        {
            for(int i = 0 ; i < s.size() ; i++)
            {
                int c = 1;
                if(s[i] != s[i+1])
                {
                    ans += to_string(c);
                    ans += s[i] ;                
                }
                else if(s[i] == s[i+1])
                {
                    while(i < s.size()-1 && s[i] == s[i+1])
                    {
                        c++;
                        i++;
                    }
                    ans += to_string(c);
                    ans += s[i];
                }
            }
        }
    }
    string countAndSay(int n) {
        if(n == 1) return "1";
        while(--n > 0)
        {
            rle(ans,n-1);
        }
        return ans;
    }
};