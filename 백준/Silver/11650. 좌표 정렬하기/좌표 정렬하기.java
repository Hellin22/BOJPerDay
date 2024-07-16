import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static class pair implements Comparable<pair>{
        int x;
        int y;

        public pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(pair other) {
            if(this.x != other.x){
                return this.x - other.x;
            }else{
                return this.y - other.y;
            }

        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        ArrayList<pair> list = new ArrayList<>();

        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++){

            st= new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            pair p = new pair(x, y);
            list.add(p);
        }
        Collections.sort(list);

        for(int i = 0; i < list.size(); i++){
            sb.append(list.get(i).x).append(" ").append(list.get(i).y).append("\n");
        }
        System.out.println(sb);
    }
}