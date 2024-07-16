import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static class pair implements Comparable<pair>{

        int x;
        int y;

//        public pair(int x, int y){
//            this.x = x;
//            this.y = y;
//        }

        @Override
        public int compareTo(pair other) {
            // y좌표 증가하는순 -> x좌표 증가하는순 (y 오름차순, x 오름차순)
            if(this.y != other.y){
                // y 오름차순
                return this.y - other.y;
            }else{
                // x 오름차순
                return this.x - other.x;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder stringbuilder = new StringBuilder();
        StringTokenizer st;
        ArrayList<pair> list = new ArrayList<>();
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            pair pair = new pair();
            pair.x = x;
            pair.y = y;

            list.add(pair);
        }
        Collections.sort(list);

        for(int i = 0; i < list.size(); i++){
            stringbuilder.append(list.get(i).x).append(" ").append(list.get(i).y).append("\n");
        }

        System.out.println(stringbuilder);
    }
}