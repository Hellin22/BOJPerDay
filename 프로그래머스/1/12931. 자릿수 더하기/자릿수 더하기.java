import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        // 자릿수를 더하는 코드
        
        String str = n+"";
        for (int i = 0; i < str.length(); i++){
            
            answer += str.charAt(i) - '0';
        }
        
        
        
        return answer;
    }
}