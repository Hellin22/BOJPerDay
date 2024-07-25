
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.util.ArrayList;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input, "-+");
        ArrayList<Integer> list = new ArrayList<>();
        while(st.hasMoreTokens()){
            list.add(Integer.parseInt(st.nextToken()));
        }

        int cnt = 1;
        for(int i = 0; i < input.length(); i++){
            if(input.charAt(i) == '+' ){
                cnt++;
            }else if(input.charAt(i) == '-'){
                break;
            }
        }
        int sum = 0;
        for(int i = 0; i < cnt; i++){
            sum += list.get(i);
        }
        for(int i = cnt; i < list.size(); i++){
            sum-=list.get(i);
        }
        System.out.println(sum);
    }
}