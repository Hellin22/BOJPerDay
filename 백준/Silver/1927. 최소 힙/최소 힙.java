import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


class Main {
    public static void main(String[] args) throws IOException {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        // 최소힙으로 생성
        StringBuilder sb = new StringBuilder();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++){
            int inputNum = Integer.parseInt(br.readLine());
            if(inputNum == 0){
                if(pq.isEmpty()){
                    sb.append("0" + "\n");
                }else{
                    // 가장 작은값 출력 후 제거
                    sb.append(pq.poll()).append("\n");
                }
            }
            else{
                pq.add(inputNum);
            }
        }
        System.out.println(sb);
    }
}