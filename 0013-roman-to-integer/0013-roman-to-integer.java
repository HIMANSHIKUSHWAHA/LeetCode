class Solution {
    public int romanToInt(String s) {
     int[] integer = new int[26];
     integer['I'-'A']= 1;
     integer['V'-'A']= 5;
     integer['X'-'A']= 10;
     integer['L'-'A']= 50;
     integer['C'-'A']=100;
     integer['D'-'A']=500;
     integer['M'-'A']=1000;

     int total =0;
     int maxfar =0;

     for(int i = s.length()-1; i>=0; i--){
        int current =integer[s.charAt(i) -'A'];
        if(current < maxfar){
            total -= current;
        }
        else{
            total += current;
            maxfar = current;
        } 
        
          
        }
    return total;
    }
}