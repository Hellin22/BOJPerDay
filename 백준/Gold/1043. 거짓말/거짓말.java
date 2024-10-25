import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int cnt = m;
        boolean[] canLying = new boolean[n+1]; // 거짓말 할 수 있는 사람.
        Arrays.fill(canLying, true);

        String[] strs = br.readLine().split(" ");
        String[] strstrs = new String[m];
        for(int i = 1; i <= Integer.parseInt(strs[0]); i++){
            canLying[Integer.parseInt(strs[i])] = false; // 거짓말 못함.
        }

        HashSet<Integer>[] sets = new HashSet[n+1]; // 1 ~ n번까지의 사람 그래프

        for(int i = 0; i <= n; i++){
            sets[i] = new HashSet<>();
        }

        for(int i = 0; i < m; i++){
            strstrs[i] = br.readLine();
            strs = strstrs[i].split(" ");

            int peopleCnt = Integer.parseInt(strs[0]);
            // 연결되어있다고 표시해줘야한다.

            for(int j = 1; j < peopleCnt; j++){

                for(int k = j+1; k <= peopleCnt; k++){
                    sets[Integer.parseInt(strs[j])].add(Integer.parseInt(strs[k]));
                    sets[Integer.parseInt(strs[k])].add(Integer.parseInt(strs[j]));
                }
            }
        }



        // sets[i]에는 i 번호를 가진 사람과 연결된 모든 번호를 알 수 있음.
        // 먼저 sets를 1~n번까지 돌면서 canlying 초기화 시키기
        // bfs를 돌려야함.
        int[] visited = new int[n+1];
        for(int i = 1; i <= n; i++){
            Arrays.fill(visited, 0);
            Queue<Integer> q = new LinkedList<>();
            Iterator<Integer> it = sets[i].iterator();
            while(it.hasNext()){
                int k = it.next();
                q.offer(k);
                visited[k] = 1;
            }
            while(!q.isEmpty()){
                int link = q.poll();
                Iterator<Integer> iterator = sets[link].iterator();
                while(iterator.hasNext()){
                    int k = iterator.next();
                    if(visited[k] == 0){
                        q.offer(k);
                        visited[k] = 1;
                    }
                    if(canLying[k] == false) {
                        canLying[i] = false;
                        break;
                    }
                }
                if(!canLying[i]) break;
            }
        }

        for(int i = 0; i < strstrs.length; i++){
            strs = strstrs[i].split(" ");
            if(canLying[Integer.parseInt(strs[1])] == false){
                cnt--;
            }
        }

        System.out.println(cnt);
    }
}