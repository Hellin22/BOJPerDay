
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.io.IOException;
import java.lang.StringBuilder;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        StringBuilder sb = new StringBuilder();
        String[] inputArr = input.split(" ");
        int n = Integer.parseInt(inputArr[0]);
        int m = Integer.parseInt(inputArr[1]);
        HashMap<Integer, String> intToString = new HashMap<>();
        HashMap<String, Integer> StringToInt = new HashMap<>();

        for(int i = 1; i <= n; i++){
            String name = br.readLine();
            intToString.put(i, name);
            StringToInt.put(name, i);
        }

        for(int i = 0; i < m; i++){
            String quesString = br.readLine();
            if((int)quesString.charAt(0) < (int)'1' || quesString.charAt(0) > (int)'9'){
                sb.append(StringToInt.get(quesString) + "\n");
            }else{
                sb.append(intToString.get(Integer.parseInt(quesString)) + "\n");;
            }
        }
        System.out.print(sb);
    }
}