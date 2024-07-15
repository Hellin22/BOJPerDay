import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true){
            String s = sc.nextLine();
            if(s.equals(".")) break;
            boolean isString = true;
            Stack<Integer> stck = new Stack<>();
            for(int i = 0; i < s.length(); i++){
                if(s.charAt(i) == '('){
                    stck.push(1);
                }
                else if(s.charAt(i) == '['){
                    stck.push(2);
                }
                else if(s.charAt(i) == ']'){
                    if(stck.empty() || stck.peek() != 2){
                        isString = false;
                        break;
                    }
                    stck.pop();
                }
                else if(s.charAt(i) == ')'){
                    if(stck.empty() || stck.peek() != 1){
                        isString = false;
                        break;
                    }
                    stck.pop();
                }
            }
            if(!stck.empty()) isString = false;

            if(isString) System.out.println("yes");
            else System.out.println("no");
        }
    }
}
