import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;
class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i = 0; i < s.length(); i++){
            arr.add(s.charAt(i)-'0');
        }

        Collections.sort(arr, Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < arr.size(); i++){
            sb.append(arr.get(i));
        }
        System.out.println(sb);
    }
}