import java.util.*;

class Solution {
    
    public static double solution(int[] arr) {
        double answer = 0;
        int ans = 0;
        for(int i = 0; i < arr.length; i++){
            ans += arr[i];
        }

        answer = (double) ans / arr.length;

        return answer;
    }
}