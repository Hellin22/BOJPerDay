
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Queue;
import java.util.LinkedList;


class Main{

    static int n, m, startv, from, to;
    static ArrayList<Integer>[] arr;
    static int isvisited[];
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        startv = Integer.parseInt(st.nextToken());
        isvisited = new int[n+1];

        int from, to;
        arr =  new ArrayList[n+1];
        for(int i = 0; i < n+1; i++){
            arr[i] = new ArrayList<>();
        }
        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            from = Integer.parseInt(st.nextToken());
            to = Integer.parseInt(st.nextToken());
            arr[from].add(to);
            arr[to].add(from);
        }
        // 방문할 수 있는 정점이 여러개 -> 정점번호 작은거 먼저 감

        for(int i = 1; i <= n; i++){
            Collections.sort(arr[i]); // 오름차순 정렬
        }
        dfs(startv);

        for(int i = 0; i < isvisited.length; i++){
            isvisited[i] = 0;
        }

        bfs(startv);

        System.out.println(sb);
    }

    public static void dfs(int node){
        sb.append(node + " ");
        isvisited[node] = 1;

        for(int i = 0; i < arr[node].size(); i++){
            if(isvisited[arr[node].get(i)] == 0){
                isvisited[arr[node].get(i)] = 1;
                dfs(arr[node].get(i));
            }
        }
    }

    public static void bfs(int node){
        sb.append("\n");
        Queue<Integer> q = new LinkedList<>();
        q.add(node);
        isvisited[node] = 1;

        while(!q.isEmpty()){
            int num = q.poll();
            sb.append(num + " ");

            for(int i = 0; i < arr[num].size(); i++){
                if(isvisited[arr[num].get(i)] == 0){
                    isvisited[arr[num].get(i)] = 1;
                    q.add(arr[num].get(i));
                }
            }
        }
    }
}