import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        StringTokenizer st = new StringTokenizer(s);
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        if(n == k) {
            System.out.println(0);
            return;
        }
        boolean[] isvisited = new boolean[100001];
        // 만약 isDouble에 안들어왔다면 시작하기.

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
                    if(a[1] != b[1])
                        return a[1] - b[1];
                    else
                        return a[0] - b[0];
                });
        pq.offer(new int[]{n, 0}); // n이 위치의미
        isvisited[n] = true;
        while(true){
            int[] arr = pq.poll();
            int cur = arr[0];
            int ttime = arr[1];

            if(cur * 2 <= 100000 && !isvisited[cur * 2]){
                if(cur * 2 == k) {
                    System.out.println(ttime);
                    return;
                }
                pq.offer(new int[]{cur * 2, ttime});
                isvisited[cur] = true;
            }
            if(cur - 1 >= 0 && !isvisited[cur - 1]){
                if(cur - 1 == k){
                    System.out.println(ttime + 1);
                    return;
                }
                pq.offer(new int[]{cur - 1, ttime + 1});
                isvisited[cur - 1] = true;
            }
            if(cur + 1 <= 100000 && !isvisited[cur + 1]){
                if(cur + 1 == k){
                    System.out.println(ttime + 1);
                    return;
                }
                pq.offer(new int[]{cur + 1, ttime + 1});
                isvisited[cur + 1] = true;
            }
        }
    }
}