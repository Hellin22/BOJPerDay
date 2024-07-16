import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        Scanner sc = new Scanner(System.in);
        StringBuilder stringBuilder = new StringBuilder();

        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            String str = sc.next();
            if(str.equals("push")){
                int inputValue = sc.nextInt();
                stack.push(inputValue);
            }else if(str.equals("pop")){
                if(stack.empty()) stringBuilder.append(-1 + "\n");
                else stringBuilder.append(stack.pop() + "\n");
            }else if(str.equals("size")){
                stringBuilder.append(stack.size() + "\n");
            }else if(str.equals("empty")){
                if(stack.empty()) stringBuilder.append(1 + "\n");
                else stringBuilder.append(0 + "\n");
            }else{
                if(stack.empty()) stringBuilder.append(-1 + "\n");
                else stringBuilder.append(stack.peek() + "\n");
            }
        }
        System.out.println(stringBuilder);
    }
}
