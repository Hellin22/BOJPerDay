import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Queue<Integer> q = new LinkedList<Integer>();
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i = 1; i <= n; i++){
            q.add(i);
        }

        int cnt = 1;
        while(!q.isEmpty()){
            Integer pollInt = q.poll();
            if(cnt != k){
                q.add(pollInt);
                cnt++;
            }else{
                list.add(pollInt);
                cnt = 1;
            }
        }

        sb.append("<");
        for (int i = 0; i < list.size()-1; i++) {
            sb.append(list.get(i)).append(", ");
        }
        sb.append(list.get(list.size()-1));
        sb.append(">");

        System.out.println(sb);



    }
}