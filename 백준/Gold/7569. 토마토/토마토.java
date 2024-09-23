import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strs = br.readLine().split(" ");
        int m = Integer.parseInt(strs[0]);
        int n = Integer.parseInt(strs[1]);
        int h = Integer.parseInt(strs[2]);

        int[] dx = {0, 1, 0, -1, 0, 0}; // 동남서북 위 아래
        int[] dy = {1, 0, -1, 0, 0, 0};
        int[] dz = {0, 0, 0, 0, 1, -1};

        int[][][] arr = new int[h][n][m];
        int[][][] visited = new int[h][n][m];
        // n m h
        // 000 001 002 003  -> h가 제일 앞에 나와야겟네
        // 010 011 012 013

        int badTomato = 0; // 모두 익을때까지 며칠?
        int cnt = 0;
        Queue<int[]> q = new LinkedList<>();

        for(int i = 0; i < h; i++){
            for(int j = 0; j < n; j++){
                String[] strings = br.readLine().split(" ");
                for(int k = 0; k < m; k++){
                    arr[i][j][k] = Integer.parseInt(strings[k]);
                        if(arr[i][j][k] == 0) badTomato++;
                        else if(arr[i][j][k] == 1){
                        q.add(new int[]{i, j, k, cnt}); // 처음에 0 추가
                        visited[i][j][k] = 1;
                    }
                }
            }
        }

        if(badTomato == 0) {
            System.out.println(0);
            return;
        }

        // cnt는 계속해서 max 값으로 바꿔주기
        while(!q.isEmpty()){
            int[] curs = q.poll();

            for(int i = 0; i < 6; i++){

                int nz = dz[i] + curs[0];
                int nx = dx[i] + curs[1];
                int ny = dy[i] + curs[2];

                if(nx < 0 || ny < 0 || nz < 0 || nx >= n || ny >= m || nz >= h
                        || visited[nz][nx][ny] == 1 || arr[nz][nx][ny] == -1) continue;

                cnt = Math.max(curs[3] + 1, cnt);
                q.add(new int[]{nz, nx, ny, curs[3] + 1});
                badTomato--;
                visited[nz][nx][ny] = 1;
            }
        }
        System.out.println((badTomato != 0) ? -1 : cnt);
    }
}