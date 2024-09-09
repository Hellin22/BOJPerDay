import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strs = br.readLine().split(" ");
        int n = Integer.parseInt(strs[0]);
        int m = Integer.parseInt(strs[1]);

        int[][] arr = new int[n+1][m+1];
        int[][] visited = new int[n+1][m+1];
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        for(int i = 1; i <= n; i++){
            String str = br.readLine();
            for(int j = 0; j < str.length(); j++){
                arr[i][j+1] = str.charAt(j) - '0';
            }
        }

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{1, 1, 1});
        visited[1][1] = 1;

        while(!q.isEmpty()){
            int[] cur = q.poll();

            for(int i = 0; i < 4; i++){
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];

                if(nx <= 0 || ny <= 0 || nx > n || ny > m
                || visited[nx][ny] == 1 || arr[nx][ny] == 0) continue;

                if(nx == n && ny == m){
                    System.out.println(cur[2]+1);
                    return;
                }
                q.add(new int[]{nx, ny, cur[2] + 1});
                visited[nx][ny] = 1;
            }
        }
    }
}