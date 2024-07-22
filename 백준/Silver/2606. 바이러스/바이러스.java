import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer>[] arr = new ArrayList[n+1];
        for(int i = 0; i < n+1; i++){
            arr[i] = new ArrayList<>();
        }

        int e = Integer.parseInt(br.readLine());
        for(int i = 0; i < e; i++){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to =Integer.parseInt(st.nextToken());
            arr[from].add(to);
            arr[to].add(from);
        }

        int[] isvisited = new int [n+1];
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        isvisited[1] = 1;
        int cnt = 0;

        while(!q.isEmpty()){
            int nodeNum = q.poll();

            for(int i = 0; i < arr[nodeNum].size(); i++){
                if(isvisited[arr[nodeNum].get(i)] == 0){
                    isvisited[arr[nodeNum].get(i)] = 1;
                    q.add(arr[nodeNum].get(i));
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
    }
}