
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


class Main {

    static int curx, cury, curdir;
    static int dx[] = new int[]{-1, 0, 1, 0};
    static int dy[] = new int[]{0, 1, 0, -1};
    static int count = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int n = Integer.parseInt(s[0]);
        int m = Integer.parseInt(s[1]);
        s = br.readLine().split(" ");
        curx = Integer.parseInt(s[0]);
        cury = Integer.parseInt(s[1]);
        curdir = Integer.parseInt(s[2]);

        int[][] arr = new int[n][m];
        int[][] isvisited = new int[n][m];
        for(int i = 0; i < n; i++) {
            String[] strs = br.readLine().split(" ");
            for(int j = 0; j < m; j++) {
                arr[i][j] = Integer.parseInt(strs[j]);
            }
        }

        while(true){
            // 1. 현재칸이 청소x -> 청소(isvisited 배열로 처리)
            if(arr[curx][cury] == 0 && isvisited[curx][cury] == 0){
                isvisited[curx][cury] = 1;
                count++;
            }

            // 1.5 -> 청소할 곳 존재 유무 찾는 로직
            boolean flag = false;
            for (int i = 0; i < 4; i++) {
                int nx = curx + dx[(curdir + i) % 4];
                int ny = cury + dy[(curdir + i) % 4];

                if(nx < 0 || ny < 0 || nx >= n || ny >= m
                || arr[nx][ny] == 1 || isvisited[nx][ny] == 1)continue;

//                System.out.println(nx + " " + ny + " " + arr[nx][ny] + " " + isvisited[nx][ny]);

                //System.out.println(curx  + " " + cury + " " + curdir + " " + count);
                flag = true;
                break;
            } // flag가 true -> 청소할곳 존재.

            // 2. 현재 칸 주변 4칸중 청소x가 존재 한다면
            if(flag){
                for (int i = 0; i < 4; i++) {
                    curdir = (curdir + 3) % 4;
                    int nx = curx + dx[curdir];
                    int ny = cury + dy[curdir];

                    if(nx < 0 || ny < 0 || nx >= n || ny >= m
                            || arr[nx][ny] == 1 || isvisited[nx][ny] == 1)continue;
                    curx = curx + dx[curdir];
                    cury = cury + dy[curdir];
                    break;
                }
            }

            // 3. 청소할곳이 없는 경우 (한칸 뒤로 갈 수 있으면 가고 벽이면 종료)
            else{
                curx += dx[(curdir + 2) % 4];
                cury += dy[(curdir + 2) % 4];

                if(arr[curx][cury] == 1) {
                    System.out.println(count);
                    return;
                }
//                int nx = curx;
//                int ny = cury;
//                while(true){
//                    nx += dx[(curdir + 2) % 4];
//                    ny += dy[(curdir + 2) % 4];
//                    if(nx < 0 || ny < 0 || nx >= n || ny >= m) continue; // 양 끝에는 벽임
//                    if(arr[nx][ny] == 1) {
//                        System.out.println(count);
//                        return;
//                    }
//                    if(isvisited[nx][ny] == 1) continue;
//
//                    // 갈수 있는곳
//                    curx = nx;
//                    cury = ny;
//                    break;
//                }
            }
        }


    }

}