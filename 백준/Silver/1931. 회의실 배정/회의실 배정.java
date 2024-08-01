
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<int[]> list = new ArrayList<>();
        int a = 0;
        for(int i = 0; i < n; i++) {
            String[] strs = br.readLine().split(" ");
            list.add(new int[]{Integer.parseInt(strs[0]), Integer.parseInt(strs[1])});
        }

        Collections.sort(list, (o1, o2) -> {
           if(o1[1] == o2[1]) return o1[0] - o2[0];
           return o1[1] - o2[1];
        });

        int finishTime = 0;
        for(int i = 0; i < list.size(); i++){
            if(list.get(i)[0] >= finishTime){
                finishTime = list.get(i)[1];
                a++;
            }
        }
        System.out.println(a);
    }

}