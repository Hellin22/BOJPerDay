import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


class Main {
    public static void main(String[] args) throws IOException {
        // 굳이 배열? -> 그냥 숫자 가지고 놀기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashMap<Integer, Integer> sadari = new HashMap<>();
        HashMap<Integer, Integer> snake = new HashMap<>();
        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());

            sadari.put(from, to);
        }

        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());

            snake.put(from, to);
        }

        // 1번에서 100번까지 진행

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{1, 0});
        int[] isvisited = new int [101];
        isvisited[1] = 1;

        while(!q.isEmpty()){
            int from = q.peek()[0];
            int cnt = q.poll()[1];

            for(int i = 1; i <=6; i++){
                if(from + i == 100){
                    System.out.println(cnt + 1);
                    return;
                }
                if(from + i <= 99) {
                    if(isvisited[from + i] == 0){
                        int finalTo;
                        // sadari 타기
                        if(sadari.containsKey(from + i)){
                            isvisited[from + i] = 1;
                            isvisited[sadari.get(from + i)] = 1;
                            finalTo = sadari.get(from + i);
                            sadari.remove(from + i);
                        }else if(snake.containsKey(from + i)){
                            isvisited[from + i] = 1;
                            isvisited[snake.get(from + i)] = 1;
                            finalTo = snake.get(from + i);
                            snake.remove(from + i);
                        }else{
                            isvisited[from + i] = 1;
                            finalTo = from+i;
                        }

                        if(finalTo == 100){
                            System.out.println(cnt + 1);
                            return;
                        }
                        q.add(new int[]{finalTo, cnt + 1});
                    }
                }
            }

        }
    }
}