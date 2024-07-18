import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) throws IOException {
        Queue<Integer> q = new LinkedList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());

        int lastPushNum = 0;
        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            if(str.equals("push")){
                int inputNum = Integer.parseInt(st.nextToken());
                q.add(inputNum);
                lastPushNum = inputNum;
            }else if(str.equals("pop")){
                if(q.isEmpty()) sb.append("-1\n");
                else{
                    sb.append(q.poll()).append("\n");
                }
            }else if(str.equals("size")){
                sb.append(q.size()).append("\n");
            }else if(str.equals("empty")){
                if(q.isEmpty()) sb.append("1\n");
                else sb.append("0\n");
            }else if(str.equals("front")){
                if(q.isEmpty()) sb.append("-1\n");
                else sb.append(q.peek()).append("\n");
            }else{ // back
                if(q.isEmpty()) sb.append("-1\n");
                else sb.append(lastPushNum).append("\n");
            }
        }
        System.out.println(sb);

    }
}