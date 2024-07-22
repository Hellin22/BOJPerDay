import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


class Main {
    public static class pair{
        int num;
        int cnt;

        pair(int num, int cnt){
            this.num = num;
            this.cnt = cnt;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int x = Integer.parseInt(br.readLine());
        Queue<pair> q = new LinkedList<>(); // 1로 만들어야함.
        q.add(new pair(x, 0));

        while(!q.isEmpty()){
            int num = q.peek().num;
            int cnt = q.poll().cnt;
            if(num == 1) {
                System.out.println(cnt);
                return;
            }
            int tmpnum;
            if(num % 3 == 0){
                tmpnum = num;
                tmpnum /= 3;
                q.add(new pair(tmpnum, cnt+1));
            }
            if(num % 2 == 0){
                tmpnum = num;
                tmpnum /= 2;
                q.add(new pair(tmpnum, cnt+1));
            }
            tmpnum = num;
            tmpnum-=1;
            q.add(new pair(tmpnum, cnt+1));
        }
    }
}