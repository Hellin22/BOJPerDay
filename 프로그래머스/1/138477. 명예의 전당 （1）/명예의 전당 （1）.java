import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        int[] answer = new int[score.length];
        
        for(int i = 0; i < score.length; i++){
            if(pq.size() < k){
                // 만약 pq의 사이즈가 k보다 작으면 그냥 넣으면 됨.
                pq.add(score[i]);
                System.out.println(pq.toString());
            }
            else{
                int a = pq.peek();
                if(a < score[i]){
                    pq.remove();
                    pq.add(score[i]);
                }
            }
            answer[i] = pq.peek();
        }

        return answer;
    }
}