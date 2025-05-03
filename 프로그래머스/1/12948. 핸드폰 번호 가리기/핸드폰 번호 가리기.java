import java.util.*;

class Solution {
    public String solution(String phone_number) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        for(int i = phone_number.length()-1; i >= 0; i--){
            if(cnt <= 3){
                sb.append(phone_number.charAt(i));
            }
            else{
                sb.append("*");
            }
            cnt+=1;
        }
        
        return sb.reverse().toString();
    }
}