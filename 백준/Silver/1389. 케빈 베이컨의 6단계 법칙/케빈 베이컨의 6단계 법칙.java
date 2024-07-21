import java.io.*;
import java.util.Arrays;
import java.util.*;
public class Main {
    public static class pair{
        int x;
        int y;

        pair(int x, int y){
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        ArrayList<Integer>[] arr = new ArrayList[n+1];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = new ArrayList<Integer>();
        }

        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            arr[from].add(to);
            arr[to].add(from);
        }

        int[] isvisited = new int [n+1]; // 처음에 0으로 초기화 하고 접근 했는지 확인
        int[] baconCnt = new int [n+1]; // 1번부터 베이컨 수 적음

        Queue<pair> q = new LinkedList<>();

        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                isvisited[j] = 0;
            }
            int summ = 0;

            // 먼저 i번째 q에 넣기
            q.add(new pair(i, 0));
            isvisited[i] = 1;

            while(!q.isEmpty()){
                int node = q.peek().x;
                int cnt = q.poll().y;

                for(int j = 0; j < arr[node].size(); j++){
                    if(isvisited[arr[node].get(j)] == 0){
                        // 안갔다면
                        isvisited[arr[node].get(j)] = 1;
                        q.add(new pair(arr[node].get(j), cnt+1));
                        summ+=cnt+1;
                      }
                }
            }
            baconCnt[i] = summ;
        }

        int min = 10000;
        int nodeNum = -1;
        for(int i = 1; i < baconCnt.length; i++){
            if(min > baconCnt[i]){
                min = baconCnt[i];
                nodeNum = i;
            }
        }
        System.out.println(nodeNum);

    }
}