import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        // 1. 모든곳 -1로 초기화 arr(벽인지 판별), dist(거리배열 -> 이걸 -1로 초기화), isvisitied(방문배열)
        // 2. 벽인 경우에는 좌표를 따로 저장하는 배열 가지고있기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] ss = br.readLine().split(" ");
        int n = Integer.parseInt(ss[0]);
        int m = Integer.parseInt(ss[1]);

        int[][] arr = new int[n][m];
        int[][] dist = new int[n][m];
        int[][] isvisited = new int[n][m];
        int[] start = new int[2];
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        // 벽 좌표 담아둘 공간
        ArrayList<int[]> wall = new ArrayList<>();

        for(int i = 0; i < n; i++){
            String[] strs = br.readLine().split(" ");
            for(int j = 0; j < strs.length; j++){
                dist[i][j] = -1;
                arr[i][j] = Integer.parseInt(strs[j]);

                if(arr[i][j] == 2) {
                    dist[i][j] = 0;
                    start[0] = i;
                    start[1] = j;
                }
                if(arr[i][j] == 0) wall.add(new int[]{i, j}); // 마지막에 wall 좌표에 대한 dist 초기화
            }
        }

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{start[0], start[1], dist[start[0]][start[1]]});
        isvisited[start[0]][start[1]] = 1;
        while(!q.isEmpty()){
            int[] cur = q.poll();

            for(int i = 0; i < 4; i++){
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];

                if(nx < 0 || ny < 0 || nx >= n || ny >= m
                    || arr[nx][ny] == 0 || isvisited[nx][ny] == 1) continue;

                q.add(new int[]{nx, ny, cur[2] + 1});
                dist[nx][ny] = cur[2] + 1;
                isvisited[nx][ny] = 1;
            }
        }

        for(int i = 0; i < wall.size(); i++) dist[wall.get(i)[0]][wall.get(i)[1]] = 0;
        
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                sb.append(dist[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
