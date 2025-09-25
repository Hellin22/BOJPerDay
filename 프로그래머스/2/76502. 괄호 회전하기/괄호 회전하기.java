import java.util.*;
class Solution {
    public int solution(String s) {
        int answer = 0;
        
        // 왼쪽으로 s를 x칸 회전
        for(int i = 0; i < s.length(); i++){
            Stack<Integer> stck = new Stack<>();
            boolean isValid = true;
            
            // i부터 끝까지 처리
            for(int j = i; j < s.length() && isValid; j++){
                if(s.charAt(j) == '['){
                    stck.push(1);
                }else if(s.charAt(j) == '{'){
                    stck.push(2);
                }else if(s.charAt(j) == '('){
                    stck.push(3);
                }else { // 닫는 괄호들
                    if(stck.empty()) {
                        isValid = false;
                        break;
                    }
                    
                    if(s.charAt(j) == ']' && stck.peek() == 1){
                        stck.pop();
                    }else if(s.charAt(j) == '}' && stck.peek() == 2){
                        stck.pop();
                    }else if(s.charAt(j) == ')' && stck.peek() == 3){
                        stck.pop();
                    }else {
                        // 매칭되지 않는 경우
                        isValid = false;
                        break;
                    }
                }
            }
            
            // 0부터 i-1까지 처리
            for (int j = 0; j < i && isValid; j++){
                if(s.charAt(j) == '['){
                    stck.push(1);
                }else if(s.charAt(j) == '{'){
                    stck.push(2);
                }else if(s.charAt(j) == '('){
                    stck.push(3);
                }else { // 닫는 괄호들
                    if(stck.empty()) {
                        isValid = false;
                        break;
                    }
                    
                    if(s.charAt(j) == ']' && stck.peek() == 1){
                        stck.pop();
                    }else if(s.charAt(j) == '}' && stck.peek() == 2){
                        stck.pop();
                    }else if(s.charAt(j) == ')' && stck.peek() == 3){
                        stck.pop();
                    }else {
                        // 매칭되지 않는 경우
                        isValid = false;
                        break;
                    }
                }
            }
            
            if(isValid && stck.size() == 0){
                answer += 1;
            }
        }
        
        return answer;
    }
}