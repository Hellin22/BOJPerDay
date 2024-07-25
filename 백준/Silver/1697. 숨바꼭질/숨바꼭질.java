
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.io.IOException;
import java.lang.StringBuilder;
import java.util.LinkedList;
import java.util.Queue;

class Main{
    static int[] isvisited = new int[100001];

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        String[] inputArr = input.split(" ");
        int n = Integer.parseInt(inputArr[0]);
        int k = Integer.parseInt(inputArr[1]);
        int ans = 0;

        if(n == k) ans = 0;

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{n, 0});
        isvisited[n] = 1;

        if(n != k){
            while(!q.isEmpty()){
                int x = q.peek()[0];
                int cnt = q.poll()[1];

//                System.out.println(x + " " + cnt);

                if(x-1 >= 0 && isvisited[x-1] == 0){
                    if(x-1 == k) {
                        ans = cnt + 1;
                        break;
                    }
                    isvisited[x-1] = 1;
                    q.add(new int[]{x-1, cnt+1});
                }
                if(x+1 <= 100000 && isvisited[x+1] == 0){
                    if(x+1 == k){
                        ans = cnt + 1;
                        break;
                    }
                    isvisited[x+1] = 1;
                    q.add(new int[]{x+1, cnt+1});
                }
                if(x * 2 <= 100000 && isvisited[2*x] == 0){
                    if(x * 2 == k){
                        ans = cnt + 1;
                        break;
                    }
                    isvisited[2*x] =1;
                    q.add(new int[]{2*x, cnt+1});
                }
            }
        }
        System.out.println(ans);
        br.close();
    }
}