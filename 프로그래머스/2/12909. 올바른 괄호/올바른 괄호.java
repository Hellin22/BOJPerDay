import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stck = new Stack<>();
        for(int i = 0; i < s.length(); i++){
            if (s.charAt(i) == '('){
                stck.add('(');
            }
            else{ // )
                if(stck.empty()) return false;
                else{
                    stck.pop();
                }
            }
        }
        if (!stck.empty()) return false;
        
        return answer;
    }
}