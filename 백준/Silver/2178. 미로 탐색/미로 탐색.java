import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


class Main {

    public static class pair{
        int x;
        int y;
        int cnt;
        pair(int x, int y, int cnt){
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n + 1][m + 1]; // 1,1부터 시작
        int[][] isvisited = new int [n+1][m+1];
        for (int i = 1; i <= n; i++) {
            String str = br.readLine();
            for(int j = 0; j < str.length(); j++){
                arr[i][j+1] = str.charAt(j) - '0';
            }
        }

        Queue<pair> q = new LinkedList<>();
        q.add(new pair(1, 1, 1));
        isvisited[1][1] = 1;

        while(!q.isEmpty()){
            int x = q.peek().x;
            int y = q.peek().y;
            int cnt = q.poll().cnt;
            
            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if(nx <= 0 || ny <= 0 || nx >= n+1 || ny >= m+1
                        || isvisited[nx][ny] == 1 || arr[nx][ny] == 0) continue;
                
                if(nx == n && ny == m){
                    System.out.println(cnt + 1);
                    return;
                }

                q.add(new pair(nx, ny, cnt+1));
                isvisited[nx][ny] = 1;
            }
        }
    }
}