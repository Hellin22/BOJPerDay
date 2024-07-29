
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;
import java.lang.StringBuilder;

class Main {
    static int[][] arr;
    static int[][] arr2;
    static int[][] isvisited;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];
        arr2 = new int[n][n];
        isvisited = new int[n][n];
        for(int i = 0; i < n; i++) {
            String str = br.readLine();
            for(int j = 0; j < str.length(); j++){
                if(str.charAt(j) == 'R'){
                    arr[i][j] = 0;
                    arr2[i][j] = 0;
                }
                else if(str.charAt(j) == 'G'){
                    arr[i][j] = 1;
                    arr2[i][j] = 0;
                }
                else {
                    arr[i][j] = 2;
                    arr2[i][j] = 2;
                }
            }
        } // 0, 1
        bfsNormal();
        bfsRedGreen();

    }

    public static void bfsNormal(){
        int curCnt = 0;
        int curNum = 0;
        Queue<int[]> q = new LinkedList<>();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(isvisited[i][j] == 0){
                    curCnt++;
                    curNum = arr[i][j];
                    isvisited[i][j] = 1;
                    q.add(new int[]{i, j});
                    while(!q.isEmpty()){
                        int[]curs = q.poll();

                        for(int k = 0; k < 4; k++){
                            int nx = curs[0] + dx[k];
                            int ny = curs[1] + dy[k];

                            if(nx < 0 || ny < 0 || nx >= n || ny >= n
                                    || isvisited[nx][ny] == 1 || arr[nx][ny] != curNum) continue;

                            q.add(new int[]{nx, ny});
                            isvisited[nx][ny] = 1;
                        }
                    }
                }
            }
        }
        System.out.println(curCnt);
    }

    public static void bfsRedGreen(){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                isvisited[i][j] = 0;
            }
        }
        int curCnt = 0;
        int curNum = 0;
        Queue<int[]> q = new LinkedList<>();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(isvisited[i][j] == 0){
                    curCnt++;
                    curNum = arr2[i][j];
                    isvisited[i][j] = 1;
                    q.add(new int[]{i, j});
                    while(!q.isEmpty()){
                        int[]curs = q.poll();

                        for(int k = 0; k < 4; k++){
                            int nx = curs[0] + dx[k];
                            int ny = curs[1] + dy[k];

                            if(nx < 0 || ny < 0 || nx >= n || ny >= n
                                    || isvisited[nx][ny] == 1 || arr2[nx][ny] != curNum) continue;

                            q.add(new int[]{nx, ny});
                            isvisited[nx][ny] = 1;
                        }
                    }
                }
            }
        }
        System.out.println(curCnt);

    }

}