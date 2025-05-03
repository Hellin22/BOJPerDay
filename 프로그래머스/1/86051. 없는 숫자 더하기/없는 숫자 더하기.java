import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        
        int[] nums = new int[10];
        for(int i = 0; i < numbers.length; i++){
            nums[numbers[i]] = 1;
        }
        
        for(int i = 0; i < 10; i++){
            if(nums[i] == 0){
                answer+=i;
            }
        }
        
        return answer;
    }
}