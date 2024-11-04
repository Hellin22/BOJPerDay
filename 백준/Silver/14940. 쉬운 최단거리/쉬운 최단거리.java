import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strs = br.readLine().split(" ");
        int n = Integer.parseInt(strs[0]);
        int m = Integer.parseInt(strs[1]);

        int[][] arr = new int[n][m];
        int[][] dp = new int[n][m];
        int[][] visited = new int[n][m];
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};

        for(int i = 0; i < n; i++) {
            Arrays.fill(dp[i], -1);
        }
        int x = 0, y = 0;
        for (int i = 0; i < n; i++) {
            strs = br.readLine().split(" ");
            for(int j = 0; j < m; j++){
                arr[i][j] = Integer.parseInt(strs[j]);
                if(arr[i][j] == 2){
                    x = i; y = j;
                    dp[i][j] = 0;
                }else if(arr[i][j] == 0){
                    dp[i][j] = 0;
                }
            }
        }
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        visited[x][y] = 1;
        while(!q.isEmpty()){
            int[] curs = q.poll();
            for(int i = 0; i < 4; i++){
                int nx = curs[0] + dx[i];
                int ny = curs[1] + dy[i];

                if(nx < 0 || ny < 0 || nx >= n || ny >= m || visited[nx][ny] == 1 || arr[nx][ny] == 0) continue;

                dp[nx][ny] = dp[nx][ny] == -1 ? dp[curs[0]][curs[1]] + 1 : Math.min(dp[nx][ny], dp[curs[0]][curs[1]] + 1);
                visited[nx][ny] = 1;
                q.add(new int[]{nx, ny});
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                sb.append(dp[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}