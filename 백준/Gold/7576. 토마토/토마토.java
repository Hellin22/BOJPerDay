
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;
import java.lang.StringBuilder;

class Main {

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strr = br.readLine().split(" ");
        int m = Integer.parseInt(strr[0]);
        int n = Integer.parseInt(strr[1]);
        int cnt = 0; // 최소일수
        int badTomato = 0;
        Queue<int[]> q = new LinkedList<>();

        int[][] arr = new int[n][m];
        int[][] isvisited = new int[n][m];

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            String[] strs = str.split(" ");
            for (int j = 0; j < strs.length; j++) {
                arr[i][j] = Integer.parseInt(strs[j]);
                if (arr[i][j] == 1) {
                    q.add(new int[]{i, j, 0});
                    isvisited[i][j] = 1;
                }
                if (arr[i][j] == 0) {
                    badTomato++;
                }
            }
        }
        if (badTomato == 0) {
            System.out.println(0);
            return;
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m || isvisited[nx][ny] == 1 || arr[nx][ny] == -1) continue;

                isvisited[nx][ny] = 1;
                badTomato--;
                cnt = cur[2] + 1;
                q.add(new int[]{nx, ny, cnt});
            }
        }

        int answer = 0;
        if (badTomato == 0) answer = cnt;
        else {
            answer = -1;
        }
        System.out.println(answer);
    }
}