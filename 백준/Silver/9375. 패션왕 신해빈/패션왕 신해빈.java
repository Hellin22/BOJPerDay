
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
import java.io.IOException;
import java.lang.StringBuilder;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        HashMap<String, Integer> hm = new HashMap<>();
        ArrayList<Integer> arr = new ArrayList<>();
        int cnt = 1;
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            hm.clear();
            int n = Integer.parseInt(br.readLine());
            for (int i = 0; i < n; i++) {
                String[] strs = br.readLine().split(" ");
                if (hm.containsKey(strs[1])) {
                    hm.put(strs[1], hm.get(strs[1]) + 1);
                } else {
                    hm.put(strs[1], 1);
                }
            }
            Iterator<String> it1 = hm.keySet().iterator();
            while (it1.hasNext()) {
                String key = it1.next();
                arr.add(hm.get(key) + 1);
            }

            for(int i = 0; i < arr.size(); i++){
                cnt *= arr.get(i);
            }
            sb.append((cnt - 1) + "\n");
            cnt = 1;
            arr.clear();
        }
        System.out.println(sb);
    }
}