import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;

        // p와 y의 개수를 비교한다. -> 대소문자 구분 안함
        StringBuilder sb = new StringBuilder(s);
        for(int i = 0; i < sb.length(); i++){
            sb.setCharAt(i, Character.toLowerCase(sb.charAt(i)));
        }
        int pcnt = 0;
        int ycnt = 0;
        for(int i = 0; i < sb.length(); i++){
            if (sb.charAt(i) == 'y'){
                ycnt+=1;
            }else if(sb.charAt(i) == 'p'){
                pcnt+=1;
            }
        }
        if(pcnt != ycnt){
            answer = false;
        }
        
        return answer;
    }
}