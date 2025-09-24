class Solution {
    public int solution(int n) {
    
        int answer = 0;
        if (n == 1){
            return 1;
        }

        int left = 1;
        int right = 2;
        int summ = 3;
        while (left < right && right < n) {
            if (summ == n){
                answer+=1;
                summ -= left;
                left += 1;
            }
            else if (summ < n){
                right += 1;
                summ += right;
            }
            else if (summ > n){
                summ -= left;
                left += 1;
            }
        }

        return answer+1;
    }
    
}