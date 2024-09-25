import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        TreeSet<String> set = new TreeSet<>();

        for(int i = 0; i < n; i++){
            String[] strs = br.readLine().split(" ");
            if(strs[1].equals("enter")){
                set.add(strs[0]);
            }else{
                set.remove(strs[0]);
            }
        }

        Iterator<String> it = set.descendingIterator();
        while(it.hasNext()){
            sb.append(it.next()).append("\n");
        }
        System.out.println(sb);
    }
}