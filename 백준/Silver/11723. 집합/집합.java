import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        // x는 1~20
        int t = Integer.parseInt(br.readLine());
        boolean[] sets = new boolean[21];
        int x;
        while(t-- > 0) {
            String strs[] = br.readLine().split(" ");
            if(strs[0].equals("add")){
                x = Integer.parseInt(strs[1]);
                sets[x] = true;
            }else if(strs[0].equals("remove")){
                x = Integer.parseInt(strs[1]);
                sets[x] = false;
            }else if(strs[0].equals("check")){
                x = Integer.parseInt(strs[1]);
                sb.append(sets[x] ? 1 : 0).append("\n");
            }else if(strs[0].equals("toggle")){
                x = Integer.parseInt(strs[1]);
                sets[x] = (sets[x] ? false : true);
            }else if(strs[0].equals("all")){
                for(int i = 1; i <= 20; i++) sets[i] = true;
            }else if(strs[0].equals("empty")){
                for(int i = 1; i <= 20; i++) sets[i] = false;
            }
        }
        System.out.println(sb);
    }
}