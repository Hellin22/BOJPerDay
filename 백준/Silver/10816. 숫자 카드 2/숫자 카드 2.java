import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        HashMap<Integer, Integer> map = new HashMap<>();
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for (int i = 0; i < n; i++) {
            int x = in.nextInt();
            if(map.containsKey(x)) {
                map.put(x, map.get(x) + 1);
            }else{
                map.put(x, 1);
            }
        }
        StringBuilder stringBuilder = new StringBuilder();
        int m = in.nextInt();
        for (int i = 0; i < m; i++) {
            int x = in.nextInt();
            if(map.containsKey(x)) {
                stringBuilder.append(map.get(x) + " ");
            }else {
                stringBuilder.append(0 + " ");
            }
        }
        System.out.print(stringBuilder);
    }
}
