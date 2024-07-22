import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static class pair implements Comparable<pair> {
        int a;
        String b;
        pair(int a, String b){
            this.a = a;
            this.b = b;
        }
        @Override
        public int compareTo(pair other){
            if(this.a != other.a){
                return this.a - other.a;
            }
            return other.a - this.a;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        ArrayList<pair> pairs = new ArrayList<pair>();
        for(int i = 0; i < t; i++) {
            int a = sc.nextInt();
            String b = sc.next();
            pairs.add(new pair(a, b));
        }
        Collections.sort(pairs);

        for (int i = 0; i < t; i++) {
            System.out.print(pairs.get(i).a + " " + pairs.get(i).b + "\n" );
        }
    }
}
