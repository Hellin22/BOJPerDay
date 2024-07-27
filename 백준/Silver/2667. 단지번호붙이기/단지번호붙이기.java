import java.io.*;
import java.util.Arrays;
import java.util.*;
public class Main {

    static int[][] arr;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String args[]) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        arr = new int[n][n];

        for(int i = 0; i < n; i++){
            String str = br.readLine();
            for(int j = 0; j < n; j++){
                arr[i][j] = str.charAt(j) - '0';
            }
        }
        ArrayList<Integer> houseCntPerDanji = new ArrayList<>();
        int[][] isvisited = new int[n][n];
        int danjiCnt = 0;
        int curDanjiHouseCnt = 0;

        Queue<int[]> q = new LinkedList<>();

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(arr[i][j] == 1 && isvisited[i][j] == 0){
                    q.add (new int[]{i, j});
                    isvisited[i][j] = 1;
                    curDanjiHouseCnt = 1;

                    while(!q.isEmpty()){
                        int[] cur = q.poll();

                        for(int k = 0; k < 4; k++){
                            int nx = cur[0] + dx[k];
                            int ny = cur[1] + dy[k];

                            if(nx < 0 || ny < 0 || nx >= n || ny >= n || isvisited[nx][ny] == 1 || arr[nx][ny] == 0)continue;

                            q.add(new int[]{nx, ny});
                            isvisited[nx][ny] = 1;
                            curDanjiHouseCnt++;
                        }
                    }

                    houseCntPerDanji.add(curDanjiHouseCnt);
                }
            }
        }

        Collections.sort(houseCntPerDanji);
        sb.append(houseCntPerDanji.size() + "\n");
        for(int i = 0; i < houseCntPerDanji.size(); i++){
            sb.append(houseCntPerDanji.get(i) + "\n");
        }
        System.out.println(sb);
    }
}