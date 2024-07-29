
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;
import java.lang.StringBuilder;

class Main {

    static int[][] arr;
    static int[][] isvisited;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int n, m;
    static int[] alphabet = new int[26];
    static int maxCnt = 1;
    static int curCnt = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] strs = br.readLine().split(" ");
        n = Integer.parseInt(strs[0]);
        m = Integer.parseInt(strs[1]);
        arr = new int[n][m];
        isvisited = new int[n][m];

        for(int i = 0; i < n; i++){
            String str = br.readLine();
            for(int j = 0; j < str.length(); j++){
                arr[i][j] = str.charAt(j) - 'A';
            }
        }

        // 0, 0을 지나야함.
        isvisited[0][0] = 1;
        alphabet[arr[0][0]] = 1;
        dfs(0, 0);

        System.out.println(maxCnt);
    }

    public static void dfs(int x, int y){

        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || ny < 0 || nx >= n || ny >= m
                || isvisited[nx][ny] == 1 || alphabet[arr[nx][ny]] == 1) continue;

            alphabet[arr[nx][ny]] = 1;
            isvisited[nx][ny] = 1;
            curCnt++;
            maxCnt = Math.max(maxCnt, curCnt);

            dfs(nx, ny);
            alphabet[arr[nx][ny]] = 0;
            isvisited[nx][ny] = 0;
            curCnt--;
        }
    }

}