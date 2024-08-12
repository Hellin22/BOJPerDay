import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strs = br.readLine().split(" ");
        int n = Integer.parseInt(strs[0]);
        int m = Integer.parseInt(strs[1]);

        int[][] arr = new int[n][m];
        int[][] visited = new int[n][m];
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int answer = 0;
        Queue<int[]> q = new LinkedList<>();

        for(int i = 0; i < n; i++){
            String s = br.readLine();
            for(int j = 0; j < s.length(); j++){
                if (s.charAt(j) == 'O') arr[i][j] = 0;
                else if (s.charAt(j) == 'X') arr[i][j] = -1;
                else if(s.charAt(j) == 'I') {
                    visited[i][j] = 1;
                    q.add(new int[]{i, j});
                }else if(s.charAt(j) == 'P') {
                    arr[i][j] = 1;
                }
            }
        }

        while(!q.isEmpty()){
            int[] cur = q.poll();

            for(int i = 0; i < 4; i++){
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];

                if(nx < 0 || ny < 0 || nx >= n || ny >= m ||
                    visited[nx][ny] == 1 || arr[nx][ny] == -1) continue;
                if(arr[nx][ny] == 1) answer++;

                q.add(new int[]{nx, ny});
                visited[nx][ny] = 1;
            }
        }
        if(answer == 0) System.out.println("TT");
        else System.out.println(answer);
    }
}
