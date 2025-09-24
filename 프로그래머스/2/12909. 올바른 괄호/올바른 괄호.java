import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Integer> stck = new Stack<>();
        
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '('){
                stck.push(0);
            }
            else if(s.charAt(i) == ')'){
                if(stck.size() != 0){
                    stck.pop();             
                }
                else{
                    return false;
                }
            }
        }
        if (stck.size() == 0){
            return true;
        }else{
            return false;
        }
    }
}