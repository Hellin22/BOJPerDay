import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static class pair implements Comparable<pair> {
        int x;
        int y;

        public pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(pair o) {
            return 0;
        }
    }

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());
        while(t-->0){
            st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());
            int locCnt = Integer.parseInt(st.nextToken());

            int[][] arr = new int[m][n];
            int[][] isvisited = new int[m][n];
            for(int i = 0; i < locCnt; i++){
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                arr[x][y] = 1;
            }
            int cnt = 0;
            Queue<pair> q = new LinkedList<>();
            for(int i = 0; i < m; i++){
                for(int j = 0; j < n; j++){
                    if(arr[i][j] == 1 && isvisited[i][j] == 0){
                        cnt++;
                        q.add(new pair(i, j));
                        isvisited[i][j] = 1;
                        while(!q.isEmpty()){
                            int xx = q.peek().x;
                            int yy = q.poll().y;

                            for(int k = 0; k < 4; k++){
                                int nx = xx + dx[k];
                                int ny = yy + dy[k];
                                if(nx < 0 || ny < 0 || nx >= m || ny >= n || arr[nx][ny] == 0 || isvisited[nx][ny] == 1)continue;
                                if(arr[nx][ny] == 1){
                                    q.add(new pair(nx, ny));
                                    isvisited[nx][ny] = 1;
                                }
                            }
                        }
                    }
                }
            }
            System.out.println(cnt);
        }
    }
}