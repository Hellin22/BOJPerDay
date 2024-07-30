
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

class Main {

    public static class shark{
        int x;
        int y;

        public shark(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    public static class pair implements Comparable<pair>{
        int x;
        int y;

        public pair(int x, int y){
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(pair o) {
            if(this.x == o.x){
                return this.y - o.y;
            }
            return this.x - o.x;
        }
    }

    static int[][] arr = new int[20][20];
    static int[][] isvisited = new int[20][20];
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int babySharkSize = 2;
    static int time = 0; // 1씩 증가시키기
    static int babySharkEaten = 0; // 상어가 먹은 물고기 수
    static shark sharkXY; // 아기상어의 xy 좌표

    public static void main(String[] args) throws IOException {
        // 1. 물고기 1마리 -> 그거 먹기
        // 2. 물고기 여러마리 -> 가장 가까운 물고기
        // 3. 거리 동일 -> 가장 위 + 가장 왼쪽 // 이걸 찾기
        // 크기가 동일한건 지나갈수있고 작은거 먹을수 있음.
        // 아기상어는 크기가 커지기도함.

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++) {
            String[] strs = br.readLine().split(" ");
            for(int j = 0; j < strs.length; j++) {
                arr[i][j] = Integer.parseInt(strs[j]);
                if(arr[i][j] == 9){
                    sharkXY = new shark(i, j);
                }
            }
        }

        // 큐에는 어떤 데이터 (거리cnt, x, y)
        Queue<int[]> q = new LinkedList<>();
        ArrayList<pair> arrlist = new ArrayList<>();
        int eatingCnt = 100;
        while(true){
            arrlist.clear();
            eatingCnt = 10000;

            q.add(new int[]{sharkXY.x, sharkXY.y, 0});

            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    isvisited[i][j] = 0;
                }
            }

            isvisited[sharkXY.x][sharkXY.y] = 1;
            while(!q.isEmpty()){
                int[] curs = q.poll();

                if(curs[2] >= eatingCnt) continue;

                for(int i = 0; i < 4; i++){
                    int nx = curs[0] + dx[i];
                    int ny = curs[1] + dy[i];

                    if(nx < 0 || ny < 0 || nx >= n || ny >= n
                            || isvisited[nx][ny] == 1 || arr[nx][ny] > babySharkSize) continue;

                    if(arr[nx][ny] > 0 && arr[nx][ny] != babySharkSize) {
                        eatingCnt = curs[2] + 1;

                        arrlist.add(new pair(nx, ny));
                    }
                    isvisited[nx][ny] = 1;
                    q.add(new int[]{nx, ny, curs[2] + 1});

                }
            }
            if(eatingCnt == 10000) {
                break;
            }
            else Collections.sort(arrlist);

            babySharkEaten++;
            if(babySharkEaten == babySharkSize){
                babySharkEaten = 0;
                babySharkSize++;
            }
            arr[sharkXY.x][sharkXY.y] = 0;
            sharkXY.x = arrlist.get(0).x;
            sharkXY.y = arrlist.get(0).y;
            arr[sharkXY.x][sharkXY.y] = 9;

            time+=eatingCnt;
        }
        System.out.println(time);

    }
}